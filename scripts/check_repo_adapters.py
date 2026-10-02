#!/usr/bin/env python3
"""Check only Git ignore boundaries; no installs, network or legal-skill execution."""
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def ignored(path):
    result = subprocess.run(
        ["git", "check-ignore", "--no-index", "-q", "--", path], cwd=ROOT,
        check=False,
    )
    if result.returncode not in (0, 1):
        raise RuntimeError(f"git check-ignore failed for {path}")
    return result.returncode == 0


def main():
    manifest = json.loads((ROOT / "ai/repo-standard.json").read_text())
    for canonical in manifest["skills"]:
        name = Path(canonical).parent.name
        for client in (".agents", ".claude"):
            adapter = f"{client}/skills/{name}"
            if ignored(adapter):
                raise SystemExit(f"FAIL: versioned adapter is ignored: {adapter}")
    for local_only in (
        ".claude/settings.json", ".claude/settings.local.json",
        ".claude/skills/local-only/SKILL.md",
    ):
        if not ignored(local_only):
            raise SystemExit(f"FAIL: local Claude configuration is not ignored: {local_only}")
    print("PASS: repo adapters are trackable; local Claude files remain ignored")


if __name__ == "__main__":
    main()
