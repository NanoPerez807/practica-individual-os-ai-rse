import unittest
import subprocess
import os

class TestScripts(unittest.TestCase):

    def run_script(self, script_name):
        scripts_dir = os.path.join(os.path.dirname(__file__), "../scripts")
        # Ejecutar el script desde scripts_dir para que '../papers' funcione
        result = subprocess.run(
            ["python3", script_name],
            cwd=scripts_dir,  # aquí está la clave
            capture_output=True,
            text=True
        )
        print(result.stdout)
        print(result.stderr)
        return result

    def test_figures(self):
        result = self.run_script("figures.py")
        self.assertEqual(result.returncode, 0)

    def test_keywords(self):
        result = self.run_script("keywords.py")
        self.assertEqual(result.returncode, 0)

    def test_links(self):
        result = self.run_script("links.py")
        self.assertEqual(result.returncode, 0)
