import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "includes": ["ctypes","win32process","win32con","ReadWriteMemory","tkinter","sys","pyautogui","win32api","win32con","win32gui","time"]}

base = "Win32GUI"

setup(
        name = 'RoseTibiaBot',
        version = "1.0",
        description = "Autobuff bot",
        options = {"build_exe": build_exe_options},
        executables = [Executable("realera.py", base=base)]
)