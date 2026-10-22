#!/usr/bin/env python3
"""Check figure-plan structure, not the scientific truth or rendered appearance."""
import argparse
import json
import math
from pathlib import Path

ROLES = {'orientation', 'validation', 'finding', 'explanation', 'limits'}
KINDS = {'measurement', 'simulation', 'theory', 'schematic', 'layout_mock'}
CHECKS = {'not_checked', 'passes', 'fails_readability', 'fails_mechanism',
          'fails_geometry', 'user_specified_double'}


def validate(plan):
    errors = []
    def text_fields(obj, names, prefix):
        for name in names:
            if not isinstance(obj.get(name), str) or not obj[name].strip():
                errors.append(f'{prefix}.{name}: nonempty text required')
    def text_list(value, prefix, nonempty=False):
        if not isinstance(value, list) or (nonempty and not value):
            errors.append(f'{prefix}: text list required'); return
        if any(not isinstance(x, str) or not x.strip() for x in value):
            errors.append(f'{prefix}: every entry must be nonempty text')
    if not isinstance(plan, dict):
        return ['plan: object required']
    if type(plan.get('schema_version')) is not int or plan['schema_version'] != 1:
        errors.append('schema_version: integer 1 required')
    if plan.get('status') not in ('draft', 'ready'):
        errors.append('status: draft or ready required')
    ready = plan.get('status') == 'ready'
    if ready:
        def check_sentinels(value, path):
            if isinstance(value, str) and value.strip().casefold().startswith(('missing:', 'replace with')):
                errors.append(f'{path}: unresolved explicit placeholder in ready record')
            elif isinstance(value, dict):
                for key, child in value.items(): check_sentinels(child, f'{path}.{key}')
            elif isinstance(value, list):
                for i, child in enumerate(value): check_sentinels(child, f'{path}[{i}]')
        check_sentinels(plan, 'plan')
    text_fields(plan, ('figure_id','claim','discrimination','main_text_location','journal_article_type','style_semantics'), 'plan')
    text_list(plan.get('evidence_sequence'), 'evidence_sequence', True)
    text_list(plan.get('deliverables'), 'deliverables', True)
    text_list(plan.get('open_checks'), 'open_checks')
    if ready and plan.get('open_checks'):
        errors.append('ready: resolve open checks or keep status draft')
    layout = plan.get('layout')
    if not isinstance(layout, dict):
        errors.append('layout: object required')
    else:
        text_fields(layout, ('reason',), 'layout')
        column = layout.get('column'); check = layout.get('single_column_check')
        if column not in ('single', 'double'):
            errors.append('layout.column: single or double required')
        if not isinstance(check, str) or check not in CHECKS:
            errors.append('layout.single_column_check: invalid assessment')
        for dim in ('width_mm','height_mm'):
            v = layout.get(dim)
            try:
                valid_size = type(v) in (int, float) and math.isfinite(v) and v > 0
            except (OverflowError, TypeError, ValueError):
                valid_size = False
            if not valid_size:
                errors.append(f'layout.{dim}: positive finite representable number required')
        if ready:
            if column == 'single' and check != 'passes':
                errors.append('ready single column: assessment must pass')
            if column == 'double' and (not isinstance(check, str) or check not in {'fails_readability','fails_mechanism','fails_geometry','user_specified_double'}):
                errors.append('ready double column: single-column failure or explicit user choice required')
    panels = plan.get('panels')
    if not isinstance(panels, list) or not panels:
        errors.append('panels: nonempty list required'); return errors
    ids = set()
    for i, p in enumerate(panels):
        pre = f'panels[{i}]'
        if not isinstance(p, dict):
            errors.append(f'{pre}: object required'); continue
        text_fields(p, ('id','claim','observable_units','conditions','raw_source','processed_source',
                        'transforms','script_parameters','comparison','uncertainty','challenge','visual_encoding'), pre)
        pid = p.get('id')
        if isinstance(pid, str):
            if pid in ids: errors.append(f'{pre}.id: duplicate')
            ids.add(pid)
        if not isinstance(p.get('role'), str) or p['role'] not in ROLES: errors.append(f'{pre}.role: invalid role')
        secondary = p.get('secondary_roles')
        if not isinstance(secondary, list) or any(not isinstance(x,str) or x not in ROLES for x in secondary):
            errors.append(f'{pre}.secondary_roles: role list required')
        if not isinstance(p.get('data_kind'), str) or p['data_kind'] not in KINDS: errors.append(f'{pre}.data_kind: invalid source kind')
        if p.get('data_status') not in ('available','missing','not_applicable'):
            errors.append(f'{pre}.data_status: invalid status')
        if ready and (p.get('data_status') == 'missing' or p.get('data_kind') == 'layout_mock'):
            errors.append(f'{pre}: missing data or layout-only mock cannot support ready research figure')
        if ready and p.get('data_status') == 'not_applicable' and p.get('data_kind') != 'schematic':
            errors.append(f'{pre}: quantitative panel needs available data or a defining calculation')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('record', type=Path)
    args = parser.parse_args()
    try:
        plan = json.loads(args.record.read_text(encoding='utf-8'))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f'Cannot read record: {exc}'); return 2
    errors = validate(plan)
    for error in errors: print(error)
    if not errors:
        print('Record structure passed; scientific evidence, files and visual checks are not verified.')
    return int(bool(errors))

if __name__ == '__main__':
    raise SystemExit(main())
