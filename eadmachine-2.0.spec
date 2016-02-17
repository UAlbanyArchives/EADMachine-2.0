# -*- mode: python -*-
a = Analysis(['EADMachine-2.0.py'],
             pathex=['C:\\Projects\\EADMachine-2.0'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries + [('msvcp100.dll', 'C:\\Windows\\System32\\msvcp100.dll', 'BINARY'), ('msvcr100.dll', 'C:\\Windows\\System32\\msvcr100.dll', 'BINARY')]
		  if sys.platform == 'win32' else a.binaries,
		  a.datas + [('resources\em.gif', 'resources\em.gif', 'DATA')],
          name='EADMachine-2.0.exe',
          debug=False,
          strip=None,
          upx=True,
		  icon='resources\em.ico',
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='EADMachine-2.0')
