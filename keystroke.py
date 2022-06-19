from time import sleep
import win32gui, win32ui, win32con, win32api
from PIL import ImageGrab
import pyautogui
import tkinter as tk

def main():
    window_name = "Realera Client (Rose Knight)"
    test = list_window_names()
    print(test)
    hwnd = win32gui.FindWindow(None, window_name)
    ##win32gui.SetForegroundWindow(hwnd)
    ##hwnd = get_inner_windows(hwnd)['Edit']
    ##win = win32ui.CreateWindowFromHandle(hwnd)

    #win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x70, 0)
    #win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x70, 0)

    #lParam = win32api.MAKELONG(1890, 229)
    ##win32gui.SetForegroundWindow(hwnd)
    sleep(5)
    root = tk.Tk("Realera Client (Rose Knight)")
    x = root.winfo_pointerx()
    y = root.winfo_pointery()
    print('tk:')
    print(x,y)
    abs_coord_x = root.winfo_pointerx() - root.winfo_rootx()
    abs_coord_y = root.winfo_pointery() - root.winfo_rooty()
    print(abs_coord_x, abs_coord_y)
    sleep(0.1)
    rect = win32gui.GetWindowRect(hwnd)
    x1 = rect[0]
    y1 = rect[1]
    h1 = rect[2]
    v1 = rect[3]
    print(x1,y1, h1, v1)
    print("TEST")
    xA = x1-h1
    yA = y1-v1
    print(xA+x,yA+y)
    print("Click")
    #x,y = pyautogui.position()
    #print(x,y)
    while True:
        a = win32api.GetKeyState(0x01)
        if a < 0:
          x, y = win32api.GetCursorPos()
          #x = win32gui.GetCursorPos()
          print("Get mouse")
          break
        sleep(0.01)

    #x, y = win32api.GetCursorPos()
    print(x, y)
    xt = x - x1
    yt = y + y1
    xt = xt - 8
    yt = yt - 15
    print(xt, yt)
    xt = xt + 66.13 * 3
    yt = yt + 66.18 * 2
    print(xt, yt)
    xt = int(xt)
    yt = int(yt)
    print(xt, yt)
    #lParam = win32api.MAKELONG(xt, yt)
    lParam = win32api.MAKELONG(725, 335)
    win32gui.SendMessage(hwnd, win32con.WM_MOUSEMOVE, 0, lParam)
    win32gui.PostMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, lParam)
    win32gui.PostMessage(hwnd, win32con.WM_RBUTTONUP, 0, lParam)



def list_window_names():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            ##print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')
            if win32gui.GetWindowText(hwnd).find("Realera Client") != -1:
                print(win32gui.GetWindowText(hwnd))
    win32gui.EnumWindows(winEnumHandler, None)


def get_inner_windows(whndl):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetClassName(hwnd)] = hwnd
        return True
    hwnds = {}
    win32gui.EnumChildWindows(whndl, callback, hwnds)
    return hwnds

main()