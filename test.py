import serial
import time

ser=serial.Serial('/dev/ttyUSB0',115200)
time.sleep(5)

ser.flushInput()

def moveX(amount):
    ser.write(b'G91\n')
    command='G0 X'+str(amount)+'\n'
    ser.write(str.encode(command))
    ser.write(b'G90\n')

for i in range(0,3):
    moveX(1)
    time.sleep(1)
    moveX(-1)
    time.sleep(1)

ser.close()

