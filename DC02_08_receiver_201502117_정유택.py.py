import socket
from time import sleep

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(('', 9000))

recv_file_name, addr = socket.recvfrom(2000)
file_name = recv_file_name.decode()
sleep(0.1)

recv_size, _ = socket.recvfrom(2000)
total_size = int(recv_size)

print('file recv start from', addr[0])
print('File Name :', file_name)
print('File size :', total_size)

with open(file_name, 'w') as recv_file:
    current_size = 0
    while current_size != total_size:
        current_size = current_size + 1024
        if current_size > total_size:
            current_size = total_size
        divided_file, _ = socket.recvfrom(1024)
        divided_file = str(divided_file.decode())
        recv_file.write(divided_file)
        percent = str((current_size / total_size) * 100) + '%'
        print('current_size / total_size =', current_size, '/', total_size, ',', percent)
