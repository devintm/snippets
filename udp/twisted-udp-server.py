#!/usr/bin/python

# Prerequisites: twisted
#   $ pip install twisted

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class Helloer(DatagramProtocol):

    def startProtocol(self):
        print "starting the twisted UDP server...\n\n"
        host = "localhost"
        port = 6789

        # self.transport.connect(host, port)
        print "now we can only send to host %s port %d" % (host, port)
        # self.transport.write("hello")  # no need for address

    def datagramReceived(self, data, (host, port)):
        print "received %r from %s:%d" % (data, host, port)

    # Possibly invoked if there is no server listening on the
    # address to which we are sending.
    def connectionRefused(self):
        print "No one listening"


# 0 means any port, we don't care in this case
# reactor.listenUDP(0, Helloer())
reactor.listenUDP(6789, Helloer())
reactor.run()
