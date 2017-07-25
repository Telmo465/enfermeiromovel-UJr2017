from sense_hat import SenseHat

sense_hat = SenseHat()
import socket

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

message()
