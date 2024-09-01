from click import command, option
from ping3 import ping
from src import scan_ports

@command()
@option("--start_port", default=1, help="Starting port number (defautl: 1).")
@option("--end_port", default=65535, help="Ending port number (default: 65535).")
@option("--ip_address", default="127.0.0.1", help="The target IP address (default: 127.0.0.1).")
@option("--log_path", default=".", help="Path to the log file (default: ./ ).")
def main(start_port, end_port, ip_address, log_path):
    """
    Scans all the ports on the given IP address.
    """
    
    if start_port < 1:
        print("\033[0;31mStart port must be greater than 0.\033[0m")
    elif end_port > 65535:
        print("\033[0;31mEnd port must be less than or equal to 65535.\033[0m")
    elif end_port < start_port:
        print("\033[0;31mEnd port must be greater than or equal to start port.\033[0m")
    elif not ping(ip_address):
        print("\033[0;31mIP address is not reachable.\033[0m ")
    else:
        scan_ports(ip_address=ip_address, start_port=start_port, end_port=end_port, log_path=log_path)
if __name__ == "__main__":
    main()