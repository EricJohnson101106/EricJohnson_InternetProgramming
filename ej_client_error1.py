__author__ = "Eric Johnson"

# From D2L Socket Practice 1 and 2
# Updating from simple_client.py (D2L)

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


request = "G4.1 0 0"
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
