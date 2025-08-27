import serial
import sys
sys.path.append('C:/krastioMag-main/pythonTools')
import krastioMag  

portName =''
for port in serial.tools.list_ports.comports():
    print(port)
    portName = port.name

ard = krastioMag.krastioMag(port = portName)
while True:
    print(ard.uv(0))