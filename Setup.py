import sys
from cx_Freeze import setup,Executable

base= None
if sys.platform == "win32": base:"Win32GUI"

opts ={"include_files": ["lotto.png"], "includes" : ["re"]}

setup(
    name = "Lotto",
    version = "1.0.1",
    description = "Lottery number picker",
    author = "Darshil Parikh",
    options = {"build.exe" : opts},
    executables = [Executable("main.py", base =base)]

)
