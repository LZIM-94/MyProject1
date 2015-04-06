import socket 
import os.path

buffer_size = 2048



s = socket.socket() 
s.bind(('localhost',8000))
s.listen(10)


while True:
    connection, address  = s.accept()
    req = connection.recv(buffer_size)
    path = ''
	
    result = req.split('\n')[0].split(' ')[1]
    path = './' + result 
	
    if not os.path.isfile(path):
            path ='./index.html' 
            
    f = open(path, 'r')
    connection.send("""HTTP/1.1 200 OK\nContent-Type: text/html\n\n\n""" + f.read())
    f.close()
    connection.close()
s.close() 
