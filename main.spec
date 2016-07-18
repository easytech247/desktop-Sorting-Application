# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\Sulaiman\\workspace\\Automatic Sorting Windows\\src'],
             binaries=None,
             datas=None,
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
          name='Desktop Sorting Application',
          debug=False,
          strip=False,
          upx=True,
          console=False,
		  icon='C:\Users\Sulaiman\workspace\Automatic Sorting Windows\src\icon.ico')
