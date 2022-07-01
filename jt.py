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
        runemaker(hwnd)
        old_mana = food(hwnd, old_mana)
        open_new_backpack(hwnd)
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

def right_click(hwnd, click_point):
    lParam = win32api.MAKELONG(int(click_point[0]), int(click_point[1]))
    win32gui.SendMessage(hwnd, win32con.WM_MOUSEMOVE, 0, lParam)
    win32gui.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, lParam)
    win32gui.SendMessage(hwnd, win32con.WM_RBUTTONUP, 0, lParam)

def food(hwnd, old_mana):
    mana = get_mana(hwnd)
    if mana == old_mana:
        key = 'F10'
        keystroke(key, hwnd)
        time.sleep(1)
        click_point = [1204, 716]
        right_click(hwnd, click_point)
    else:
        old_mana = mana
    return old_mana

def move(hwnd, move_points):
    lParam = win32api.MAKELONG(int(move_points[0]), int(move_points[1]))
    win32gui.SendMessage(hwnd, win32con.WM_MOUSEMOVE, 0, lParam)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    time.sleep(1)

    lParam = win32api.MAKELONG(int(move_points[2]), int(move_points[3]))
    win32gui.SendMessage(hwnd, win32con.WM_MOUSEMOVE, 0, lParam)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)

def open_new_backpack(hwnd):
    mana = get_mana(hwnd)
    if mana > 660:
        move_points = [1205, 253, 1283, 655] #move rune to bp
        move(hwnd, move_points)
        time.sleep(0.5)
        click_point = [1209, 718] #close bp
        right_click(hwnd, click_point)
        time.sleep(0.5)
        move_points = [1202, 510, 139, 367] #move bp to other side
        move(hwnd, move_points)
        time.sleep(0.5)
        click_point = [1204, 510] #open new rune bp
        right_click(hwnd, click_point)
        time.sleep(0.5)
        move_points = [1241, 526, 1241, 703] #expand bp
        move(hwnd, move_points)
        time.sleep(1)
        click_point = [1278, 218] #open main bp
        right_click(hwnd, click_point)
        time.sleep(0.5)
        runemaker(hwnd)
        time.sleep(2)

def runemaker(hwnd):
    mana = get_mana(hwnd)
    if mana > 600:
        move_points = [1283, 655, 1205, 253]
        move(hwnd,move_points)
        time.sleep(0.2)
        key = 'F11'
        keystroke(key, hwnd)
        

if __name__ == "__main__":
    main()