import socket
import subprocess
import platform

def ping_host():
    while True:
        host = input("Enter the host (or 'q' to quit): ")
        if host == 'q':
            break

        try:
            port = int(input("Enter the port: "))
        except ValueError:
            print("Invalid port number. Please try again.")
            continue

        if port <= 0 or port > 65535:
            print("Invalid port number. Please try again.")
            continue

        # Check if 'ping' utility is available
        is_ping_available = platform.system().lower() == 'windows'

        if is_ping_available:
            try:
                # Create a socket object
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    # Set a timeout value for the socket
                    sock.settimeout(5)  # 5 seconds

                    # Attempt to connect to the host and port
                    result = sock.connect_ex((host, port))

                    if result == 0:
                        print(f"Host {host} is reachable on port {port}")
                    else:
                        print(f"Host {host} is not reachable on port {port}")

            except socket.error as e:
                print(f"Socket error: {e}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            # Use 'ping' command to check host availability
            try:
                process = subprocess.Popen(["ping", "-n", "1", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                _, error = process.communicate()

                if process.returncode == 0:
                    print(f"Host {host} is reachable")
                else:
                    print(f"Host {host} is not reachable")

                if error:
                    print(f"Error: {error.decode().strip()}")

            except subprocess.CalledProcessError as e:
                print(f"Subprocess error: {e}")
            except Exception as e:
                print(f"Error: {e}")

# Call the function to ping a host
ping_host()
