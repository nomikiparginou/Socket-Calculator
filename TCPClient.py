from socket import *
#Host IP to send to. 127.0.0.1 is localhost
serverName = '127.0.0.1'
#Port to send to
serverPort = 12006
#Create the client socker
#socket.AF_INET == IPv4
#socket.SOCK_STREAM == TCP
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
#get input for numbers
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
#insert them into list "data"
data = [num1, num2]
#convert list to string
data = str(data)
#encode to bytes
data = data.encode()
#send data through socket
clientSocket.send(data)
#get input for operation
operation = input("Enter operation (+,-,*,/): ")
#encode string to bytes
clientSocket.send(operation.encode())
#send operation through socket
result = clientSocket.recv(4096)
#receive operation result
result = result.decode('utf-8')
#Print result
print (result)
#Close the socket
clientSocket.close()