#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverPort = 80   #using port 80
#Fill in start
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'the web server on port:',serverPort
#Fill in end
while True:
 #Establish the connection
 print('Ready to serve...')
 connectionSocket, addr = #Fill in start #Fill in end
 
 try:
     
 message = connectionSocket.recv(1024)
 print message,'::',message.split()[0],':',message.split()[1]
 filename = message.split()[1]
 f = open(filename[1:])
 outputdata = f.read()
 print outputdata
 #Send one HTTP header line into socket
 #Fill in start
 #Fill in end
 #Send the content of the requested file to the client
 for i in range(0, len(outputdata)):
 connectionSocket.send(outputdata[i].encode())
 connectionSocket.send("\r\n".encode())
 connectionSocket.close()
 
 except IOError:
 #Send response message for file not found
 #Fill in start
 connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')
 connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')
 #Fill in end
 #Close client socket
 #Fill in start
 #Fill in end
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
