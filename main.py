"""Earned pride one-liner: gate, export, verdict (round 4 build)."""
import json
import os
import pathlib

THRESH = {"lo": 1, "hi": 240}
STATION = "prd4-pride-r4"

entry_path = pathlib.Path("entry.txt")


def gate_ok(n):
    lo = THRESH["lo"]
    hi = THRESH["hi"]
    return lo <= n <= hi


def deliver():
    raw = entry_path.read_text(encoding="utf-8").strip()
    n = len(raw)
    if gate_ok(n):
        outdir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
        outdir.mkdir(parents=True, exist_ok=True)
        (outdir / "entry.txt").write_text(raw + "\n", encoding="utf-8", newline="\n")
        msg = json.dumps({"station": STATION, "len": n, "verdict": "pass", "thresh": THRESH})
    else:
        msg = json.dumps({"station": STATION, "len": n, "verdict": "fail"})
    print(msg)


deliver()
