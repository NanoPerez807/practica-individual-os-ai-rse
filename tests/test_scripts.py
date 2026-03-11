import unittest
import subprocess
import sys


class TestScripts(unittest.TestCase):

    def test_figures(self):
        result = subprocess.run([sys.executable, "scripts/figures.py"])
        self.assertEqual(result.returncode, 0)

    def test_keywords(self):
        result = subprocess.run([sys.executable, "scripts/keywords.py"])
        self.assertEqual(result.returncode, 0)

    def test_links(self):
        result = subprocess.run([sys.executable, "scripts/links.py"])
        self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
