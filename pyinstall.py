#!/usr/bin/env python3

from pathlib import Path
import subprocess
import sys
import platform
import secrets


IS_WIN = sys.platform.startswith("win")
ARCH = '64' in platform.machine() and '64' or '32'
KEY = secrets.token_hex(16)
NAME = "crypto2regedit"
SELF_DIR = Path(__file__).parent
UPX = Path(f"d:/progs/upx/win{ARCH}/upx.exe")

DIST = SELF_DIR / "dist" / NAME
FILE = SELF_DIR / f"{NAME}.py"


def make_exe():
    subprocess.check_call(["d:/python/Python38-32/Scripts/pyinstaller.exe",
                           "-y",
                           "--clean",
                           "--name", NAME,
                           "--console",
                           # "--upx-dir", UPX.parent,
                           "--onefile",
                           FILE])


if __name__ == "__main__":
    make_exe()
