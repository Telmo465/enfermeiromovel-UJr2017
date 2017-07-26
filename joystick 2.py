from sense_hat import SenseHat
import socket
sense = SenseHat()

while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)
while True:
    for event in sense.stick.get_events():
        sense.set_pixel(x, y, colours[colour])
        if event.action == 'pressed' and event.direction == 'up':
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
                    


         message()
  
        if event.action == 'pressed' and event.direction == 'down':
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
                    

 

         message()
  
        if event.action == 'pressed' and event.direction == 'right':
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
                    


         message()

        if event.action == 'pressed' and event.direction == 'left':
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
         message()
