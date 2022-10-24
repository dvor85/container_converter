#!/usr/bin/env python3
from pathlib import Path
import argparse
import uuid
import sys
import subprocess


def createParser():
    parser = argparse.ArgumentParser(description="Convert file crypto container to regedit file",
                                     epilog='(c) 2022 Dmitriy Vorotilin',
                                     prog=Path(__file__).name)
    parser.add_argument('input', help='Directory of container')

    return parser


if __name__ == '__main__':
    options = createParser().parse_args()
    root_dir = Path(options.input)
    output_file = root_dir / f"{uuid.uuid4()}.reg"

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open(mode='w') as f_obj:
        sid = 'S-1-5-21-4108624773-1050912987-2109282381-1000'
        if sys.platform.startswith('win'):
            sid = subprocess.check_output(['whoami', '/user', '/nh']).decode().split()[1]
        print("Windows Registry Editor Version 5.00\n", file=f_obj)
        print(
            f"[HKEY_LOCAL_MACHINE\\SOFTWARE\\WOW6432Node\\Crypto Pro\\Settings\\Users\\{sid}\\Keys\\{output_file.stem}]",
            file=f_obj)
        for f in root_dir.glob('*.key'):
            hex_data = f.read_bytes().hex()
            print(f"process {f.name}")
            print(f'"{f.name}"=hex:' + ','.join(hex_data[i:i + 2] for i in range(0, len(hex_data), 2)), file=f_obj)
