import socket
import struct

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# address and port
server = ('oarnet', 43212)
tcp_socket.connect(server)

try:
  setinput = b '+' + struct.pack('>ii', 7, 3)
  tcp_socket.sendall(setinput)
  
  data = tcp_socket.recv(4)
  if data:
    result = struct.unpack('>i', data)[0]
    print('Woah! Look what I got here: {!r}'.format(result))
except Exception as e:
  print(f"Uh oh, got an error: {e}")
finally:
  tcp_socket.close()
