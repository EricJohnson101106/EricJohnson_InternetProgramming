__author__ = "Eric Johnson"

# Write a Python program which let the user input a website link and a filename.
# Then the program will send an HTTP request to the server. Finally, this program
# will create a new file according to the filename and save the response from the server into that file.
#
# Sample input: www.kennesaw.edu response.txt.
#
# The result is the response will be saved into the file response.txt.

import socket

server = input("Input a website link: ")
filename = input("Input a file name: ")
file = open(filename, "a+")
path = ""

port = 80

initial_line = "GET " + path + " HTTP/1.1\r\n"
header_line = "Host: " + server + "\r\n\r\n"

sock = socket.socket()

sock.connect((server, port))

sock.sendall(initial_line.encode())
sock.sendall(header_line.encode())
sock.sendall("\n".encode())

sock.shutdown(1)

response = ""
bytes = sock.recv(2048)
while len(bytes) > 0:
    response += bytes.decode()
    bytes = sock.recv(2048)
    file.write(response)

print(response)


sock.close()
