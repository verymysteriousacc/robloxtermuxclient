
import socket
import time

ip = input("Server IP: ").strip()
port = int(input("Server port: "))
data = input("Message to send: ").encode()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(3)

try:
    s.sendto(data, (ip, port))
    print("Sent. Waiting for a reply...")

    start = time.time()
    response, address = s.recvfrom(4096)

    print(f"RESPONSE from {address[0]}:{address[1]}")
    print(f"Bytes received: {len(response)}")
    print(f"Data (hex): {response.hex()}")
    print(f"Elapsed: {time.time() - start:.3f}s")

except socket.timeout:
    print("No UDP response received within 3 seconds.")
except OSError as e:
    print(f"Socket error: {e}")
finally:
    s.close()
