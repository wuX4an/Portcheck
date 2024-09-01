import requests
from time import sleep
from tqdm import tqdm

def scan_ports(ip_address, start_port, end_port, log_path):
    open_ports = []
    with tqdm(total=end_port - start_port + 1, desc="Scanning ports") as pbar:
        for port in range(start_port, end_port + 1):
            try:
                response = requests.get(f"http://{ip_address}:{port}")
                if response:
                    open_ports.append(port)
                    pbar.set_description(f"Found open port: {port}")
                    pbar.update(1)
                    sleep(0.5)


                    with open(f"{log_path}/scanned_ports.log", "a") as f:
                        f.write(f"http://{ip_address}:{port} | {response.status_code}\n")
                else:
                    open_ports.append(port)
                    pbar.set_description(f"Found open port: {port}")
                    pbar.update(1)
                    sleep(0.5)
                    
                    with open(f"{log_path}/scanned_ports.log", "a") as f:
                        f.write(f"http://{ip_address}:{port} | {response.status_code}\n")
            except Exception:
                pbar.set_description(f"Error connecting to {ip_address}:{port}")
                pbar.update(1)

    if len(open_ports) > 0:
        print(f"Open ports saved to {log_path}/scanned_ports.log")
    else:
        print("No open ports found")