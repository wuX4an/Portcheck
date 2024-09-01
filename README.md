## Port Checker: 
A Python Tool for Scanning Ports This repository contains a simple Python tool for scanning ports on a given IP address. It utilizes the `requests` library for making HTTP requests and `tqdm` for displaying a progress bar. The tool also includes a ping check to ensure the target IP address is reachable. 
### Features 
- **Port Scanning:** Scans a specified range of ports on a target IP address. 
- **Progress Bar:** Displays a progress bar using `tqdm` to track the scanning process. 
- **Log File:** Saves the results of the scan to a log file, including the port number and HTTP status code. 
- **Ping Check:** Verifies the target IP address is reachable before starting the scan. 
- **Command-Line Interface:** Uses `click` to provide a user-friendly command-line interface. 
### Installation 
1. **Install Python:** Ensure you have Python installed on your system. 
2. **Install Dependencies:** Install the required libraries using pip: `pip install -r requirements.txt`
#### Alternative you can download the binary from the [latest](https://github.com/wuX4an/portcheck/releases/latest).
---
### Usage To use the port checker, run the following command in your terminal: 
``` 
python main.py --ip_address <target_ip_address> --start_port <start_port> --end_port <end_port> --log_path <log_file_path> 
```

#### **Example:** 
``` 
python main.py --ip_address 127.0.0.1 --start_port 80 --end_port 443 --log_path logs
```
#### This will scan ports 80 to 443 on the IP address 127.0.0.1 and save the results to a log file named `scanned_ports.log` in the `logs` directory. 
#### **Arguments:** 
- `--ip_address`: The target IP address to scan (Default: 127.0.0.1) .
- `--start_port`: The starting port number (Default: 1).
- `--end_port`: The ending port number (Default: 65535).
- `--log_path`: The path to the log file (Default: ./).
- `--help`: Displays the help message.
