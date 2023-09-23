import socket

target_ip = "10.10.10.10"
web_ports = [80, 8080, 8000, 8888]  # Common web server ports

def check_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
            return True
    except (socket.timeout, ConnectionRefusedError):
        return False

for port in range(1, 65536):
    if check_port(target_ip, port):
        if port in web_ports:
            print(f"Port {port} (HTTP) is open.")
        else:
            print(f"Port {port} is open, but not identified as a web server.")
