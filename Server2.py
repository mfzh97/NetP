import socket
import struct
import socket, sys, time, datetime
from _thread import *
import RPi.GPIO as GPIO
import time
import hashlib


host = ''
port = 9000

## Create Socket Function
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("[SERVER]Socket Created")

## To bind Function
try:
    s.bind((host,port))
except socket.error:
    print("[SERVER]Binding Failed")
    sys.exit()

print("[SERVER]Socket has been binded")

## To listen function, 10 mean up to 10 people able to queue to handle a request
s.listen(10)

print("[SERVER]Socket Is Ready\n")


def clientthread(con):
    
    
    
    lCheck = True
    while lCheck:
         ## Define Pin on Raspberry Pi
        rPin = 27
        bPin = 22
        mPin = 17
        gPin = 23

        ## Function to turn on pin
        def turnOn(pin):
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)

        ## Function to turn off pin
        def turnOff(pin):
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW) 

        def redOn():
            turnOn(rPin)
                    
        def greenOn():
            turnOn(gPin)

        def blueOn():
            turnOn(bPin)
                    
        def mixOn():
            turnOn(mPin)

        def redOff():
            turnOff(rPin)

        def greenOff():
            turnOff(gPin)
                    
        def blueOff():
            turnOff(bPin)
                    
        def mixOff():
            turnOff(mPin)

        def blink(color, uTime):
            t_end = time.time() + int(uTime)
                    
            while time.time() < t_end:
            
                turnOn(color)
                time.sleep(0.5)
                turnOff(color)
                time.sleep(0.5) 

        def File():
            file = open('Hello.txt', 'rb')
            file_data = file.read(1024)
            con.send(file_data)
            blink(gPin,3)
            print("Data has been transmitted successfully!")

        def addition():
            
            redOn()
            statement = "[SERVER ADD] insert 1st numbers"
            con.send(bytes(statement, 'UTF8'))
            ##value = int.from_bytes(con.recv(1024),byteorder='big')
            ##num1 = int.from_bytes(value, byteorder='big')
            value = int(con.recv(1024))

            statement = "[SERVER ADD] insert 2st numbers"
            con.send(bytes(statement, 'UTF8'))
            ##value2 = int.from_bytes(con.recv(1024),byteorder='big')
            ##num2 = int.from_bytes(value2, byteorder='big')
            value2 = int(con.recv(1024))
            total = value + value2
            print(total)
            total = str(total)
            con.send(bytes(total, 'UTF8'))
            redOff()
            return total

        def subtract():
            greenOn()
            statement = "[SERVER SUBTRACT] insert 1st numbers"
            con.send(bytes(statement, 'UTF8'))
            ##value = int.from_bytes(con.recv(1024),byteorder='big')
            ##num1 = int.from_bytes(value, byteorder='big')
            value = int(con.recv(1024))

            statement = "[SERVER SUBTRACT] insert 2st numbers"
            con.send(bytes(statement, 'UTF8'))
            ##value2 = int.from_bytes(con.recv(1024),byteorder='big')
            ##num2 = int.from_bytes(value2, byteorder='big')
            value2 = int(con.recv(1024))
            total = value - value2
            print(total)
            total = str(total)
            con.send(bytes(total, 'UTF8'))
            greenOff()
            return total

        def divide():
            blueOn()
            statement = "[SERVER SUBTRACT] insert 1st numbers"
            con.send(bytes(statement, 'UTF8'))
            ##value = int.from_bytes(con.recv(1024),byteorder='big')
            ##num1 = int.from_bytes(value, byteorder='big')
            value = int(con.recv(1024))

            statement = "[SERVER SUBTRACT] insert 2st numbers"
            con.send(bytes(statement, 'UTF8'))
            ##value2 = int.from_bytes(con.recv(1024),byteorder='big')
            ##num2 = int.from_bytes(value2, byteorder='big')
            value2 = int(con.recv(1024))
            total = value / value2
            print(total)
            total = str(total)
            con.send(bytes(total, 'UTF8'))
            blueOff()
            return total         
                


        def multiply():
            blueOn()
            statement = "[SERVER SUBTRACT] insert 1st numbers"
            con.send(bytes(statement, 'UTF8'))
            ##value = int.from_bytes(con.recv(1024),byteorder='big')
            ##num1 = int.from_bytes(value, byteorder='big')
            value = int(con.recv(1024))

            statement = "[SERVER SUBTRACT] insert 2st numbers"
            con.send(bytes(statement, 'UTF8'))
            ##value2 = int.from_bytes(con.recv(1024),byteorder='big')
            ##num2 = int.from_bytes(value2, byteorder='big')
            value2 = int(con.recv(1024))
            total = value * value2
            print(total)
            total = str(total)
            con.send(bytes(total, 'UTF8'))
            blueOff()
            return total           



        data = con.recv(4096)
        if not data:
             break
            
        reply = "<Client> " + data.decode()
        print(reply)
        OpsReply = data.decode()
        Operations = "[SERVER]What would you like us to do?:"
        con.send(bytes(Operations,'UTF8'))
        OpsReply = con.recv(4056).decode('UTF8')
        print(OpsReply)

        if OpsReply == "ADD":
            addition()

        elif OpsReply == "SUBTRACT":
            subtract()

        elif OpsReply == "DIVIDE":
            divide()

        elif OpsReply == "MULTIPLY":
            multiply()
     
        elif OpsReply == "exit":
            lCheck = False
                        
        else:
            print("Invalid Command")
                    
                    
        Operations = "[SERVER]Switch on light?:"
        con.send(bytes(Operations,'UTF8'))
        OpsReply = con.recv(4056).decode('UTF8')
        print(OpsReply)
                
        if OpsReply == "raya on":
            blink(rPin, 1)
            blink(bPin, 1)
            blink(gPin, 1)
            blink(mPin, 1)
            blink(bPin, 1)
            blink(gPin, 1)
            blink(rPin, 1)
            blink(mPin, 1)
            blink(rPin, 1)
            blink(bPin, 1)
            blink(gPin, 1)
            blink(mPin, 1)
            
        elif OpsReply == "exit":
            lCheck = False    
                    
        else :
            print("Invalid Command")
                    
                    
        Operations = "[SERVER]Enter File name to receive?:"
        con.send(bytes(Operations,'UTF8'))
        OpsReply = con.recv(4056).decode('UTF8')
        print(OpsReply)
                
        if OpsReply == "":
            print("Invalid Command")
            
        elif OpsReply == "exit":
            lCheck = False    
                    
        else:
            File()            
            """" if uInput == "Add":
            print("[SERVER] ", uInput)
            con.s"""


   

## Function to save connection into file
def saveFile(addr):
    f = open("logRecord.txt", "a+")

    millis = int(round(time.time() * 1000))
    millis = str(millis)

    ## msg = "[CONNECTED] 192.168.10.3 on " + datetime.date.today().strftime("%A %d/%m/%Y") + " at " + datetime.datetime.now().strftime("%H:%M:%S:") + millis + "\n"
    msg = "[CONNECTED] " + addr[0] + ":" + str(addr[1]) + " on " + datetime.date.today().strftime("%A %d/%m/%Y") + " at " + datetime.datetime.now().strftime("%H:%M:%S:") + millis + "\n"
    f.write(msg)
    f.close

## Main function to loop the server   
while 1:
    ## To accept function
    con, addr = s.accept()
    saveFile(addr)
    print("[SERVER]Connected with " + addr[0] + ":" + str(addr[1]) + "\n")
    start_new_thread(clientthread, (con,))
    

s.close()

