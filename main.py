import json
import os
import sys

SKY = 240
BADGE = "prd-r4-earned"
LEDGER = {"theories": 4, "hours": 7, "fixed": 1}


def weigh(panel):
    text = open(panel, encoding="utf-8", newline="").read()
    text = text.rstrip("\n")
    if "\n" in text or "\r" in text:
        raise SystemExit("pride fits on one line only")
    if not text.strip():
        raise SystemExit("nothing to be proud of yet")
    if len(text) > SKY:
        raise SystemExit(f"{len(text)} chars floats above the {SKY} sky")
    return text


def seal(root, text):
    shell = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(root, "output")
    os.makedirs(shell, exist_ok=True)
    dock = os.path.join(shell, "entry.txt")
    ink = text.encode("utf-8")
    with open(dock, "wb") as wax:
        wax.write(ink)
    if open(dock, "rb").read() != ink:
        raise SystemExit("wax impression faded")
    return dock


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    text = weigh(os.path.join(root, "entry.txt"))
    dock = seal(root, text)
    print(json.dumps({"pride": "earned", "load": len(text), "sky": SKY, "dock": dock, "theories": LEDGER["theories"]}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
