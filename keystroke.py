import win32con, win32api

keys = {
    "F1": 0x70,
    "F2": 0x71,
    "F3": 0x72,
    "F4": 0x73,
    "F5": 0x74,
    "F6": 0x75,
    "F7": 0x76,
    "F8": 0x77,
    "F9": 0x78,
    "F10": 0x79,
    "F11": 0x7A,
    "F12": 0x7B
}

def keystroke(key, hwnd):
    key = keys[key]
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, key, 0)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, key, 0)

def listen_keystroke():
    result = win32api.GetKeyState(0x52)
    if result < 0:
        return True
    else:
        return False