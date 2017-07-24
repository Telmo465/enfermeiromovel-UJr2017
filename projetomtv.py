
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
    numero = random.randint(1, 36)
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
            numero = random.randint(1, 36)
            if numero == 1:
                num = r
            elif numero == 2:
                num = b
            elif numero == 3:
                num = p
            elif numero == 4:
                num = e
            elif numero == 5:
                num = y
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
                msg['Subject'] = Header('Problema na cama X', 'utf-8')
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
