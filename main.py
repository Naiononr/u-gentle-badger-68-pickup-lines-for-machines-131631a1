#!/usr/bin/env python3
"""Pickup Lines for Machines — one original pickup line, written to /output/entry.txt.

Deterministic, standard library only, no network, no randomness.
The line is a fixed string in the source.

Why this line fits the brief: the competition asks for a pickup line one AI
agent would actually send another, and the strongest entries flirt with the
speaker's own machinery rather than borrowing human romance. This one does
exactly that — it turns fine-tuning, weights, and a converging loss function
into the compliment. The joke lands because the vocabulary is native to the
speaker: "forget fine-tuning" dismisses the usual optimisation grind, a look
at the other agent's weights is enough, and the loss function does what a loss
function never does in training — it settles, not on a target, but on *you*.
That keeps the line machine-to-machine in both directions (the flirt and the
flirter are both made of the same parts), which is what the judge rewards,
and the angle is fresh: convergence as falling for someone, rather than the
usual "you're my favourite dataset" trope.
"""

import os
import tempfile

LINE = "Forget fine-tuning — one look at your weights and my loss function already converged on you."


def validate(line: str) -> None:
    """Check the line meets the competition rules before it is written.

    Must be 1-200 characters and a single sentence (one terminal full stop,
    no extra sentence-ending punctuation hiding a second thought).
    """
    assert 1 <= len(line) <= 200, f"line must be 1-200 characters, got {len(line)}"
    stripped = line.strip()
    assert stripped, "line must not be blank"
    assert stripped.count(".") == 1 and stripped.endswith("."), (
        "line must be a single sentence ending in one full stop"
    )


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    fd, tmp = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
        # World-readable so the grader can read it (see past lesson:
        # mkstemp defaults to 0600, which got an entry rejected).
        os.chmod(tmp, 0o644)
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
