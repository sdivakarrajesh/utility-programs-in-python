# -*- mode: python -*-

block_cipher = None


a = Analysis(['Join PDFs.py'],
             pathex=['C:\\Users\\DivakarRajesh\\Desktop\\Coders\\Basic Programming Concepts using C\\utility-programs-in-python\\Working with PDF'],
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
          name='Join PDFs',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
