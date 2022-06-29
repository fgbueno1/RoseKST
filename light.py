from ReadWriteMemory import ReadWriteMemory
import time

base_address = '0x00003C18'
light_address = '0x14579A6C'

def light():
    rwm = ReadWriteMemory()
    process = rwm.get_process_by_name("Jornada-Tibiana_dx.exe")
    process.open()
    light = process.get_pointer(base_address, offsets=[light_address])   
    process.writeByte(light, 15)

while True:
    light()
    time.sleep(1)