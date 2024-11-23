# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py', 'gun_data.json', 'resource_rc.py', 'common.py'],
    pathex=['F:/Object/GitHub/CuteAide'],
    binaries=[],
    datas=[
        ('F:/Object/GitHub/CuteAide/basic/', 'basic'),
        ('F:/Object/GitHub/CuteAide/resource/', 'resource'),
        ('F:/Object/GitHub/CuteAide/libs/', 'libs'),

        ('F:/Object/GitHub/CuteAide/tools/', 'tools'),
        ('F:/Object/GitHub/CuteAide/views/', 'views'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='CuteAide',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    icon='resource/images/log.ico',
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
