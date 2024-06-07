import socket
import struct

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# address and port
server = ('oarnet', 43212)
tcp_socket.bind(server)

tcp_socket.listen(1)

# connection process
while True:
  connection, client = tcp_socket.accept()
  try:
    data = connection.recv(9)
    if data:
      operator = data[0:1].decode('utf-8')
      in1, in2 = struct.unpack('ii', data[1:9])
      try:
        if operator == '+':
          result = in1 + in2
        elif operator == '-':
          result = in1 - in2
        elif operator == '*':
          result = in1 * in2
        elif operator == '/':
          result = in1 / in2
        else: 
          raise ValueError('Error: Not an operator.')
      except Exception as e:
        result = str(e)
      connection.sendall(struct.pack('>i', int(result)))
      
  finally:
    connection.close()
