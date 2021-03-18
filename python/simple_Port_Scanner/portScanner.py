import socket # allows establish connection over internet
from IPy import IP
from datetime import datetime
# testing port scanner by using testphp.vulnweb.com website
def DNS(ip):
    try:
        IP(ip)
        return ip
    except ValueError: # if user input is domain name, find ip address
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress, port):
    try:
        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # socket.setdefaulttimeout(1) 
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((ipaddress, port)) # socket try to connect to ip_address:port
        
        try:
            banner = get_banner(s)
            print(f'[+] Open Port {port} : {banner}')
        except:
            print(f'[+] Open Port {port}')
    
    except:
        pass # pass if port is closed

targets_count = 0
def scan_target(target, port_num):
    global targets_count # access varaible that is declared in the outer scope
    ip = DNS(target)
    
    print(f'\n[Scanning Target {targets_count}] {target}')
    targets_count += 1
    
    for port in range(1, int(port_num)):
        scan_port(ip, port)

def scan(targets, port_num):
    print(f'\nScanning started at: {datetime.now()}')

    if ',' in targets:
        for ip_add in targets.split(','):
            scan_target(ip_add.strip(' '), port_num)
    else:
        scan_target(targets, port_num)

    print(f'\nScanning finished at: {datetime.now()}')

# only run portScanner.py is running. 
# if it is imported from other file, it will not execute
if __name__ == "__main__": 
    targets = input('[+] Enter Target/s To Scan (split multiple targets with ,): ')
    port_num = input('Enter Number Of Ports To Scan (Scan starts from port 1): ')

    scan(targets, port_num)

