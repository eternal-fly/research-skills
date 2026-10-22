import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class FigurePlanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location('figure_plan', ROOT/'scripts/validate_figure_plan.py')
        cls.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.module)

    def plan(self):
        return {
            'schema_version': 1, 'figure_id': 'F1', 'status': 'ready',
            'claim': 'Test premise only', 'discrimination': 'Compare defined A and B',
            'evidence_sequence': ['Same observable under two conditions'],
            'main_text_location': 'Result paragraph 1', 'journal_article_type': 'PRA Regular Article',
            'layout': {'column': 'single', 'width_mm': 85, 'height_mm': 70,
                       'single_column_check': 'passes', 'reason': 'Final-size comparison legible'},
            'style_semantics': 'A: circle; B: square; common normalization',
            'open_checks': [], 'deliverables': ['figure.pdf', 'make_figure.py'],
            'panels': [{'id': 'a', 'claim': 'A and B differ', 'role': 'finding',
                        'secondary_roles': ['validation'], 'observable_units': 'X (dimensionless)',
                        'conditions': 'Specified finite model; deterministic input',
                        'data_kind': 'theory', 'data_status': 'available',
                        'raw_source': 'model.py revision example', 'processed_source': 'values.csv',
                        'transforms': 'No aggregation', 'script_parameters': 'make_figure.py; stated grid',
                        'comparison': 'A versus B at matched size',
                        'uncertainty': 'Not applicable: exact stipulated example',
                        'challenge': 'Model assumptions constrain interpretation',
                        'visual_encoding': 'Common axes with labeled conditions'}]
        }

    def test_complete_record(self):
        self.assertEqual(self.module.validate(self.plan()), [])

    def test_required_blank_is_rejected(self):
        p = self.plan(); p['panels'][0]['raw_source'] = '  '
        self.assertTrue(self.module.validate(p))

    def test_ready_missing_or_mock_rejected(self):
        for key, value in [('data_status', 'missing'), ('data_kind', 'layout_mock')]:
            p = self.plan(); p['panels'][0][key] = value
            self.assertTrue(self.module.validate(p))

    def test_draft_missing_can_be_recorded(self):
        p = self.plan(); p['status'] = 'draft'; p['panels'][0]['data_status'] = 'missing'
        self.assertEqual(self.module.validate(p), [])

    def test_duplicate_ids_rejected(self):
        p = self.plan(); p['panels'].append(copy.deepcopy(p['panels'][0]))
        self.assertTrue(self.module.validate(p))

    def test_double_column_requires_assessment(self):
        p = self.plan(); p['layout']['column'] = 'double'
        self.assertTrue(self.module.validate(p))
        p['layout']['single_column_check'] = 'fails_mechanism'
        self.assertEqual(self.module.validate(p), [])
        p['layout']['single_column_check'] = 'user_specified_double'
        self.assertEqual(self.module.validate(p), [])

    def test_no_panel_count_width_rule(self):
        p = self.plan()
        for i in range(1,4):
            q = copy.deepcopy(p['panels'][0]); q['id'] = chr(97+i); p['panels'].append(q)
        self.assertEqual(self.module.validate(p), [])

    def test_ready_unchecked_layout_rejected(self):
        p = self.plan(); p['layout']['single_column_check'] = 'not_checked'
        self.assertTrue(self.module.validate(p))

    def test_malformed_types_do_not_crash(self):
        for p in [None, [], {'panels': [None], 'layout': []}, {'panels': 'bad'}]:
            self.assertTrue(self.module.validate(p))

    def test_nested_bad_types_and_nonfinite_sizes(self):
        p = self.plan(); p['panels'][0]['role'] = []
        p['panels'][0]['data_kind'] = {}; p['layout']['single_column_check'] = []
        p['layout']['width_mm'] = float('nan')
        self.assertTrue(self.module.validate(p))

    def test_huge_json_integer_is_an_error_not_crash(self):
        p = self.plan(); p['layout']['width_mm'] = 10**400
        self.assertTrue(self.module.validate(p))

    def test_ready_rejects_explicit_template_sentinels(self):
        p = json.loads((ROOT/'assets/planning/figure-plan.template.json').read_text(encoding='utf-8'))
        p['status'] = 'ready'; p['open_checks'] = []
        p['layout']['single_column_check'] = 'passes'
        p['panels'][0]['data_status'] = 'available'
        self.assertTrue(self.module.validate(p))

    def test_journal_type_is_required(self):
        p = self.plan(); del p['journal_article_type']
        self.assertTrue(self.module.validate(p))

    def test_template_is_valid_draft(self):
        p = json.loads((ROOT/'assets/planning/figure-plan.template.json').read_text(encoding='utf-8'))
        self.assertEqual(p['status'], 'draft')
        self.assertEqual(self.module.validate(p), [])

if __name__ == '__main__':
    unittest.main()
