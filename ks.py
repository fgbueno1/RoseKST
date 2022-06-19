from tkinter import Text
from ReadWriteMemory import ReadWriteMemory
from PySimpleGUI import PySimpleGUI as sg
import win32api, win32process
import win32gui, win32ui, win32con
import sys
import time
import multiprocessing
from pynput import keyboard

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

def healer(baseAddress, valores, pid, hwnd):
    rwm = ReadWriteMemory()
    process = rwm.get_process_by_id(pid)
    process.open()
    while True:
        if valores ['runa'] == True:
            try:
                hp = process.get_pointer(baseAddress, offsets=[0x410])
                hp = process.readDouble(hp)
                heal_hp = valores['rhp_value']
                x = valores['x']
                y = valores['y']
                cx = valores['cx']
                cy = valores['cy']
                if int(hp) < int(heal_hp):
                    lParam = win32api.MAKELONG(int(x), int(y))
                    win32gui.SendMessage(hwnd, win32con.WM_MOUSEMOVE, 0, lParam)
                    win32gui.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, lParam)
                    win32gui.SendMessage(hwnd, win32con.WM_RBUTTONUP, 0, lParam)
                    time.sleep(0.1)
                    lParam = win32api.MAKELONG(int(cx), int(cy))
                    win32gui.SendMessage(hwnd, win32con.WM_MOUSEMOVE, 0, lParam)
                    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
                    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)
                    time.sleep(0.5)
            except:
                continue
        if valores['hp'] == True:
            try:
                key = valores['hp_key']
                hp = process.get_pointer(baseAddress, offsets=[0x410])
                hp = process.readDouble(hp)
                heal_hp = valores['hp_value']
                mp = process.get_pointer(baseAddress, offsets=[0x448])
                mp = process.readDouble(mp)
                heal_mp = valores['hpmp_value']
                if int(hp) < int(heal_hp) and int(mp) > int(heal_mp):
                    keystroke(key, hwnd)
                    time.sleep(0.5)
            except:
                continue
        if valores['lhp'] == True:
            try:
                key = valores['lhp_key']
                hp = process.get_pointer(baseAddress, offsets=[0x410])
                hp = process.readDouble(hp)
                heal_hp = valores['lhp_value']
                mp = process.get_pointer(baseAddress, offsets=[0x448])
                mp = process.readDouble(mp)
                heal_mp = valores['lhpmp_value']
                if int(hp) < int(heal_hp) and int(mp) > int(heal_mp):
                    keystroke(key, hwnd)
                    time.sleep(0.5)
            except:
                continue
        if valores['mp'] == True:
            try:
                key = valores['mp_key']
                mana = process.get_pointer(baseAddress, offsets=[0x448])
                mana = process.readDouble(mana)
                heal_mana = valores['mp_value']
                if int(mana) < int(heal_mana):
                    keystroke(key, hwnd)
            except:
                continue

def mana_trainer(baseAddress, valores, pid, hwnd):
    rwm = ReadWriteMemory()
    process = rwm.get_process_by_id(pid)
    process.open()
    while True:
        if valores['fmt'] == True:
            try:
                key = valores['fspell_key']
                mp = process.get_pointer(baseAddress, offsets=[0x448])
                mp = process.readDouble(mp)
                mt_mp = valores['fspell_value']
                if int(mp) > int(mt_mp):
                    keystroke(key, hwnd)
                    time.sleep(0.5)
            except Exception as e:
                print(e)
                continue
        if valores['mt'] == True:
            try:
                key = valores['spell_key']
                mp = process.get_pointer(baseAddress, offsets=[0x448])
                mp = process.readDouble(mp)
                mt_mp = valores['spell_value']
                if int(mp) > int(mt_mp):
                    keystroke(key,hwnd)
                    time.sleep(0.5)
            except:
                continue
        time.sleep(int(valores['sleep']))

def on_press(key):
    if key == keyboard.Key.space:
        pass
    else:
        return False

def pick_spear(baseAddress, valores, pid, hwnd):
    rwm = ReadWriteMemory()
    process = rwm.get_process_by_id(pid)
    process.open()
    while True:
        listener = keyboard.Listener(on_press=on_press)
        listener.start()  # start to listen on a separate thread
        listener.join()  # remove if main thread is polling self.keys
        

