#!/usr/bin/python

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 62200)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    print("Starting Simple TCP Client...\n\n")
    # Send data
    # message = "Test Message,Hello World,Element#3,param:value#"
    message = "Test Message,Hello World,Element#3,param:value\n"
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    # amount_expected = len(message)
    amount_expected = 2

    while amount_received < amount_expected:
        # The ammount of characters to receive, the same length as the 'message'
        # variable
        data = sock.recv(47)
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
