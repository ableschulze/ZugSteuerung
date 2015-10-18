# -*- coding: utf-8 -*-

import socket
import sys

#IP Adresse der Zentrale z21 in meinem Netzwerk
UDP_IP = "192.168.0.111"
#Port über den die Kommunikation stattfinden soll, siehe Schnittstelle
UDP_PORT = 21105
#Variable für die zu versendenen Nachrichten
MESSAGE = ""

print ("UDP target IP:", UDP_IP)
print ("UDP target port",UDP_PORT)
print ("messages:", MESSAGE)

#Erstellung des UDP-Sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    #Binden des Sockets zum Empfangen der Nachrichten. Der Lauscht doch nur auf dem Port?
    #Also ist die IP doch auf Localhost ok, oder :D ?
    sock.bind(('localhost',UDP_PORT))
    print ("Socket wurde an Port" , UDP_PORT, "gebunden!")
except:
    print ("ERROR - Socket ist bereits gebunden!")

print("Socket wurde erstellt!")

#Die Nachricht für den Befehl - Notaus ... ist das so richtig :D ?
#ich habe noch nie eine Netzwerk - Anwendung geschrieben, geschweige denn ein
#UDP Paket zum versenden vorbereitet ;D
MESSAGE = "\x06\x00\x40\x00\x80\x80"
print("NOTAUS wird gesendet ..." + MESSAGE);

sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

#Schließen des Sockets
sock.close()

#Wenn das klappt mach ich weiter ;)
#Die Zentrale bekommt nämlich irgendwie die Nachricht nicht ... also macht einfach nichts
#Ist das denn so weit richtig ?










#MESSAGE = "\x04\x00\x30\x00"
#print("LAN_LOGOFF");
#sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))


#Empfangen der Nachrichten die von der Zentrale versendet werden
#a = True
#while a:
#   data, addr = sock.recvfrom(1024)
#   if data != "":
#     sock.close()        
#     a = False
#     break;
#   else:
#        a = True
        
    
