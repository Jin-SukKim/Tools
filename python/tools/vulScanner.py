import portScanner as scanner

targets_ip = input('[+] * Enter Target/s To Scan For Vulnerable Open Ports: ')
port_num = input('[+] * Enter Amount Of Ports To Scan (500 - first 500 ports): ')
vul_file = input('[+] * Enter Path To The File With Vurlnerable Softwares: ')
print('\n')

target = scanner(targets_ip, port_num)
target.scan()

with open(vul_file, 'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0) # to seek from beginning from file to end.
        for line in file.readlines():
            if line.strip() in banner:
                print(f'[!] VULNERABLE BANNER: "{banner}" ON PORT: {target.open_ports[count]}')

        count += 1