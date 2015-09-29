#tkinter for Python 3.x
#Tkinter for Python 2.x
 
import serial
import time
import Tkinter as tkinter
 
def quit():
    global tkTop
    tkTop.destroy()
 
def setCheckButtonText():
    if varCheckButton.get():
        varLabel.set("LED ON")
        ser.write('HIGH')
    else:
        varLabel.set("LED OFF")
        ser.write('LOW')
 
ser = serial.Serial('COM18', 9600,timeout=0)
print("Reset Arduino")
time.sleep(3)
ser.write('LOW')
 
tkTop = tkinter.Tk()
tkTop.geometry('300x200')
 
varLabel = tkinter.StringVar()
tkLabel = tkinter.Label(textvariable=varLabel)
tkLabel.pack()
 
varCheckButton = tkinter.IntVar()
tkCheckButton = tkinter.Checkbutton(
    tkTop,
    text="Control Arduino LED",
    variable=varCheckButton,
    command=setCheckButtonText)
tkCheckButton.pack(anchor=tkinter.CENTER)
 
tkButtonQuit = tkinter.Button(
    tkTop,
    text="Quit",
    command=quit)
tkButtonQuit.pack()
 
tkinter.mainloop()