__author__ = "Eric Johnson"

# From D2L Socket Practice 1 and 2
# Updating from simple_socket.py (D2L)

import socket
import logging
from polynomials import evaluate, bisection

logging.basicConfig(level=logging.ERROR)

# Binom function from example
# def binom(n, m):
#     b = 1
#     for i in range(0, m):
#         b = b * (n - i) // (i + 1)
#     return b


port = 12345
# 1. create a socket
listener = socket.socket()
# 2. bind the socket with IP address and port number
listener.bind(('', port))
# 3. generate a listener
listener.listen(0)
# 4. wait for a connection request
# 4.1 making a connection
while True:
    (sock, address) = listener.accept()
    print(address)
    logging.info("Connection established with" + str(address))
    logging.error("connection failed with " + str(address))  # throwing an error TODO

    # 4.2 getting data from the client
    # Be aware of indentation: all the code must be located inside the while loop
    # right below the “print(address)” statement.
    bytes = sock.recv(2048)
    client_data = ""
    while len(bytes) > 0:
        client_data += bytes.decode()  # UTF-8
        bytes = sock.recv(2048)

    # 4.3 parse the data from the client
    print(client_data)
    list_of_parts = client_data.split(" ")
    # "12 6" => ["12","6"]
    # "12  6" => ["12", "", "6"]
    # "twelve six" => ["twelve", "six"]
    print("Printing the list of parts before converting")
    print(list_of_parts)

    try:
        if client_data[0] == "E":
            if len(list_of_parts) < 2:
                raise Exception("Too few arguments")  # Caught if there aren't enough arguments

            # If we are sending an polynomials.evaluate request, it will start with E
            # followed by the value of x
            # i.e. E1.0 is evaluate given polynomial where 1.0 is the value of x
            for i in range(1, len(list_of_parts)):
                list_of_parts[i] = int(list_of_parts[i])

            print("Printing the list of parts after converting")
            print(list_of_parts)
            print("xval is: " + list_of_parts[0][1:] +
                  " poly is: " + str(list_of_parts[1:]))

            result = evaluate(float(list_of_parts[0][1:]), list_of_parts[1:])
            print("result " + str(result))
            response_status = 'E'
            response_message = str(result)
        elif client_data[0] == "S":
            if len(list_of_parts) < 4:
                raise Exception("Too few arguments")  # Caught if there aren't enough arguments

            if float(list_of_parts[len(list_of_parts) - 1]) < 0:
                raise Exception("Invalid tolerance")  # According to polynomials.py, tolerances should be greater than 0

            elif float(list_of_parts[len(list_of_parts) - 1]) == 0:
                raise Exception("Invalid tolerance")  # Tolerance can't be 0 for some reason

            for i in range(2, len(list_of_parts) - 1):
                list_of_parts[i] = int(list_of_parts[i])

            print("Printing the list of parts after converting")
            print(list_of_parts)
            print("aval is: " + str(list_of_parts[0][1:]) +
                  " bval is: " + str(list_of_parts[1]) +
                  " tol is: " + str(list_of_parts[len(list_of_parts) - 1]))

            result = bisection(float(list_of_parts[0][1:]), float(list_of_parts[1]),
                               list_of_parts[2:len(list_of_parts) - 1],
                               float(list_of_parts[len(list_of_parts) - 1]))
            print("result " + str(result))
            response_status = 'S'
            response_message = str(result)
        else:
            raise Exception("Incorrect command type")  # Caught if the first character from client is not E or S

    except Exception as ex:
        # signal a conversion problem or computation problem
        # error response
        response_status = 'X'
        response_message = str(ex)

    response = response_status + response_message
    logging.error(response)
    response_byte = response.encode()

    # response = "Hi! The connection has been established!"
    # response_byte = response.encode()
    # 4.4 sending a response to the client
    sock.sendall(response_byte)

    sock.shutdown(1)  # signal close of the writing side of the socket

# Don’t forget to close the socket after using:
sock.close()
