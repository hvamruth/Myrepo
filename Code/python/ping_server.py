import ping3
import sys

def ping_server(ip_address):
    try:
        response_time = ping3.ping(ip_address)
        if response_time is not None:
            print(f"Ping to {ip_address} successful. Response time: {response_time:.2f} ms")
        else:
            print(f"Ping to {ip_address} failed.")
    except PermissionError:
        print("Ping failed. Please run the script as a superuser (root/Administrator).")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ping_server.py <ip_address>")
        sys.exit(1)

    ip_address = sys.argv[1]
    ping_server(ip_address)
