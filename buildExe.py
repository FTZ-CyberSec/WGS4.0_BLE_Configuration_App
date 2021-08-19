import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"]}
base = None
if sys.platform == "win32":
    base = "WIN32GUI"

setup(  name = "Programm", 
        version = "0.1",
        options = {"build_exe": build_exe_options},
        executables =[Executable ("mainui_Work.py", base = base)])