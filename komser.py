#komunikasi serial python
#creat for controling arduino 
#in this arduino connect to port 
#create 27/08/2015 20:38


import serial, time 
print"================================================== "
print"contoh COM18 COM19 etc (in windows)                "
print"contoh /dev/ttyUSB0 /dev/ttyUSB1 etc(in linux)     "
print"================================================== "


port=raw_input("Masukan port serial : ")

ser=serial.Serial(port,9600,timeout=0)
time.sleep(1)    
#true=bool
#while true:
a=raw_input("Enter command :")
if a=="1":
        ser.write(a)
        time.sleep(1)
        print"Lampu nyala"
elif a=="0" :
        ser.write(a)
        time.sleep(1)
        print"lampu mati"       
elif a=="exit" or a=="keluar":
        exit()
else:
        ser.write(a)
        print"Kata perintah tidak di temukan"