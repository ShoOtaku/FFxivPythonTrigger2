import socketserver
import os
import sys
from FFxivPythonTrigger import PluginBase
from FFxivPythonTrigger import Logger



connection_pool = []

_logger = Logger.Logger("SocketLogger")


def broadcast_msg(msg):
    data = str(msg).encode('utf-8')
    len_data = len(data).to_bytes(4, byteorder="little",signed=True)
    for connection in connection_pool.copy():
        if connection._closed:
            connection_pool.remove(connection)
        else:
            connection.send(len_data)
            connection.send(data)


def close():
    data = (-1).to_bytes(4, byteorder="little",signed=True)
    for connection in connection_pool.copy():
        if connection._closed:
            connection_pool.remove(connection)
        else:
            connection.send(data)


class TcpServer(socketserver.BaseRequestHandler):
    def handle(self):
        _logger.info("new connection")
        if Logger.PRINT != broadcast_msg:
            _logger.debug("set logger print method")
            Logger.PRINT = broadcast_msg
        for log in Logger.print_history.copy():
            data = str(log).encode('utf-8')
            len_data = len(data).to_bytes(4, byteorder="little")
            self.request.send(len_data)
            self.request.send(data)
        connection_pool.append(self.request)
        while True:
            if not self.request.recv(1):
                break


class SocketLogger(PluginBase):
    name = "socket logger"
    git_repo = 'nyaoouo/FFxivPythonTrigger2'
    repo_path = 'plugins/SocketLogger'
    hash_path = os.path.dirname(__file__)

    def __init__(self):
        super(SocketLogger, self).__init__()
        self.server = socketserver.ThreadingTCPServer(("127.0.0.1", int(os.environ.setdefault('FptSocketPort',"3520"))), TcpServer)
        self.server.allow_reuse_address = True
        self.create_mission(self.server.serve_forever,limit_sec=0)
        self.old_std_out = None
    def _start(self):
        self.old_std_out = sys.stdout
        sys.stdout = type('',(object,),{'write':broadcast_msg})

    def _onunload(self):
        close()
        self.server.shutdown()
        self.server.server_close()
        if self.old_std_out is not None:
            sys.stdout = self.old_std_out
