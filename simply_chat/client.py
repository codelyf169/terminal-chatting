#Client.py

import socket,select
import sys

def prompt(self) :
        sys.stdout.write('<You> ')
        sys.stdout.flush()
    
        
if __name__ == "__main__":
     
     
    host = "192.168.5.78"
    port = 5555
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()
     
    print 'Connected to remote host. Please choose a username'
    name=raw_input(" ")
    s.send(name)
    prompt()
     
    while 1:
        socket_list = [sys.stdin, s]
         
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :
                    sys.stdout.write(data)
                    prompt()
             

            else :
                msg = sys.stdin.readline()
                s.send("<"+name+">"+msg)
                prompt()