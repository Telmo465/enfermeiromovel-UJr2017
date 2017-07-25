from sense_hat import SenseHat

sense_hat = SenseHat()
import socket

#recetor reforços
UDP_IP = "10.250.4.123"
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

UDP_IP = "10.250.4.123"
UDP_Port = 8000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet UDP              
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((UDP_IP, UDP_Port))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data = data.decode("UTF-8")
    print (data)

UDP_IP = "10.250.4.123"
UDP_Port = 8000
#transmissor de reforços
while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)
while True:
    for event in sense.stick.get_events():
        sense.set_pixel(x, y, colours[colour])
        if event.action == 'pressed':
         UDP_IP = "10.250.4.123"
         UDP_Port = 8000

         def message(): 
           Message = "reforços"
           bytesMessage = bytes(Message, 'UTF-8')

           print ("UDP target IP:"), UDP_IP
           print ("UDP target port:"), UDP_Port
           #print ("message:"), MESSAGE

           sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
           sock.sendto(bytesMessage, ("10.250.3.103", UDP_Port))
                    
                    


