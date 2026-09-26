import sys, os, ctypes
os.add_dll_directory('C:\\DobotStudio')
os.chdir('C:\\DobotStudio')
print('Loading DLL...')
api = ctypes.cdll.LoadLibrary('C:\\DobotStudio\\DobotDll.dll')
print('Loaded!')
