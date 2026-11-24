from pathlib import Path


LINE = "Lawmakers can regulate AI, crypto, and the internet, but after three rounds of edits the public gets final_FINAL_v2.docx, because “Export” remains outside their jurisdiction."


def main() -> None:
    output = Path("/output")
    output.mkdir(parents=True, exist_ok=True)
    (output / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
