Python 3.4.2 (default, Oct 19 2014, 13:31:11) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import time
import random
import os
from sense_hat import SenseHat
def geradoraleatorio():
    numero = random.randint(1, 5)
    if numero == 1:
        os.system('mpg123 musicas/Mega\ Alarm.mp3')
        time.sleep(0.5)
    elif numero == 2:
        os.system('mpg123 musicas/Trumpet\ Military\ Wake\ Up.mp3')
        time.sleep(0.5)
    elif numero == 3:
        os.system('mpg123 musicas/Alarm\ Clock.mp3')
        time.sleep(0.5)
    elif numero == 4:
        os.system('mpg123 musicas/Samsung\ Galaxy\ S6\ Alarm.mp3')
        time.sleep(0.5)
    else
        os.system('mpg123 musicas/Alarm\ v1.mp3')
        time.sleep(0.5)
        
geradoraleatorio()