def walker(waypoints, pid, hwnd, address):
    rwm = ReadWriteMemory()
    process = rwm.get_process_by_id(pid)
    process.open()
    rect = win32gui.GetWindowRect(hwnd)
    x1 = rect[0]
    y1 = rect[1]
    print(x1,y1)
    sg.Popup("Clique no centro do seu personagem")
    time.sleep(2)
    while True:
        a = win32api.GetKeyState(0x01)
        if a < 0:
          x, y = win32api.GetCursorPos()
          break
        time.sleep(0.01)
    x = x - x1
    y = y + y1
    x = x - 8
    y = y - 15
    while True:
        for k, v in waypoints.items():
            wx = v[0]
            wy = v[1]
            wz = v[2]
            h = process.get_pointer(address, offsets=[0xAC,0x80,0x0,0x0,0x2C8])
            h = process.read(h)
            h = int(h) - 312
            v = process.get_pointer(address, offsets=[0xAC,0x80,0x0,0x0,0x2CC])
            v = process.read(v)
            sqm_h = int(h) / 15
            sqm_v = int(v) / 11
            pos_x = process.get_pointer(0x00CC4DCC)
            pos_x = process.read(pos_x)
            pos_y = process.get_pointer(0x00CC4DD0)
            pos_y = process.read(pos_y)
            pos_z = process.get_pointer(0x00CC4DD4)
            pos_z = process.read(pos_z)
            while pos_x != wx or pos_y != wy or pos_z != wz:
                is_atk = process.get_pointer(0x00C4AF4)
                is_atk = process.read(is_atk)
                if int(is_atk) == 0:
                    pos_x = process.get_pointer(0x00CC4DCC)
                    pos_x = process.read(pos_x)
                    pos_y = process.get_pointer(0x00CC4DD0)
                    pos_y = process.read(pos_y)
                    pos_z = process.get_pointer(0x00CC4DD4)
                    pos_z = process.read(pos_z)
                    if int(pos_x) > int(wx):
                        walk = int(pos_x) - int(wx)
                        x_walk = walk * sqm_h
                        #x_walk = x_walk * (-1)
                        xt = int(x - x_walk)
                    elif int(pos_x) <= int(wx):
                        walk = int(wx) - int(pos_x)
                        x_walk = walk * sqm_h
                        xt = int(x + x_walk)
                    if int(pos_y) > int(wy):
                        walk = int(pos_y) - int(wy) 
                        y_walk = walk * sqm_v
                        #y_walk = y_walk * (-1)
                        yt = int(y - y_walk)
                    elif int(pos_y) <= int(wy):
                        walk = int(wy) - int(pos_y)
                        y_walk = walk * sqm_v
                        yt = int(y + y_walk)
                    lParam = win32api.MAKELONG(xt, yt)
                    win32gui.SendMessage(hwnd, win32con.WM_MOUSEMOVE, 0, lParam)
                    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
                    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)
                else:
                    time.sleep(0.01)
                time.sleep(0.01)
    
def light(address, pid):
    while True:
        rwm = ReadWriteMemory()
        process = rwm.get_process_by_id(pid)
        process.open()
        light = process.get_pointer(address, offsets=[0xA9])
        process.writeByte(light, 15)
        time.sleep(1)


