"""Release-builder regression tests using real Git indexes and ZIP readback."""
import hashlib
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest
import zipfile


class ReleaseBuilderTests(unittest.TestCase):
    def setUp(self):
        workspace = Path(__file__).resolve().parents[1]
        self.temp = tempfile.TemporaryDirectory(prefix='.release-test-', dir=workspace)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        assert self.root.resolve().is_relative_to(workspace.resolve())
        subprocess.run(['git', 'init', '-q', str(self.root)], check=True)
        subprocess.run(['git', '-C', str(self.root), 'config', 'core.autocrlf', 'false'], check=True)
        skill = self.root/'skills/aps-quantum-writing'
        files = {'VERSION': b'1.2.0\n',
                 'assets/heading-examples/APS-heading-layout-examples.pdf': b'fixture-pdf',
                 'evidence/heading-revalidation-2026-10-20.zip': b'fixture-evidence'}
        for name, data in files.items():
            p = skill/name; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(data)
        (skill/'SHA256SUMS').write_text(''.join(
            f'{hashlib.sha256(data).hexdigest()}  {name}\n' for name,data in sorted(files.items())),
            encoding='utf-8')
        (self.root/'README.md').write_bytes(b'INDEX VERSION\n')
        subprocess.run(['git', '-C', str(self.root), 'add', '.'], check=True)
        spec = importlib.util.spec_from_file_location('release12', Path(__file__).with_name('build_release_1_2.py'))
        self.builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.builder)
        self.builder.ROOT = self.root

    def test_clean_index_and_worktree_are_archived(self):
        out = self.root/'out'
        self.builder.build(out)
        with zipfile.ZipFile(out/'research-skills-1.2.0-source.zip') as z:
            self.assertEqual(z.read('research-skills/README.md'), b'INDEX VERSION\n')

    def test_unstaged_source_change_is_rejected_before_build(self):
        (self.root/'README.md').write_bytes(b'UNSTAGED WORKTREE VERSION\n')
        with self.assertRaisesRegex(ValueError, 'Unstaged'):
            self.builder.build(self.root/'out')
        self.assertFalse((self.root/'out').exists())


if __name__ == '__main__':
    unittest.main()
