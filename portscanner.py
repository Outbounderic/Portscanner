import socket
import termcolor

def scan_port(ipaddress, port):
    try:
        sock = socket.socket
        sock.connect((ipaddress, port))
        print("[+] Port Opened" + str(port))
    except:
        print("Port Closed")