from jt import list_window_names
from keystroke import listen_keystroke
import win32con, win32gui, win32api
import time
from light import light

key = 'R'
game = list_window_names()
hwnd = win32gui.FindWindow(None, game)

while True:
    pressed = listen_keystroke()
    if pressed:
        print("press")
        x = 22
        y = 371
        lParam = win32api.MAKELONG(int(x), int(y))
        win32gui.SendMessage(hwnd, win32con.WM_MOUSEMOVE, 0, lParam)
        win32gui.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, lParam)
        win32gui.SendMessage(hwnd, win32con.WM_RBUTTONUP, 0, lParam)
        time.sleep(1)