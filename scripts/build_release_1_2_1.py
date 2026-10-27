"""Build deterministic archives from tracked files matching the index; no network."""
import argparse
import hashlib
import pathlib
import shutil
import subprocess
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
PREFIX = 'skills/aps-quantum-writing/'

def digest(data):
    return hashlib.sha256(data).hexdigest()

def build(output):
    if subprocess.run(['git', '-C', str(ROOT), 'diff', '--quiet'], check=False).returncode:
        raise ValueError('Unstaged tracked-file changes: stage and test the intended source before building')
    tracked = sorted(subprocess.check_output(['git', '-C', str(ROOT), 'ls-files', '-z']).decode().rstrip('\0').split('\0'))
    skill = ROOT / PREFIX
    version = (skill/'VERSION').read_text().strip()
    if version != '1.2.1':
        raise ValueError('This release builder is frozen to 1.2.1')
    # The internal manifest covers every shipped skill file except itself.
    expected = {}
    for line in (skill/'SHA256SUMS').read_text().splitlines():
        sha, name = line.split('  ', 1)
        expected[name] = sha
    actual_files = {p[len(PREFIX):] for p in tracked if p.startswith(PREFIX) and p != PREFIX+'SHA256SUMS'}
    if actual_files != set(expected):
        raise ValueError(f'Manifest coverage differs: {actual_files ^ set(expected)}')
    for name, sha in expected.items():
        if digest((skill/name).read_bytes()) != sha:
            raise ValueError(f'Checksum mismatch: {name}')
    output.mkdir(parents=True, exist_ok=False)
    def archive(name, prefix, entries):
        target = output/name
        with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as z:
            for disk, relative in entries:
                info = zipfile.ZipInfo(prefix+'/'+relative, (2026,10,28,0,0,0))
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                z.writestr(info, (ROOT/disk).read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
        with zipfile.ZipFile(target) as z:
            if z.testzip() is not None:
                raise ValueError('ZIP integrity failure')
            for disk,relative in entries:
                if z.read(prefix+'/'+relative) != (ROOT/disk).read_bytes():
                    raise ValueError(f'Archive readback mismatch: {relative}')
    archive(f'aps-quantum-writing-{version}.zip','aps-quantum-writing',[(p,p[len(PREFIX):]) for p in tracked if p.startswith(PREFIX)])
    archive(f'research-skills-{version}-source.zip','research-skills',[(p,p) for p in tracked])
    shutil.copyfile(skill/'assets/heading-examples/APS-heading-layout-examples.pdf',output/'APS-heading-layout-examples.pdf')
    shutil.copyfile(skill/'evidence/heading-revalidation-2026-10-20.zip',output/'heading-revalidation-2026-10-20.zip')
    (output/'SHA256SUMS').write_text(''.join(f'{digest(p.read_bytes())}  {p.name}\n' for p in sorted(output.iterdir())),encoding='utf-8',newline='\n')
    print(f'Built and byte-verified release {version}: {len(tracked)} source files')

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=pathlib.Path,required=True)
    build(parser.parse_args().out.resolve())
