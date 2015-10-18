import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Hello, World!"
MESSAGE_HEX = "\x06\x00\x40\x00\x80\x80"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

sock = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_DGRAM) # UDP

print "message:", MESSAGE
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
print "message:", MESSAGE_HEX
sock.sendto(MESSAGE_HEX, (UDP_IP, UDP_PORT))
