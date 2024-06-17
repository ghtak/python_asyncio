import socket
import struct

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(('localhost', 17543))  # 서버에 접속
    data = 'hi'.encode()
    header = struct.pack('>iii', 1, len(data), 1)
    client_socket.send(header+data)  # 서버에 메시지 전송
    msg = client_socket.recv(len(data))  # 서버로부터 응답받은 메시지 반환
    print(f"resp from server : {msg.decode()}")  # 서버로부터 응답받은 메시지 출력