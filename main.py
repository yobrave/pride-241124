"""Earned pride one-liner herald."""
import json
import os
from pathlib import Path

crown = 240
MEDAL = "quiet-earned"
line = (Path(__file__).resolve().parent / "entry.txt").read_bytes().decode("utf-8").strip()
grade = len(line)
match grade:
    case 0:
        pride = "empty"
    case g if g > crown:
        pride = "overflowing"
    case _:
        pride = "earned"
if pride == "earned":
    stage = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    stage.mkdir(parents=True, exist_ok=True)
    (stage / "entry.txt").write_bytes(line.encode("utf-8"))
print(json.dumps({"pride": pride, "count": grade}))
