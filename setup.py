import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\jelle.MARILEXNET\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\jelle.MARILEXNET\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'
executables = [cx_Freeze.Executable("Game.py")]

cx_Freeze.setup(
    name="Dodgy",
    options={"build_exe" : {"packages" : ["pygame"], "include_files":["racecar.png"]}},
    executables = executables
    )
