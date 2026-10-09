"""Distribution invariants; scientific validity remains a separate review."""
from pathlib import Path
import json
import re
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

class ReleaseLayoutTests(unittest.TestCase):
    def test_release_documents_exist(self):
        for name in ('README.md', 'LICENSE', 'THIRD_PARTY_NOTICES.md',
                     'docs/INSTALL.md', 'docs/USAGE.md', 'CONTRIBUTING.md'):
            with self.subTest(name=name):
                self.assertTrue((ROOT / name).is_file(), f'Missing release document: {name}')

    def test_active_instructions_are_english(self):
        for path in [ROOT / 'SKILL.md', *sorted((ROOT / 'references').glob('*.md'))]:
            with self.subTest(path=path.name):
                self.assertIsNone(re.search(r'[\u4e00-\u9fff]', path.read_text(encoding='utf-8')),
                                  'Untranslated active instruction text')

    def test_local_markdown_targets_exist(self):
        for path in ROOT.rglob('*.md'):
            if any(p in {'.git', '.venv', '__pycache__'} for p in path.relative_to(ROOT).parts):
                continue
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
                target = target.split('#', 1)[0]
                if not target or '://' in target or target.startswith(('mailto:', '<')):
                    continue
                with self.subTest(path=str(path.relative_to(ROOT)), target=target):
                    self.assertTrue((path.parent / unquote(target)).exists())

    def test_evidence_index_is_unique_and_balanced(self):
        path = ROOT / 'evidence/papers.json'
        self.assertTrue(path.is_file(), 'Curated evidence index is missing')
        records = json.loads(path.read_text(encoding='utf-8'))
        self.assertEqual(len(records), 700)
        self.assertEqual(len({r['doi'].casefold() for r in records}), 700)
        counts = {}
        for record in records:
            counts[record['journal']] = counts.get(record['journal'], 0) + 1
        self.assertEqual(len(counts), 7)
        self.assertEqual(set(counts.values()), {100})

    def test_three_primary_branches_exist(self):
        entry = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        for branch in ('PLANNING', 'WRITING', 'FIGURES'):
            self.assertIn(branch, entry)
        for name in ('branch-planning.md', 'branch-writing.md', 'branch-figures.md'):
            self.assertTrue((ROOT / 'references' / name).is_file())

if __name__ == '__main__':
    unittest.main()
