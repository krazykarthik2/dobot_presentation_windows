import pydobot
from serial.tools import list_ports
import time
import struct
from pydobot.message import Message

def main():
    ports = list_ports.comports()
    if not ports:
        print("No ports found")
        return
        
    p = ports[0].device
    print(f"Connecting to {p}...")
    device = pydobot.Dobot(port=p, verbose=False)

    print("Re-initializing execution queue in correct order...")
    # Fix pydobot's broken initialization order (Clear THEN Start)
    msg_clear = Message()
    msg_clear.id = 245
    msg_clear.ctrl = 0x01
    device._send_command(msg_clear)
    time.sleep(0.1)
    
    msg_start = Message()
    msg_start.id = 240
    msg_start.ctrl = 0x01
    device._send_command(msg_start)
    time.sleep(0.1)

    print("Clearing software alarms...")
    msg_alarm = Message()
    msg_alarm.id = 20
    msg_alarm.ctrl = 0x01
    msg_alarm.params = bytearray()
    device._send_command(msg_alarm)
    time.sleep(0.5)

    print("Setting JOG limits...")
    msg = Message()
    msg.id = 71
    msg.ctrl = 0x03 # Must be Queued
    msg.params = bytearray(struct.pack('ff', 100.0, 100.0))
    device._send_command(msg)

    msg = Message()
    msg.id = 70
    msg.ctrl = 0x03 # Must be Queued
    msg.params = bytearray(struct.pack('8f', 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0))
    device._send_command(msg)

    print("--- FORCING NATIVE PTP MOVEMENT ---")
    x, y, z, r, j1, j2, j3, j4 = device.pose()
    print(f"Current Z: {z}")
    
    # Try native PTP using pydobot
    print("Moving Z up by 20mm...")
    device.move_to(x, y, z + 20, r, wait=True)
    
    print("--- FORCING JOG MOVEMENT ---")
    print("Sending Joint 3 (Forearm) JOG Positive command for 1.5 seconds...")
    for _ in range(15):
        msg = Message()
        msg.id = 73
        msg.ctrl = 0x01 # Write Immediate
        msg.params = bytearray([1, 5]) # 1=Joint, 5=Joint3 Positive
        device._send_command(msg)
        time.sleep(0.1)

    print("Stopping motors...")
    msg = Message()
    msg.id = 73
    msg.ctrl = 0x01
    msg.params = bytearray([1, 0]) # Idle
    device._send_command(msg)
    
    print("Done!")
    device.close()

if __name__ == "__main__":
    main()
