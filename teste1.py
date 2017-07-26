import socket 
import string
import time
import random
import os
import sys

from smtplib import SMTP_SSL
from email.header import Header
from email import encoders
from email.mime.text import MIMEText
from sense_hat import SenseHat

sense = SenseHat()

r = (255, 0, 0) #Febre
b = (0, 0, 255) #Hipotermia
g = (0, 255, 0) #Normalizado
e = (0, 0, 0) #Paragem Cardiaca
y = (255, 255, 0) #Hipertensão
p = (160, 32, 240) #Hipotensão
o = (255, 255, 255)#Borda

def geradoraleatorio():
    numero = random.randint(1, 60)
    r = (255, 0, 0) #Febre
    b = (0, 0, 255) #Hipotermia
    g = (0, 255, 0) #Normalizado
    e = (0, 0, 0) #Paragem Cardiaca
    y = (255, 255, 0) #Hipertensão
    p = (160, 32, 240) #Hipotensão
    o = (255, 255, 255)#Borda
    
    image = [o,o,o,o,o,o,o,o]
    for x in range(6):
        image1 = [o,]
        for z in range(6):
            numero = random.randint(1, 60)
            if numero == 1:
                num = r
                os.system('mpg123 musicas/Mega\ Alarm.mp3')
                time.sleep(0.5)
                print(1)
            elif numero == 2:
                num = b
                os.system('mpg123 musicas/Trumpet\ Military\ Wake\ Up.mp3')
                time.sleep(0.5)
                print(2)
            elif numero == 3:
                num = p
                os.system('mpg123 musicas/Alarm\ Clock.mp3')
                time.sleep(0.5)
                print(3)
            elif numero == 4:
                num = e
                os.system('mpg123 musicas/Samsung\ Galaxy\ S6\ Alarm.mp3')
                time.sleep(0.5)
                print(4)
            elif numero == 5:
                num = y
                os.system('mpg123 musicas/Alarm\ v1.mp3')
                time.sleep(0.5)
                print(5)
            else:
                num = g
            image1.append( num );
            if num != g:
                login, password = 'projetoujunior@gmail.com', 'supersenha2017'
                recipients = [login]
                message = """Problema """
                if num == r:
                    num = 'Febre'
                if num == b:
                    num = 'Hipotermia'
                if num == p:
                    num = 'Hipotensão'
                if num == e:
                    num = 'Paragem Cardiaca'
                if num == y:
                    num = 'Hipertensão'
                message += num
                msg = MIMEText(message, 'plain', 'utf-8')
                msg['Subject'] = Header('Problema na cama' + str(x*6+z+1),  'utf-8')
                msg['From'] = 'My rpi <projetoujunior@gmail.com>'
                msg['To'] = 'projetoujunior@gmail.com'
                s = SMTP_SSL('smtp.gmail.com', 465, timeout=10)
                s.set_debuglevel(1)
                try:
                    s.login(login, 'supersenha2017')
                    s.sendmail(msg['From'], recipients, msg.as_string())
                finally:
                    s.quit()

        image1.append( o )
        image.extend(image1)
    image2 = [o,o,o,o,o,o,o,o]
    image.extend(image2)
    print(len(image), image)
    sense.set_pixels(image)
        
   
geradoraleatorio()

UDP_IP = "10.250.3.103"
UDP_Port = 8000
Message = "reforços"

def Message():
    Message = "reforços"
    print ("UDP target IP:"), UDP_IP
    print ("UDP target port:"), UDP_Port
    print ("message:"), MESSAGE
    sock = socket.socket(socket.AF_INET, # Internet
    socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_Port))

UDP_IP = "10.250.3.103"
UDP_Port = 8000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet UDP              
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((UDP_IP, UDP_Port))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data = data.decode("UTF-8")
    print (data)
 
