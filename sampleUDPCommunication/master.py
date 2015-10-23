import socket

UDP_IP = "192.168.0.111"
UDP_PORT = 21105
SOURCE_PORT = 21105
MESSAGE = "Hello, World!"
MESSAGE_HEX = "\x06\x00\x40\x00\x80\x80"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "UDP source port:", SOURCE_PORT #muss gesetzt werden, sonst antwortet die z21 nicht

sock = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_DGRAM) # UDP
sock.bind(('0.0.0.0', SOURCE_PORT))
print "message:", MESSAGE
#sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
print "message:", MESSAGE_HEX
sock.sendto(MESSAGE_HEX, (UDP_IP, UDP_PORT))
sock.close()
