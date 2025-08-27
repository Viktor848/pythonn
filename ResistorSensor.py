import serial
import sys
sys.path.append('C:/krastioMag-main/pythonTools')
import krastioMag  

portName =''
for port in serial.tools.list_ports.comports():
    print(port)
    portName = port.name

ard = krastioMag.krastioMag(port = portName)
print(ard.uv(3))

# vout = ard.uv(0)*(5.0/1023.0)
# print(vout)
# print(1000*(1/(5/(vout-1))))
# print(5/vout-1)

voltage = ard.uv(3)/1000.0
print(voltage)
# resistance = ((3.3-voltage)*1000)/voltage
resistance2 = ((1000*voltage)/(3.3-voltage))+6
# print(resistance)
print(resistance2)