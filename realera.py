from ReadWriteMemory import ReadWriteMemory
from PySimpleGUI import PySimpleGUI as sg
from pynput.keyboard import Key, Controller
import psutil
import win32api, win32process
import sys
import time

class autopot:
    def __init__(self):
        self.game = "RealeraDX9.exe"
        self.keyboard = Controller()
        self.rwm = ReadWriteMemory()
        try:
            self.process = self.rwm.get_process_by_name(self.game)
            self.process.open()
            my_pid = None
            pids = psutil.pids()
            for pid in pids:
                ps = psutil.Process(pid)
                if self.game in ps.name():
                    my_pid = ps.pid
            PROCESS_ALL_ACCESS = 0x1F0FFF
            processHandle = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, my_pid)
            modules = win32process.EnumProcessModules(processHandle)
            processHandle.close()
            base_addr = modules[0]
            self.baseAddress = base_addr + 0x004939F8
            ## POS X = 0x00A7403C
            '''pos_x = self.process.get_pointer(0x00A7403C)
            pos_x = self.process.read(pos_x)
            print(pos_x)
            ## POS Y = 0x00A74040
            pos_y = self.process.get_pointer(0x00A74040)
            pos_y = self.process.read(pos_y)
            print(pos_y)
            ## POS Z = 0x00A74044
            pos_z = self.process.get_pointer(0x00A74044)
            pos_z = self.process.read(pos_z)
            print(pos_z)
            wanna_walk = [32369, 32234, 7]
            if pos_x > wanna_walk[0]:
                walk = pos_x - wanna_walk[0]
                self.key = Key.left
                for i in range(walk):
                    self.keystroke()  
            elif pos_x < wanna_walk[0]:
                walk = wanna_walk[0] - pos_x
                self.key = Key.right
                for i in range(walk):
                    self.keystroke()
            if pos_y > wanna_walk[1]:
                walk = pos_y - wanna_walk[1]
                self.key = Key.up
                for i in range(walk):
                    self.keystroke()  
            elif pos_y < wanna_walk[1]:
                walk = wanna_walk[1] - pos_y
                self.key = Key.down
                for i in range(walk):
                    self.keystroke() ''' 

        except:
            sg.theme('Reddit')
            sg.popup('Por favor inicie o jogo antes de abrir o RoseTibiaBot - Realera', background_color='#272424',
            title='Erro ao Iniciar', button_color='#fd6468', text_color='white')
            sys.exit()
    
    def keystroke(self):
        if self.key == 'F1':
            self.key = Key.f1
        elif self.key == 'F2':
            self.key = Key.f2
        elif self.key == 'F3':
            self.key = Key.f3
        elif self.key == 'F4':
            self.key = Key.f4
        elif self.key == 'F5':
            self.key = Key.f5
        elif self.key == 'F6':
            self.key = Key.f6
        elif self.key == 'F7':
            self.key = Key.f7
        elif self.key == 'F8':
            self.key = Key.f8
        elif self.key == 'F9':
            self.key = Key.f9
        elif self.key == 'F10':
            self.key = Key.f10
        elif self.key == 'F11':
            self.key = Key.f11
        elif self.key == 'F12':
            self.key = Key.f12
        self.keyboard.press(self.key)
        self.keyboard.release(self.key)

    def bot_main(self):
        sg.theme('Reddit')
        char_name = self.process.get_pointer(self.baseAddress, offsets=[0x20])
        self.char_name = self.process.readString(char_name, 30)
        layout_title = [
            [sg.Text(f'RoseTibiaBot-Realera -- logged as {self.char_name}',font=('Helvetica, 10'), justification='c', background_color='#272424', text_color='white')]
        ]
        layout_buttons = [
            [sg.Button('Healing', button_color='#fd6468'), sg.Button('Cavebot', button_color='#fd6468'),
            sg.Button('Mana Trainer', button_color='#fd6468'), sg.Button('Exit', button_color='#fd6468')]
        ]
        layout = [
            [sg.Canvas(background_color='#272424', size=(400, 10), pad=None)],
            [sg.Column(layout=layout_title, justification='c', element_justification='c', background_color='#272424')],
            [sg.Canvas(background_color='#272424', size=(400, 3), pad=None)],
            [sg.Column(layout=layout_buttons, justification='c', element_justification='c', background_color='#272424')]
        ]
        janela = sg.Window(f'RoseTibiaBot - Realera -- logged as {self.char_name}', layout, size=(300,100),
        background_color='#272424', finalize=True, grab_anywhere=True, resizable=False)
        while True:
            eventos, valores = janela.read(timeout=100)
            if eventos == sg.WINDOW_CLOSED:
                break
            if eventos == "Exit":
                janela.close()
                break
            if eventos == "Healing":
                self.healing()
            if eventos == "Cavebot":
                self.cavebot()

    def cavebot(self):
        sg.theme('Reddit')
        layout_hp = [
            [sg.Text('Waypoints',font=('Helvetica, 14'), justification='c', background_color='#272424', text_color='white')]
        ]
        layout_buttons = [
            [sg.Button('Iniciar', button_color='#fd6468'), sg.Button('Pausar', button_color='#fd6468')]
        ]
        layout = [
            [sg.Canvas(background_color='#272424', size=(400, 10), pad=None)],
            [sg.Column(layout=layout_hp, justification='c', element_justification='c', background_color='#272424')],
            [sg.Canvas(background_color='#272424', size=(400, 3), pad=None)],
            [sg.Checkbox('HP', default=False,key='hp', background_color='#272424', text_color='white'),
            sg.Combo(['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12'],default_value='',key='hp_key',readonly=True, background_color='#272424', text_color='white'),
            sg.Text("HP to Heal: ", background_color='#272424', text_color='white'),sg.Input(key='hp_value', background_color='#272424', text_color='white'), ],
            [sg.Checkbox('MP', default=False,key='mp', background_color='#272424', text_color='white'),
            sg.Combo(['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12'],default_value='',key='mp_key',readonly=True, background_color='#272424', text_color='white'),
            sg.Text("MP to Heal: ", background_color='#272424', text_color='white'),sg.Input(key='mp_value', background_color='#272424', text_color='white'), ],
            [sg.Canvas(background_color='#272424', size=(400, 20), pad=None)],
            [sg.Column(layout=layout_buttons, justification='c', element_justification='c', background_color='#272424')]
        ]
        janela = sg.Window('RoseTibiaBot - Realera', layout, size=(400,300),
        background_color='#272424', finalize=True, grab_anywhere=True, resizable=False)
        init = 0
        while True:
            eventos, valores = janela.read(timeout=100)
            

    def healing(self):
        sg.theme('Reddit')
        layout_hp = [
            [sg.Text('Auto Pot',font=('Helvetica, 14'), justification='c', background_color='#272424', text_color='white')]
        ]
        layout_buttons = [
            [sg.Button('Iniciar', button_color='#fd6468'), sg.Button('Pausar', button_color='#fd6468')]
        ]
        layout = [
            [sg.Canvas(background_color='#272424', size=(400, 10), pad=None)],
            [sg.Column(layout=layout_hp, justification='c', element_justification='c', background_color='#272424')],
            [sg.Canvas(background_color='#272424', size=(400, 3), pad=None)],
            [sg.Checkbox('HP', default=False,key='hp', background_color='#272424', text_color='white'),
            sg.Combo(['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12'],default_value='',key='hp_key',readonly=True, background_color='#272424', text_color='white'),
            sg.Text("HP to Heal: ", background_color='#272424', text_color='white'),sg.Input(key='hp_value', background_color='#272424', text_color='white'), ],
            [sg.Checkbox('MP', default=False,key='mp', background_color='#272424', text_color='white'),
            sg.Combo(['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12'],default_value='',key='mp_key',readonly=True, background_color='#272424', text_color='white'),
            sg.Text("MP to Heal: ", background_color='#272424', text_color='white'),sg.Input(key='mp_value', background_color='#272424', text_color='white'), ],
            [sg.Canvas(background_color='#272424', size=(400, 20), pad=None)],
            [sg.Column(layout=layout_buttons, justification='c', element_justification='c', background_color='#272424')]
        ]
        janela = sg.Window(f'RoseTibiaBot - Realera -- logged as {self.char_name}', layout, size=(400,300),
        background_color='#272424', finalize=True, grab_anywhere=True, resizable=False)
        init = 0
        while True:
            eventos, valores = janela.read(timeout=100)
            if eventos ==  sg.WINDOW_CLOSED:
                break
            if eventos == 'Pausar':
                init = 0
            if init == 1:
                eventos = "Iniciar"
            if eventos == "Iniciar":
                ##self.healer(init, valores)
                init = 1
                if valores['hp'] == True:
                    try:
                        self.key = valores['hp_key']
                        hp = self.process.get_pointer(self.baseAddress, offsets=[0x3B0])
                        hp = self.process.readDouble(hp)
                        heal_hp = valores['hp_value']
                        if int(hp) < int(heal_hp):
                            self.keystroke()
                            time.sleep(0.5)
                    except:
                        continue
                if valores['mp'] == True:
                    try:
                        self.key = valores['mp_key']
                        mana = self.process.get_pointer(self.baseAddress, offsets=[0x3E8])
                        mana = self.process.readDouble(mana)
                        heal_mana = valores['mp_value']
                        if int(mana) < int(heal_mana):
                            self.keystroke()
                    except:
                        continue

    def healer(self, init, valores):
        if init == 1:
            while True:
                if valores['hp'] == True:
                    try:
                        self.key = valores['hp_key']
                        hp = self.process.get_pointer(self.baseAddress, offsets=[0x3B0])
                        hp = self.process.readDouble(hp)
                        heal_hp = valores['hp_value']
                        if int(hp) < int(heal_hp):
                            self.keystroke()
                            time.sleep(0.5)
                    except:
                        continue
                if valores['mp'] == True:
                    try:
                        self.key = valores['mp_key']
                        mana = self.process.get_pointer(self.baseAddress, offsets=[0x3E8])
                        mana = self.process.readDouble(mana)
                        heal_mana = valores['mp_value']
                        if int(mana) < int(heal_mana):
                            self.keystroke()
                    except:
                        continue

if __name__ == "__main__":
    start = autopot()
    start.bot_main()