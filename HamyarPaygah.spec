# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_all
from pathlib import Path

project_root = Path.cwd()

ar_datas, ar_bins, ar_hiddenimports = collect_all('arabic_reshaper')

# Normalize for single-module packages
if not ar_bins:
    ar_bins = []
if not ar_datas:
    ar_datas = []

a = Analysis(
    ['src/hamyar_paygah/main.py'],
    pathex=[str(project_root / "src")],
    binaries=[],
    datas=[],
    hiddenimports=ar_hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=2,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [('O', None, 'OPTION'), ('O', None, 'OPTION')],
    name='HamyarPaygah',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
