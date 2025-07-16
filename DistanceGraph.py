import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial.tools.list_ports
import csv
import datetime
import sys
sys.path.append('C:/krastioMag-main/pythonTools')
import krastioMag  

portName =''
for port in serial.tools.list_ports.comports():
    print(port)
    portName = port.name

def animate(i, dataList1, ard):
    #timestamp = datetime.datetime.now().isoformat(sep=' ', timespec='seconds')
    arduinoData_string1 = ard.dmm()
    # try:
    arduinoData_float1 = int(arduinoData_string1)
    dataList1.append(arduinoData_float1)

    # with open("data.csv", "a", newline="") as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow([timestamp, 'Sensor 1:', arduinoData_float1,'ampers'])
    #     writer.writerow([timestamp, 'Sensor 2:', arduinoData_float2,'ampers'])

    # except:
    #     pass

    del dataList1[:-50]  # Изтриване на по-старите елементи, запазва само последните 50

    ax.clear()
    ax.plot(dataList1, label='Millimeters', color='blue')
    ax.legend()

    ax.set_ylim(-260 , 260)
    ax.set_title("Arduino Data")
    ax.set_ylabel("Value")

    for x in range(len(dataList1)):
        print('Sensor 1: ', dataList1[x])
                           # Set title of y axis 

dataList1 = []                                           # Create empty list variable for later use

fig = plt.figure()                                      # Create Matplotlib plots fig is the 'higher level' plot window

ax = fig.add_subplot(111)                               # Add subplot to main fig window

ard = krastioMag.krastioMag(port = portName)
time.sleep(2)                                           # Time delay for Arduino Serial initialization 

                                                        # Matplotlib Animation Fuction that takes takes care of real time plot.
                                                        # Note that 'fargs' parameter is where we pass in our dataList and Serial object. 
ani = animation.FuncAnimation(fig, animate, frames=100, fargs=(dataList1, ard), interval=100) 
plt.style.use('_mpl-gallery')
plt.show()                                              # Keep Matplotlib plot persistent on screen until it is closed       


 