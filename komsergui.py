import Tkinter as tk
import serial, time
print"================================================== "
print"contoh COM18 COM19 etc (in windows)                "
print"contoh /dev/ttyUSB0 /dev/ttyUSB1 etc(in linux)     "
print"================================================== "

porot=raw_input("Masukan port serial :")
ser=serial.Serial(porot,9600)

#kon=ser.read()
#kondisi.set(kon)

def keluar():
 global form
 form.destroy()
def lampu_on():
  ser.write('1')
  time.sleep(0.5)
  print "Lampu ON"
  
def lampu_off():
  ser.write('0')
  time.sleep(0.5)
  print "Lampu OFF"

form=tk.Tk()
form.geometry('350x100')
form.title("Pengendali lampu otomatis")

on=tk.Button(form,text="LAMPU ON",command=lampu_on)
on.pack(anchor=tk.CENTER)

off=tk.Button(form,text="LAMPU OFF",command=lampu_off)
off.pack()




#off.grid(column=1,row=1)

quit=tk.Button(form,text="KELUAR",command=keluar)
quit.pack(anchor=tk.CENTER)
tk.mainloop()
