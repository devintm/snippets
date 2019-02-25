#!/usr/bin/python

# A very simple UDP client using the socket module
# https://tutorialedge.net/python/udp-client-server-python/

import socket

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789

# UDP_IP_ADDRESS = "172.104.44.199"
# UDP_PORT_NO = 6688

Message = "Hello, Server"

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))
print("Sent UDP Hello, Server message. IP:{}:{}".format(UDP_IP_ADDRESS, UDP_PORT_NO))
