# -*- mode: python -*-

block_cipher = None


a = Analysis(['diff_all.py'],
             pathex=['C:\\Script\\20180722_Diff_all'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='diff_all',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
