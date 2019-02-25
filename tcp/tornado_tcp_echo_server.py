#!/usr/bin/python

# Prerequisites: tornado
#   $ pip install tornado

from tornado.tcpserver import TCPServer
from tornado.ioloop import IOLoop
from tornado.iostream import StreamClosedError
from tornado import gen


class EchoServer(TCPServer):
    @gen.coroutine
    def handle_stream(self, stream, address):
        while True:
            try:
                data = yield stream.read_until(b"\n")
                yield stream.write(data)
            except StreamClosedError:
                break


if __name__ == '__main__':
    server = EchoServer()
    server.listen(62200)
    IOLoop.instance().start()
