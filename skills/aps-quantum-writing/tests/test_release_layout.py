"""Distribution invariants; scientific validity remains a separate review."""
from pathlib import Path
import json
import re
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

def markdown_targets(text):
    # The package uses Markdown fences and TeX math delimiters. Those contexts
    # can contain ](...) without a navigable link; preserve the raw evidence.
    prose = []
    fence = None
    for line in text.splitlines(keepends=True):
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if marker:
            run = marker.group(1)
            if fence is None:
                fence = run
            elif run[0] == fence[0] and len(run) >= len(fence):
                fence = None
            continue
        if fence is None:
            prose.append(line)
    text = ''.join(prose)
    text = re.sub(r'(`+)[\s\S]*?\1', '', text)
    text = re.sub(r'\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)', '', text)
    text = re.sub(r'(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$', '', text)
    text = re.sub(r'(?<!\\)\$[^\n]*?(?<!\\)\$', '', text)
    return re.findall(r'\]\(([^)]+)\)', text)

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
            for target in markdown_targets(path.read_text(encoding='utf-8')):
                target = target.split('#', 1)[0]
                if not target or '://' in target or target.startswith(('mailto:', '<')):
                    continue
                with self.subTest(path=str(path.relative_to(ROOT)), target=target):
                    self.assertTrue((path.parent / unquote(target)).exists())

    def test_local_link_scanner_preserves_prose_links_and_ignores_math_code(self):
        text = r'''
[guide](guide.md)
\[
\mathcal D[A](|m\rangle\langle n|)
\]
Inline \(D[A](x)\) and $D[B](y)$ and `[code](not-a-file)`.
$$D[C](z)$$
```tex
[code](not-a-file)
```
~~~text
[also code](not-a-file)
~~~
[figure](figure.pdf) and [missing](still-checked.json)
'''
        self.assertEqual(markdown_targets(text), ['guide.md', 'figure.pdf', 'still-checked.json'])

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
