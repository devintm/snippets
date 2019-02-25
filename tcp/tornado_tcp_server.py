#!/usr/bin/python

# Prerequisites: tornado
#   $ pip install tornado

# import logging

from tornado.ioloop import IOLoop
from tornado.tcpserver import TCPServer

# https://stackoverflow.com/questions/37800585/how-to-store-tornado-logs-to-a-file
# https://stackoverflow.com/questions/12593460/where-can-i-check-tornados-log-file

# Notes / placeholders for setting up Tornado log files
# access_log = logging.getLogger("tornado.access")
# app_log = logging.getLogger("tornado.application")
# gen_log = logging.getLogger("tornado.general")

# access_log_handler = logging.FileHandler(log_file_filename)
# app_log = logging.getLogger("tornado.application")
# enable_pretty_logging()
# app_log.addHandler(handler)


class MyTCPServer(TCPServer):
    def handle_stream(self, stream, address):
        def got_data(data):
            print "Input: {}".format(repr(data))
            stream.write("OK", stream.close)

        stream.read_until("\n", got_data)
        # stream.read_until("#", got_data)


if __name__ == '__main__':
    server = MyTCPServer()
    server.listen(62200)
    IOLoop.instance().start()
