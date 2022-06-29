import win32con, win32api

def keystroke(key, hwnd):
    if key == 'F1':
        key = 0x70
    elif key == 'F2':
        key = 0x71
    elif key == 'F3':
        key = 0x72
    elif key == 'F4':
        key = 0x73
    elif key == 'F5':
        key = 0x74
    elif key == 'F6':
        key = 0x75
    elif key == 'F7':
        key = 0x76
    elif key == 'F8':
        key = 0x77
    elif key == 'F9':
        key = 0x78
    elif key == 'F10':
        key = 0x79
    elif key == 'F11':
        key = 0x7A
    elif key == 'F12':
        key = 0x7B
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, key, 0)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, key, 0)