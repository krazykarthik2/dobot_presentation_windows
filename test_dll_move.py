import sys, os, time
def log(s):
    with open(r'C:\Users\karthikkrazy\Downloads\dobot_joystick\StarterGuide-Dobot-Magician-with-Python\Python Example Files\move.log', 'a') as f:
        f.write(s + '\n')

log('Starting...')
os.add_dll_directory('C:\\DobotStudio')
os.chdir('C:\\DobotStudio')
sys.path.insert(0, r'C:\Users\karthikkrazy\Downloads\dobot_joystick\StarterGuide-Dobot-Magician-with-Python\Python Example Files')
import DobotDllType as dType

log('Loading DLL...')
api = dType.load()
log('Connecting...')
res = dType.ConnectDobot(api, 'COM13', 115200)
log(f'Connected: {res[0]}')

log('Clearing Queue...')
dType.SetQueuedCmdClear(api)
log('Starting Queue...')
dType.SetQueuedCmdStartExec(api)

log('Setting JOG Common Params...')
dType.SetJOGCommonParams(api, 100, 100, isQueued=1)
log('Setting JOG Joint Params...')
dType.SetJOGJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued=1)

log('Moving...')
dType.SetJOGCmd(api, 1, 1, isQueued=0)
time.sleep(2)
dType.SetJOGCmd(api, 1, 0, isQueued=0)

log('Disconnecting...')
dType.DisconnectDobot(api)
log('Done!')
