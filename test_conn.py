import sys, os, ctypes
from ctypes import create_string_buffer
os.add_dll_directory('C:\\DobotStudio')
os.chdir('C:\\DobotStudio')
api = ctypes.cdll.LoadLibrary('DobotDll.dll')

port = create_string_buffer(100)
port.value = b'COM13'
fw = create_string_buffer(100)
ver = create_string_buffer(100)

print('Connecting...')
res = api.ConnectDobot(port, 115200, fw, ver)
print(f'Result: {res}')
