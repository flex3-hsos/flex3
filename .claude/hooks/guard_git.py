"""Guard git operations of the FLEX3 project assistant.

Two modes:

* ``python guard_git.py`` runs as a Claude Code PreToolUse hook. It reads the
  tool call from stdin and blocks it (exit code 2) when it would
  - commit without a passed review of exactly the staged changes,
  - commit on ``main``,
  - commit with ``-a``/``--all`` (bypasses the reviewed staging area),
  - push to ``main`` or force-push.
* ``python guard_git.py stamp`` records that the currently staged changes
  passed ``/review``. The stamp lives inside ``.git`` and is never committed.
"""

from __future__ import annotations

import hashlib
import json
import re
import shlex
import subprocess
import sys
from pathlib import Path

PROTECTED_BRANCHES = {"main", "master"}
STAMP_NAME = "flex3-review-stamp"

GIT_COMMIT = re.compile(r"\bgit\b(?:\s+-[cC]\s+\S+)*\s+commit\b(?P<args>[^;&|]*)")
GIT_PUSH = re.compile(r"\bgit\b(?:\s+-[cC]\s+\S+)*\s+push\b(?P<args>[^;&|]*)")


def git(*args: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(["git", *args], capture_output=True, check=False)


def staged_diff_hash() -> str:
    diff = git("diff", "--cached", "--binary", "--no-color", "--no-ext-diff").stdout
    return hashlib.sha256(diff).hexdigest()


def stamp_path() -> Path:
    git_dir = git("rev-parse", "--git-dir").stdout.decode().strip()
    return Path(git_dir) / STAMP_NAME


def current_branch() -> str:
    return git("rev-parse", "--abbrev-ref", "HEAD").stdout.decode().strip()


def block(reason: str) -> None:
    print(reason, file=sys.stderr)
    sys.exit(2)


OPTIONS_WITH_VALUE = {"-m", "--message", "-F", "--file", "-C", "-c", "--author", "--date", "-t"}
STAGING_CHANGES = re.compile(r"\bgit\b(?:\s+-[cC]\s+\S+)*\s+(?:add|rm|mv|restore|stage)\b")


def has_pathspec(args: str) -> bool:
    """Return True if the commit names files, which bypasses the reviewed staging area."""
    try:
        tokens = shlex.split(args)
    except ValueError:
        return False  # unparsable (e.g. heredoc message); the stamp check still applies
    skip_next = False
    for token in tokens:
        if skip_next:
            skip_next = False
        elif token in OPTIONS_WITH_VALUE:
            skip_next = True
        elif token in ("-i", "--include", "-o", "--only") or not token.startswith("-"):
            return True
    return False


def check_commit(args: str, command: str) -> None:
    tokens = args.split()
    if current_branch() in PROTECTED_BRANCHES:
        block(
            "Commit auf 'main' ist nicht erlaubt. Lege zuerst einen Zweig fuer die "
            "Aufgabe an (siehe knowledge-base/standards/git-workflow.md)."
        )
    if any(t in ("-a", "--all") or re.fullmatch(r"-[a-zA-Z]*a[a-zA-Z]*", t) for t in tokens):
        block(
            "'git commit -a' umgeht die gepruefte Vormerkung. Merke die Dateien mit "
            "'git add' vor, fuehre /review aus und committe dann ohne -a."
        )
    if STAGING_CHANGES.search(command):
        block(
            "Vormerken und Committen bitte in getrennten Befehlen: erst 'git add', "
            "dann /review, dann 'git commit'."
        )
    if has_pathspec(args):
        block(
            "Commit mit Dateiangabe umgeht die gepruefte Vormerkung. Merke die Dateien "
            "mit 'git add' vor und committe ohne Pfade."
        )
    path = stamp_path()
    if not path.exists():
        block("Kein Review fuer diese Aenderungen vermerkt. Fuehre zuerst /review aus.")
    if path.read_text(encoding="utf-8").strip() != staged_diff_hash():
        block(
            "Die vorgemerkten Aenderungen weichen vom geprueften Stand ab. Fuehre "
            "/review fuer den aktuellen Stand erneut aus."
        )


def check_push(args: str) -> None:
    tokens = args.split()
    if any(t in ("-f", "--force", "--force-with-lease") or t.startswith("--force") for t in tokens):
        block("Force-Push ist in diesem Repository nicht erlaubt.")
    refspecs = [t for t in tokens if not t.startswith("-")][1:]
    targets = {r.split(":")[-1].removeprefix("refs/heads/").lstrip("+") for r in refspecs}
    if targets & PROTECTED_BRANCHES or (not refspecs and current_branch() in PROTECTED_BRANCHES):
        block(
            "Push nach 'main' ist nicht erlaubt. Aenderungen kommen ueber einen Pull "
            "Request nach 'main' (siehe /ship)."
        )


def run_hook() -> None:
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        return
    if event.get("tool_name") != "Bash":
        return
    command = event.get("tool_input", {}).get("command", "")
    for match in GIT_COMMIT.finditer(command):
        check_commit(match.group("args"), command)
    for match in GIT_PUSH.finditer(command):
        check_push(match.group("args"))


def write_stamp() -> None:
    if not git("diff", "--cached", "--quiet").returncode:
        print("Nichts vorgemerkt. Erst 'git add', dann stempeln.", file=sys.stderr)
        sys.exit(1)
    stamp_path().write_text(staged_diff_hash() + "\n", encoding="utf-8")
    print("Review vermerkt fuer die aktuell vorgemerkten Aenderungen.")


if __name__ == "__main__":
    if sys.argv[1:] == ["stamp"]:
        write_stamp()
    else:
        run_hook()