class bot:
    def __init__(self, win_name):
        self.game = "KingdomSwapDX.exe"
        self.rwm = ReadWriteMemory()
        try:
            self.window_name_got = win_name
            self.hwnd = win32gui.FindWindow(None, self.window_name_got)
            thread_id, self.my_pid = win32process.GetWindowThreadProcessId(self.hwnd)
            self.process = self.rwm.get_process_by_id(self.my_pid)
            self.process.open()
            PROCESS_ALL_ACCESS = 0x1F0FFF
            processHandle = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, self.my_pid)
            modules = win32process.EnumProcessModules(processHandle)
            processHandle.close()
            base_addr = modules[0]
            self.baseAddress = base_addr + 0x00944AF0
            char_name = self.process.get_pointer(self.baseAddress, offsets=[0x30])
            self.char_name = self.process.readString(char_name, 30)
            self.window_name = f"KST - {self.char_name}"
            self.hwnd = win32gui.FindWindow(None, self.window_name)
            self.win_addr = base_addr + 0x00945D80
            self.waypoints = {}
            self.light = multiprocessing.Process(target=light, args=(self.baseAddress, self.my_pid,))
            self.light.start()
        except Exception as e:
            print(e)
            sg.theme('Reddit')
            sg.popup('Por favor inicie o jogo antes de abrir o RoseTibiaBot - KST', background_color='#272424',
            title='Erro ao Iniciar', button_color='#fd6468', text_color='white')
            sys.exit()

    def bot_main(self):
        sg.theme('Reddit')
        layout_title = [
            [sg.Text(f'RoseTibiaBot-KST -- logged as {self.char_name}',font=('Helvetica, 10'), justification='c', background_color='#272424', text_color='white')]
        ]
        layout_buttons = [
            [sg.Button('Healing', button_color='#fd6468'), sg.Button('Cavebot', button_color='#fd6468'),
            sg.Button('Targeting', button_color='#fd6468'), sg.Button('Mana Trainer', button_color='#fd6468'),
            sg.Button('Exit', button_color='#fd6468')]
        ]
        layout = [
            [sg.Canvas(background_color='#272424', size=(400, 10), pad=None)],
            [sg.Column(layout=layout_title, justification='c', element_justification='c', background_color='#272424')],
            [sg.Canvas(background_color='#272424', size=(400, 3), pad=None)],
            [sg.Column(layout=layout_buttons, justification='c', element_justification='c', background_color='#272424')]
        ]
        janela = sg.Window(f'RoseTibiaBot - KST -- logged as {self.char_name}', layout, size=(500,100),
        background_color='#272424', finalize=True, grab_anywhere=True, resizable=False)
        self.healing_flag = 0
        self.mt_flag = 0
        self.cave_flag = 0
        self.way_flag = 1
        self.targeting_flag = 0
        self.spear = 0
        while True:
            eventos, valores = janela.read(timeout=100)
            if eventos == sg.WINDOW_CLOSED or eventos == "Exit":
                try:
                    self.heal.terminate()
                except:
                    pass
                try:
                    self.mt.terminate()
                except:
                    pass
                try:
                    self.cave.terminate()
                except:
                    pass
                try:
                    self.light.terminate()
                except:
                    pass
                try:
                    self.pick.terminate()
                except:
                    pass
                janela.close()
                break
            if eventos == "Healing":
                self.healing()
            if eventos == "Cavebot":
                self.cavebot()
            if eventos == "Targeting":
                sg.popup("in Development...")
            if eventos == "Mana Trainer":
                self.mana_training()

    def cavebot(self):
        sg.theme('Reddit')
        layout_title = [
            [sg.Text('Waypoints',font=('Helvetica, 14'), justification='c', background_color='#272424', text_color='white')]
        ]
        layout_buttons = [
            [sg.Button('Gravar Waypoint', button_color='#fd6468'), sg.Button('Resetar Waypoints', button_color='#fd6468'), 
            sg.Button('Iniciar', button_color='#fd6468'), sg.Button('Pausar', button_color='#fd6468')]
        ]
        layout_way = [
            [sg.Text(self.waypoints, font=('Helvetica, 10'), justification='c', background_color='#272424', text_color='white')]
        ]
        layout = [
            [sg.Canvas(background_color='#272424', size=(400, 10), pad=None)],
            [sg.Column(layout=layout_title, justification='c', element_justification='c', background_color='#272424')],
            [sg.Canvas(background_color='#272424', size=(400, 3), pad=None)],
            [sg.Column(layout=layout_way, justification='c', element_justification='c', background_color='#272424')],
            [sg.Canvas(background_color='#272424', size=(400, 20), pad=None)],
            [sg.Column(layout=layout_buttons, justification='c', element_justification='c', background_color='#272424')]
        ]
        janela = sg.Window(f'RoseTibiaBot - KST -- logged as {self.char_name}', layout, size=(400,300),
        background_color='#272424', finalize=True, grab_anywhere=True, resizable=False)
        while True:
            eventos, valores = janela.read(timeout=100)
            if eventos ==  sg.WINDOW_CLOSED:
                break
            if eventos == 'Gravar Waypoint':
                ways = []
                pos_x = self.process.get_pointer(0x00CC4DCC)
                pos_x = self.process.read(pos_x)
                pos_y = self.process.get_pointer(0x00CC4DD0)
                pos_y = self.process.read(pos_y)
                pos_z = self.process.get_pointer(0x00CC4DD4)
                pos_z = self.process.read(pos_z)
                ways.append(pos_x)
                ways.append(pos_y)
                ways.append(pos_z)
                self.waypoints["pos"+str(self.way_flag)] = ways
                self.way_flag = self.way_flag + 1
                print(self.waypoints)
            if eventos == 'Resetar Waypoints':
                self.waypoints = {}
            if eventos == 'Iniciar':
                try:
                    if self.cave_flag == 1:
                        sg.popup("Cavebot já em execução, primeiro pause para poder alterar")
                    else:    
                        self.cave_flag = 1
                        self.cave = multiprocessing.Process(target=walker, args=(self.waypoints, self.my_pid, self.hwnd, self.win_addr,))
                        self.cave.start()
                except Exception as e:
                    print(e)
                    continue
            if eventos == 'Pausar':
                try:
                    self.cave.terminate()
                    self.cave_flag = 0
                except Exception as e:
                    print(e)
                    continue
            
    def healing(self):
        sg.theme('Reddit')
        layout_hp = [
            [sg.Text('Healing',font=('Helvetica, 14'), justification='c', background_color='#272424', text_color='white')]
        ]
        layout_buttons = [
            [sg.Button('Iniciar', button_color='#fd6468'), sg.Button('Pausar', button_color='#fd6468')]
        ]
        layout = [
            [sg.Canvas(background_color='#272424', size=(400, 10), pad=None)],
            [sg.Column(layout=layout_hp, justification='c', element_justification='c', background_color='#272424')],
            [sg.Canvas(background_color='#272424', size=(400, 3), pad=None)],
            [sg.Checkbox('Light Healing', default=False,key='lhp', background_color='#272424', text_color='white'),
            sg.Combo(['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12'],default_value='',key='lhp_key',readonly=True, background_color='#272424', text_color='white'),
            sg.Text("HP: ", background_color='#272424', text_color='white'),sg.Input(key='lhp_value', background_color='#272424', text_color='white', size=(7,20)),
            sg.Text("MP: ", background_color='#272424', text_color='white'),sg.Input(key='lhpmp_value', background_color='#272424', text_color='white', size=(7,20)), ],
            [sg.Checkbox('Heavy Healing', default=False,key='hp', background_color='#272424', text_color='white'),
            sg.Combo(['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12'],default_value='',key='hp_key',readonly=True, background_color='#272424', text_color='white'),
            sg.Text("HP: ", background_color='#272424', text_color='white'),sg.Input(key='hp_value', background_color='#272424', text_color='white', size=(7,20)),
            sg.Text("MP: ", background_color='#272424', text_color='white'),sg.Input(key='hpmp_value', background_color='#272424', text_color='white', size=(7,20)), ],
            [sg.Checkbox('Mana Healing', default=False,key='mp', background_color='#272424', text_color='white'),
            sg.Combo(['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12'],default_value='',key='mp_key',readonly=True, background_color='#272424', text_color='white'),
            sg.Text("MP: ", background_color='#272424', text_color='white'),sg.Input(key='mp_value', background_color='#272424', text_color='white', size=(7,20)), ],
            [sg.Checkbox('UH', default=False,key='runa', background_color='#272424', text_color='white'),
            sg.Text("HP: ", background_color='#272424', text_color='white'),sg.Input(key='rhp_value', background_color='#272424', text_color='white', size=(7,20)),
            sg.Text("X_pos: ", background_color='#272424', text_color='white'),sg.Input(key='x', background_color='#272424', text_color='white', size=(7,20)),
            sg.Text("Y_pos: ", background_color='#272424', text_color='white'),sg.Input(key='y', background_color='#272424', text_color='white', size=(7,20)),
            sg.Text("Char_X_pos: ", background_color='#272424', text_color='white'),sg.Input(key='cx', background_color='#272424', text_color='white', size=(7,20)),
            sg.Text("Char_Y_pos: ", background_color='#272424', text_color='white'),sg.Input(key='cy', background_color='#272424', text_color='white', size=(7,20)),],
            [sg.Canvas(background_color='#272424', size=(400, 20), pad=None)],
            [sg.Column(layout=layout_buttons, justification='c', element_justification='c', background_color='#272424')]
        ]
        janela = sg.Window(f'RoseTibiaBot - KST -- logged as {self.char_name}', layout, size=(800,270),
        background_color='#272424', finalize=True, grab_anywhere=True, resizable=False)
        while True:
            eventos, valores = janela.read(timeout=100)
            if eventos ==  sg.WINDOW_CLOSED:
                break
            if eventos == 'Pausar':
                try:
                    self.heal.terminate()
                    self.healing_flag = 0
                except Exception as e:
                    print(e)
                    continue
            if eventos == "Iniciar":
                try:
                    if self.healing_flag == 1:
                        sg.popup("Healing já em execução, primeiro pause para poder alterar")
                    else:    
                        self.healing_flag = 1
                        self.heal = multiprocessing.Process(target=healer, args=(self.baseAddress, valores, self.my_pid, self.hwnd,))
                        self.heal.start()
                except Exception as e:
                    print(e)
                    continue

    def mana_training(self):
        sg.theme('Reddit')
        layout_hp = [
            [sg.Text('Mana Trainer',font=('Helvetica, 14'), justification='c', background_color='#272424', text_color='white')]
        ]
        layout_buttons = [
            [sg.Button('Iniciar', button_color='#fd6468'), sg.Button('Pausar', button_color='#fd6468')]
        ]
        layout = [
            [sg.Canvas(background_color='#272424', size=(400, 10), pad=None)],
            [sg.Column(layout=layout_hp, justification='c', element_justification='c', background_color='#272424')],
            [sg.Canvas(background_color='#272424', size=(400, 3), pad=None)],
            [sg.Checkbox('First Spell', default=False,key='fmt', background_color='#272424', text_color='white'),
            sg.Combo(['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12'],default_value='',key='fspell_key',readonly=True, background_color='#272424', text_color='white'),
            sg.Text("MP: ", background_color='#272424', text_color='white'),sg.Input(key='fspell_value', background_color='#272424', text_color='white', size=(7,20)), ],
            [sg.Checkbox('Second Spell', default=False,key='mt', background_color='#272424', text_color='white'),
            sg.Combo(['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12'],default_value='',key='spell_key',readonly=True, background_color='#272424', text_color='white'),
            sg.Text("MP: ", background_color='#272424', text_color='white'),sg.Input(key='spell_value', background_color='#272424', text_color='white', size=(7,20)), ],
            [sg.Text("Sleep: ", background_color='#272424', text_color='white'),sg.Input(key='sleep', background_color='#272424', text_color='white', size=(7,20)), ],
            [sg.Checkbox('Pick Spear', default=False,key='spear', background_color='#272424', text_color='white')],
            [sg.Canvas(background_color='#272424', size=(400, 20), pad=None)],
            [sg.Column(layout=layout_buttons, justification='c', element_justification='c', background_color='#272424')]

        ]
        janela = sg.Window(f'RoseTibiaBot - KST -- logged as {self.char_name}', layout, size=(400,250),
        background_color='#272424', finalize=True, grab_anywhere=True, resizable=False)
        while True:
            eventos, valores = janela.read(timeout=100)
            if eventos ==  sg.WINDOW_CLOSED:
                break
            if eventos == 'Pausar':
                try:
                    self.mt_flag = 0
                    self.mt.terminate()
                except Exception as e:
                    pass
                try:
                    self.spear = 0
                    self.pick.terminate()
                except Exception as e:
                    continue
            if eventos == "Iniciar":
                if valores['spear'] == True:
                    if self.spear == 1:
                        sg.popup("Mana Training já em execução, primeiro pause para poder alterar")
                    else:
                        self.spear = 1
                        self.pick = multiprocessing.Process(target=pick_spear, args=(self.baseAddress, valores, self.my_pid, self.hwnd,))
                        self.pick.start()
                try:
                    if self.mt_flag == 1:
                        sg.popup("Mana Training já em execução, primeiro pause para poder alterar")
                    else:
                        self.mt_flag = 1
                        self.mt = multiprocessing.Process(target=mana_trainer, args=(self.baseAddress, valores, self.my_pid, self.hwnd,))
                        self.mt.start()
                except Exception as e:
                    print(e)
                    continue


