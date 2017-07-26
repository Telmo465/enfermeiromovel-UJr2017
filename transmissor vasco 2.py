from sense_hat import SenseHat

sense_hat = SenseHat()
import socket

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
