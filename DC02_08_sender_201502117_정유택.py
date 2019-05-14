import socket
import os
from time import sleep


recv_ip = '192.168.219.104'
# client IP address

recv_port = 9000
# client port number


file_name = input('Input your file name : ')
# input file name to send

total_size = os.path.getsize(file_name)
# file_size is size of file which is going to send, result is byte

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket.sendto(file_name.encode(), (recv_ip, int(recv_port)))
sleep(0.5)

send_size = str(total_size)
socket.sendto(send_size.encode(), (recv_ip, int(recv_port)))


with open(file_name, 'rb') as send_file:
    if total_size == 0:
        print('File size is ZERO')
        print('Please try again with another file')
    else:
        print('File Transmit Start....')
        current_size = 0
        while current_size != total_size:
            current_size = current_size + 1024
            if current_size > total_size:
                current_size = total_size
            divided_file = send_file.read(1024)
            socket.sendto(divided_file, (recv_ip, int(recv_port)))
            percent = str((current_size / total_size) * 100) + '%'
            print('current_size / total_size =', current_size, '/', total_size, ',', percent)

