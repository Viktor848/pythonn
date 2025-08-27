import serial.tools.list_ports
import time
import sys
sys.path.append('C:/Users/ltp-l/Desktop/magnet/km/krastioMag-main/pythonTools')
import krastioMag  


portName =''
for port in serial.tools.list_ports.comports():
    print(port)
    portName = port.name

ard = krastioMag.krastioMag(port = portName)
while True:
    #print(ard.uv(0))
    
    #print(ard.aread(0, "volts"))
    #print(ard.aread(0, "ampers"))
    print(ard.aread(0, "ampers2"))
    print() 
    time.sleep(3)