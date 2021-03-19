import socket # allows establish connection over internet
from IPy import IP
import sys
# import threading
# from queue import Queue
# import time
from datetime import datetime

class PortScanner():
    banners = []
    open_ports = []

    def __init__(self, targets, port_num):
        self.targets = targets
        self.port_num = port_num

    # testing port scanner by using testphp.vulnweb.com website
    def DNS(self):
        try:
            IP(self.targets)
            return self.targets
        except ValueError: # if user input is domain name, find ip address
            return socket.gethostbyname(self.targets)

    def scan_port(self, port):
        try:
            ip = self.DNS()
            # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # socket.setdefaulttimeout(1) 
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((ip, port)) # socket try to connect to ip_address:port
            self.open_ports.append(port)

            try:
                banner = s.recv(1024).decode().strip('\n').strip('\r')
                self.banners.append(banner)
            except:
                self.banners.append(' ')
            
            s.close()

        except:
            pass # pass if port is closed

    
    def scan_targets(self):
        # ip = DNS(targets)
        
        # scan_threads(ip, port_num)
        for port in range(1, int(self.port_num)):
            self.scan_port(port)

    def scan(self):
        print(f'\nScanning started at: {datetime.now()}')
        self.scan_targets()
        print(f'\nScanning finished at: {datetime.now()}')

    # To prevent "double" modification of shared vairable. (race condition)
    # lock = threading.Lock()
    # q = Queue()

    # # thread is running by getting process from queue
    # def threader(self):
    #     while True:
    #         # gets thread from the queue
    #         thread_port = q.get()

    #         # Run the sacn
    #         scan_port(targets, thread_port)
    
    #         q.task_done()

    # def scan_threads(self):
    #     # how many threads are allowed
    #     for x in range(100):
    #         t = threading.Thread(targets=threader, args=(targets))

    #         # classifying as a daemon, so they will die when the main dies
    #         t.daemon = True

    #         # begins, must come after daemon definition
    #         t.start()

    #     # 100 jobs assigned
    #     for port in range(1, port_num):
    #         q.put(port)

    #     # wait until the thread terminates.
    #     q.join()

# only run portScanner.py is running. 
# if it is imported from other file, it will not execute
if __name__ == "__main__": 
    targets = input('[+] Enter targets/s To Scan (split multiple targets with ,): ')
    port_num = input('Enter Number Of Ports To Scan (Scan starts from port 1): ')

    target_scan = PortScanner(targets, port_num)
    target_scan.scan()
