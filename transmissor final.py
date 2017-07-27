import socket

from smtplib import SMTP_SSL
from sense_hat import SenseHat

sense_hat = SenseHat()


#função so pode ser "recetor" ou "transmissor"
funcao = "recetor"

#comunicação com o meu dispositivo
UDP_IP_Meu = "10.250.4.123"
UDP_Port_Meu = 8000

#comunicação com outro dispositivo
UDP_IP_OD = "10.250.3.103"
UDP_Port_OD = 8000

#recetor reforços
def Message(message):
    Message = mensagem
    bytesMessage = bytes(Message, 'UTF-8')

    print("UDP target IP: ", UDP_IP_OD)
    print("UDP target port: ", UDP_Port_OD)
    print("message: ", Message)

    sock = socket.socket(socket.AF_INET, # Internet
    socket.SOCK_DGRAM) # UDP
    sock.sendto(bytesMessage, (UDP_IP_OD, UDP_Port_OD))

if funcao == "recetor":
    #recetor de reforcos
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.socket.SOL_S0CKET, socket.socket.SO_REUSEADDR, 1)
    sock.bind((UDP_IP_Meu, UDP_Port_Meu))
    while True:
        data, addr = sock.recvfrom(1024)
        dat = data.decode("UTF-8")
        print(data)

elif funcao == "transmissor":
    while True:
        for event in sense.stick.get_events():
            print(event.direction, event.action)
            if event.action == 'pressed':
                Message("Reforços")
        
                         
