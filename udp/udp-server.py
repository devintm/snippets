#!/usr/bin/python

# Again we import the necessary socket python module
import socket

# Here we define the UDP IP address as well as the port number that we have
# already defined in the client python script.
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789

# UDP_IP_ADDRESS = "172.104.44.199"
# UDP_PORT_NO = 6688

# declare our serverSocket upon which
# we will be listening for UDP messages
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


# One difference is that we will have to bind our declared IP address
# and port number to our newly declared serverSock
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

print("Started UDP server. Listening on IP:{}:{}".format(UDP_IP_ADDRESS, UDP_PORT_NO))
while True:
    data, addr = serverSock.recvfrom(2048)
    print "Message: ", data
    d = data.encode('hex').upper()
    print "HEX: ", d
