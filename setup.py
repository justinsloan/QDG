from cx_Freeze import setup, Executable
import sys

productName = "QDG: Quantum Diceware Generator"
if 'bdist_msi' in sys.argv:
    sys.argv += ['--initial-target-dir', 'C:\InstallDir\\' + productName]
    sys.argv += ['--install-script', 'setup.py']

exe = Executable(
      script="QDG.py",
      base="Win32GUI",
      targetName="QDG.exe"
     )

setup(
      name="QDG",
      version="1.0",
      author="Justin M. Sloan",
      description="Generates Diceware passphrases using quantum random data.",
      executables=[exe],
      scripts=[
               'setup.py'
               ]
      ) 