def list_window_names():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            ##print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')
            if win32gui.GetWindowText(hwnd).find("KST") != -1:
                win_name = win32gui.GetWindowText(hwnd)
                ctx.append(win_name)
    wins =[]
    win32gui.EnumWindows(winEnumHandler, wins)
    sg.theme('Reddit')
    layout_buttons = [
        [sg.Button('Iniciar', button_color='#fd6468')]
    ]
    layout = [
        [sg.Listbox(wins, font=('Helvetica, 12'), key='win_char', background_color='#272424', text_color='white', size=(300, 20))],
        [sg.Canvas(background_color='#272424', size=(400, 20), pad=None)],
        [sg.Column(layout=layout_buttons, justification='c', element_justification='c', background_color='#272424')]
    ]
    janela = sg.Window(f'RoseTibiaBot - KST', layout, size=(300,470),
    background_color='#272424', finalize=True, grab_anywhere=True, resizable=False)
    while True:
        eventos, valores = janela.read(timeout=100)
        if eventos ==  sg.WINDOW_CLOSED:
            sys.exit()
        if eventos == 'Iniciar':
            window_name = valores['win_char'][0]
            janela.close()
            break
    return window_name

if __name__ == "__main__":
    multiprocessing.freeze_support()
    sg.popup('Bem vindo ao RoseTibiaBot - KST', background_color='#272424',
            title='Bem vindo', button_color='#fd6468', text_color='white')
    window_name = list_window_names()
    start = bot(window_name)
    start.bot_main()