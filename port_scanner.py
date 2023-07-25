from socket import *

# create a function connect_scanner
def connect_scanner(target_host, target_port):
    try:
        connecting_scanner = socket(AF_INET, SOCK_STREAM)
        connecting_scanner.connect(target_host, target_port)
        print('[+] tcp open' % target_port)
        connecting_scanner.close()
    except:
        print('[-]%d/tcp close' % target_port)

# created another function port scanner with arguments host and port
def port_scanner(target_host, target_ports):
    try:
        target_IP = gethostbyname(target_host)
    except:
        print('[-] Cannot resolve %d' % target_host)
        return
    try:
        target_name = gethostbyaddr(target_IP)
        print('\n[+] Scan result of: %s ' % target_name[0])
    except:
        print('\n [+] Scan result of: %s ' % target_IP)
    setdefaulttimeout(1)
    for target_port in target_ports:
        print('Scanning Port:  %d' % target_port)
        connect_scanner(target_host,target_port)

if __name__ == '__main__':
    port_scanner('google.com',[80,22])





