"""Prepare the static files for the configured GitHub Pages main/docs source."""
import argparse
from pathlib import Path

from validate_site import PUBLIC_FILES, validate

ROOT = Path(__file__).resolve().parents[1]
DESTINATION = ROOT / "docs"


def prepare(check=False):
    validate()
    expected = {name: (ROOT / name).read_bytes() for name in PUBLIC_FILES}
    expected[".nojekyll"] = b""
    if check:
        actual = {
            str(path.relative_to(DESTINATION)): path.read_bytes()
            for path in DESTINATION.rglob("*") if path.is_file()
        }
        if actual != expected:
            raise ValueError("Published docs differ from source. Run python3 scripts/prepare_pages.py")
        print("GitHub Pages docs match the public source files.")
        return
    DESTINATION.mkdir(exist_ok=True)
    for filename, content in expected.items():
        (DESTINATION / filename).write_bytes(content)
    print("Prepared static GitHub Pages files in docs/.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    prepare(parser.parse_args().check)
