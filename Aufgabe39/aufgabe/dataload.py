'''
Created on 28.05.2015

@author: Vladimir
'''
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol

from hbase import ttypes
from hbase.Hbase import Client, Mutation

sock = TSocket.TSocket('hostname', 9090)
transport = TTransport.TBufferedTransport(sock)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = Client(protocol)
transport.open()