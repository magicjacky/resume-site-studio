import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

import yaml

from scripts.package_workbuddy import ROOT, build


class PackageTests(unittest.TestCase):
    def read_frontmatter(self, archive: ZipFile):
        source = archive.read("SKILL.md").decode("utf-8")
        return yaml.safe_load(source.split("---", 2)[1]), source

    def test_chinese_package_has_complete_ui_content(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "cn.zip"
            build(output, ROOT / "scripts" / "SKILL.zh-CN.md")
            with ZipFile(output) as archive:
                frontmatter, source = self.read_frontmatter(archive)
                self.assertEqual(frontmatter["name"], "简历网站工坊")
                self.assertEqual(frontmatter["display_name"], "简历网站工坊")
                self.assertIn("## 工作流程", source)
                self.assertIn("modules/job-fit-evidence-analyzer/SKILL.md", archive.namelist())
                self.assertIn("assets/templates/professional-light/index.html", archive.namelist())
                self.assertIn("assets/templates/professional-light/styles.css", archive.namelist())
                self.assertFalse(any(name.startswith("assets/readme/") for name in archive.namelist()))
                self.assertLess(output.stat().st_size, 100_000)

    def test_portable_package_keeps_standard_name(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "portable.zip"
            build(output, ROOT / "SKILL.md")
            with ZipFile(output) as archive:
                frontmatter, _ = self.read_frontmatter(archive)
                self.assertEqual(frontmatter["name"], "resume-site-studio")


if __name__ == "__main__":
    unittest.main()
