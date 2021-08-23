from socket import *
#Port to listen to
serverPort = 12006
close = False
#Create the server socker
serverSocket = socket(AF_INET,SOCK_STREAM)
#Bind the socket
serverSocket.bind(('127.0.0.1',serverPort))
#Listen for one connection only
serverSocket.listen(1)
print ('The server is ready to receive')
while not close:
    #Listen and wait for connection
    #Once a connection is made it returns two values, the conn will have the connection socket and the addr will have the address
    connectionSocket, addr = serverSocket.accept()
    #Print info: Connected address, Server IP & Port, Client IP & Port
    print("Connected by:", addr)
    print("Server Socket port: ", connectionSocket.getsockname())
    print("Client Socket port: ", connectionSocket.getpeername())
    #Receive list of data
    data = connectionSocket.recv(4096)
    #decode from bytes to utf-8
    data = data.decode('utf-8')
    # Convert decoded data into list of numbers
    data = eval(data)
    #insert the data into two separate variables and convert them to float
    num1 = float(data[0])
    num2 = float(data[1])
    #receive operation 
    operation = connectionSocket.recv(1024)
    #decode operation to string
    operation = operation.decode()

    #check if the numbers values are equal or above 0 and equal or less than 3000
    if (num1 >= 0 and num2 >= 0 and num1 <= 30000 and num2 <= 30000):
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1*num2
        elif operation == "/":
            if num2 == 0:
                result = "Cannot divide by 0"
            else:
                result = num1/num2
        else:
            result = "Unknown operant"
    else:
        result = "Number value cannot be less than 0 or over 3000"


    #Send it back where it came from
    connectionSocket.send(str(result).encode('utf8'))
    #Close the connection socket
    connectionSocket.close()
    serverSocket.close()