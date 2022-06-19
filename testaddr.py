from ReadWriteMemory import ReadWriteMemory
import win32api, win32process, win32gui

rwm = ReadWriteMemory()
window_name_got = "Realera Client (Rose Knight)"
hwnd = win32gui.FindWindow(None, window_name_got)
thread_id, my_pid = win32process.GetWindowThreadProcessId(hwnd)
process = rwm.get_process_by_id(my_pid)
process.open()
PROCESS_ALL_ACCESS = 0x1F0FFF
processHandle = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, my_pid)
modules = win32process.EnumProcessModules(processHandle)
processHandle.close()
base_addr = modules[0]
baseAddress = base_addr + 0x00493FF8
