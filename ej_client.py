__author__ = "Eric Johnson"

# From D2L Socket Practice 1 and 2
# Updating from simple_client.py (D2L)
# To allow a user to input values to be calculated by the server

import socket

# 1. create a socket
sock = socket.socket()
# 2. Make a connection to the server - 127.0.0.1 is localhost. Server file has blank address which is localhost
sock.connect(('127.0.0.1', 12345))

#  - Create a request message and encode it:
# request = "Hi there, I would like to make a connection"
# request_byte = request.encode()

# 3. Send a request to the server
# 3.1 make a request

# Asking the user for inputs.
a = input("Input E or S promptly followed by the x value (E1.0 or S0)")
b = input("If a bisection, input the second x value (b)")
#  If b is not empty, it will put  a space between a and b
if b != '':
    b = " " + b

poly = input("Input the values of your polynomial from the lowest X variable to the highest (-945 1689 -950 230 -25 1)")
# If poly is not empty, it will put a space between the prior input and poly
if poly != '':
    poly = " " + poly
tol = input("If a bisection, input the value of your tolerance (greater than 0)")
# If tol is not empty, it will put a space between poly and tol
if tol != '':
    tol = " " + tol

request = str(a) + str(b) + str(poly) + str(tol)
print("Sending Request: " + request)
request_byte = request.encode()

# - The encode() function covert a string to a byte, making a transferable data for the socket.
# Let’s send the request message:
# 3.2 send the request
sock.sendall(request_byte)
sock.shutdown(1)

# - shutdown(1) does not mean that we want to close the socket. It just sends a signal to
# notify the server that we sent all request messages and now wait for the response.
# - The following code can be used to receive a response from the server:
# 4. receive a response from the server
bytes = sock.recv(2048)
response = ""
while len(bytes) > 0:
    response = bytes.decode()
    bytes = sock.recv(2048)
print("Received Response: " + response)

# - Finally, we should close the created socket:
# 5. close the socket
sock.close()
