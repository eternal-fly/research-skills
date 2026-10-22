"""Check review bookkeeping and recipe source references, not scientific validity."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

class QuantumReviewLinksTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = json.loads((ROOT/'evidence/quantum-figure-review/ledger.json').read_text(encoding='utf-8'))
        cls.records = cls.ledger['papers']
        cls.by_id = {r['id']:r for r in cls.records}

    def test_partition_and_identity(self):
        baseline = json.loads((ROOT/'evidence/papers.json').read_text(encoding='utf-8'))
        self.assertEqual(len(self.records), len(baseline))
        self.assertEqual(len(self.by_id), len(self.records))
        self.assertEqual({r['doi'].casefold() for r in self.records},
                         {r['doi'].casefold() for r in baseline})

    def test_summary_is_derived(self):
        summary = self.ledger['summary']
        self.assertEqual(summary['metadata_screened'], sum(bool(r['metadata_screened']) for r in self.records))
        self.assertEqual(summary['substantive_review'], sum(bool(r['substantive_review']) for r in self.records))
        self.assertEqual(summary['pixel_inspected_papers'], sum(bool(r['pixel_inspected']) for r in self.records))
        self.assertEqual(summary['full_main_text_review'], sum(r['review_tier']=='full_main_text' for r in self.records))

    def test_recipe_anchors_are_substantive(self):
        source_text = (ROOT/'evidence/quantum-figure-review/sources.md').read_text(encoding='utf-8')
        for filename in ('quantum-figures-manybody.md','quantum-figures-information.md','quantum-figures-devices.md'):
            text = (ROOT/'references'/filename).read_text(encoding='utf-8')
            ids = re.findall(r'sources\.md#([a-z]+-\d{3})',text)
            self.assertTrue(ids)
            for key in ids:
                with self.subTest(recipe=filename, source=key):
                    self.assertIn(key, self.by_id)
                    self.assertTrue(self.by_id[key]['substantive_review'])
                    self.assertIn('## '+key.upper(), source_text)

    def test_substantive_records_have_extent_and_primary_source(self):
        for r in self.records:
            if not r['substantive_review']: continue
            with self.subTest(source=r['id']):
                self.assertTrue(r['read_extent'].strip())
                self.assertTrue(r['observations'])
                self.assertTrue(r['source_url'].startswith(('https://arxiv.org/','https://harvest.aps.org/','https://journals.aps.org/','https://olab.physics.sjtu.edu.cn/papers/')))

    def test_pixel_claims_have_locators(self):
        for r in self.records:
            if r['pixel_inspected']:
                with self.subTest(source=r['id']):
                    self.assertTrue(r['image_locator'].strip())

if __name__ == '__main__':
    unittest.main()
