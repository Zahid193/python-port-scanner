import socket
import time

print("""
Simple Python Port Scanner
Author: Zahid Qureshi
""")

with open("results.txt", "w") as file:
    file.write("Scan Results\n")
    file.write("=" * 30 + "\n")

start_time = time.time()
target = input("Enter target IP or domain: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid target")
    exit()

print("=" * 50)
print(f" Target: {target_ip}")
print(" Scan started...")
print("=" * 50)

services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    443: "HTTPS"
}

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(2)

    result = sock.connect_ex((ip, port))

    if result == 0:
        service = services.get(port, "Unknown")
        print(f"[OPEN] Port {port} ({service})")

        with open("results.txt", "a") as file:
            file.write(f"[OPEN] Port {port} ({service})\n")

    sock.close()

for port in services.keys():
    print(f"Scanning port {port}....")
    scan_port(target_ip, port)

end_time = time.time()
print("=" * 50)
print(f"Scan completed in {round(end_time - start_time, 2)} seconds")