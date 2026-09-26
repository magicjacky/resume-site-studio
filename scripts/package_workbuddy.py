"""Build a WorkBuddy upload ZIP without changing the portable source skill."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
import argparse


ROOT = Path(__file__).resolve().parents[1]
EXTRA = """description_zh: 分析职位匹配，并根据真实简历制作可编辑的个人网站或作品集。
description_en: Analyze job fit and build an editable personal website from real career evidence.
version: 2.0.1
author: magicjacky
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT.parent / "resume-site-studio-workbuddy.zip")
    output = parser.parse_args().output.resolve()
    source = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not source.startswith("---\n"):
        raise ValueError("SKILL.md frontmatter is missing")
    source = source.replace("\n---\n", "\n" + EXTRA + "---\n", 1)
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        archive.writestr("SKILL.md", source)
        for folder in ("references", "assets", "modules"):
            for path in sorted((ROOT / folder).rglob("*")):
                if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc":
                    archive.write(path, path.relative_to(ROOT).as_posix())
        for name in ("README.md", "LICENSE", "THIRD_PARTY_NOTICES.md", "COMMERCIAL_USE.md"):
            archive.write(ROOT / name, name)
    print(output)


if __name__ == "__main__":
    main()
