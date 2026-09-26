"""Build Chinese UI and portable ZIP packages for the skill."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
import argparse


ROOT = Path(__file__).resolve().parents[1]
CHINESE_SKILL = ROOT / "scripts" / "SKILL.zh-CN.md"


def iter_payload_files():
    for folder in ("references", "assets", "modules"):
        for path in sorted((ROOT / folder).rglob("*")):
            if not path.is_file():
                continue
            relative = path.relative_to(ROOT)
            if "__pycache__" in path.parts or path.suffix == ".pyc":
                continue
            if relative.parts[:2] == ("assets", "readme"):
                continue
            yield path, relative.as_posix()


def build(output: Path, skill_source: Path) -> None:
    source = skill_source.read_text(encoding="utf-8")
    if not source.startswith("---\n"):
        raise ValueError(f"Frontmatter is missing: {skill_source}")

    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        archive.writestr("SKILL.md", source)
        for path, relative in iter_payload_files():
            archive.write(path, relative)
        for name in ("LICENSE", "THIRD_PARTY_NOTICES.md", "COMMERCIAL_USE.md"):
            archive.write(ROOT / name, name)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--variant", choices=("cn", "portable", "all"), default="all")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    output_dir = args.output_dir.resolve()

    outputs = []
    if args.variant in ("cn", "all"):
        output = output_dir / "resume-site-studio-cn.zip"
        build(output, CHINESE_SKILL)
        outputs.append(output)
    if args.variant in ("portable", "all"):
        output = output_dir / "resume-site-studio-portable.zip"
        build(output, ROOT / "SKILL.md")
        outputs.append(output)

    for output in outputs:
        print(output)


if __name__ == "__main__":
    main()
