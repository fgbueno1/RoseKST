import win32api, win32process
import win32gui, win32ui, win32con
import sys
import time
from ReadWriteMemory import ReadWriteMemory

from keystroke import keystroke

base_address = "0x00000A90"
mana_address = "0x0F37F578"

def main():
    game =list_window_names()
    hwnd = win32gui.FindWindow(None, game)
    
    old_mana = 0

    while True:
        old_mana = food(hwnd, old_mana)
        runemaker(hwnd)
        time.sleep(4)

def list_window_names():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            if win32gui.GetWindowText(hwnd).find("Jornada") != -1:
                win_name = win32gui.GetWindowText(hwnd)
                ctx.append(win_name)
    wins =[]
    win32gui.EnumWindows(winEnumHandler, wins)
    return wins[0]

def get_mana(hwnd):
    thread_id, my_pid = win32process.GetWindowThreadProcessId(hwnd)
    rwm = ReadWriteMemory()
    process = rwm.get_process_by_id(my_pid)
    process.open()
    mp = process.get_pointer(base_address, offsets=[mana_address])   
    mp = process.readDouble(mp)
    process.close()
    return int(mp)

def eat(hwnd):
    x = 1204
    y = 567
    lParam = win32api.MAKELONG(int(x), int(y))
    win32gui.SendMessage(hwnd, win32con.WM_MOUSEMOVE, 0, lParam)
    win32gui.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, lParam)
    win32gui.SendMessage(hwnd, win32con.WM_RBUTTONUP, 0, lParam)

def food(hwnd, old_mana):
    mana = get_mana(hwnd)
    if mana == old_mana:
        key = 'F10'
        keystroke(key, hwnd)
        time.sleep(1)
        eat(hwnd)
    else:
        old_mana = mana
    return old_mana

def move_blank_rune(hwnd):
    start_x = 1283
    start_y = 509
    end_x = 1205
    end_y = 253

    lParam = win32api.MAKELONG(int(start_x), int(start_y))
    win32gui.SendMessage(hwnd, win32con.WM_MOUSEMOVE, 0, lParam)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    time.sleep(1)

    lParam = win32api.MAKELONG(int(end_x), int(end_y))
    win32gui.SendMessage(hwnd, win32con.WM_MOUSEMOVE, 0, lParam)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)

def runemaker(hwnd):
    mana = get_mana(hwnd)
    if mana > 600:
        move_blank_rune(hwnd)
        time.sleep(0.2)
        key = 'F11'
        keystroke(key, hwnd)
        


if __name__ == "__main__":
    main()