import psutil as ps
import socket as sck
import nmap


def get_running_process(process_name):
    """
     @brief Get the name of the running computers. This is useful for debugging the process that is running
     @param process_name the name of the process to look for. E. g.'my - computer '
     @return a list of the names of the running computers
    """
    processes = ps.process_iter(attrs=['pid', 'name'])
    running_computers = []

    # Add all running processes to the running_computers list.
    for p in processes:
        # Add a process to the list of running computers.
        if process_name.lower() in p.info['name'].lower():
            running_computers.append(p.info['name'])

    return running_computers


def get_ip_and_network():
    """
     Get IP and network of host. This is used to check if host is running on network or not.
     
     
     @return tuple of local ip and network as string in format ( host_ip network )
    """
    local_ip = sck.gethostbyname(sck.gethostname())
    local_network = '.'.join(local_ip.split('.')[:-1])
    ip_range = local_network + ".0/24"
    return local_ip, ip_range


def scan_network(ip):
    """
     @brief Scan network for devices.
     @param ip IP address of the network
     @return List of host names of the active computers on
    """
    nm = nmap.PortScanner()
    nm.scan(hosts=ip, arguments='-sn')
    active_computers = []

    # Add host to active_computers list
    for host in nm.all_hosts():
        active_computers.append(host)
        print(f"Device: {host} is up")

    return active_computers


def check_device_with_process(process_name, ip_range):
    """
     @brief Scans network for devices with running processes.
     @param process_name Name of the process to look for
     @param ip_range IP range of the device
     @return Dictionary of computer_ip : list of
    """
    active_computers = scan_network(ip_range)
    device_with_running_process = {}

    # Set device_with_running_process for each computer_ip in active_computers.
    for computer_ip in active_computers:
        running_processes = get_running_process(process_name)
        # Set the running_processes variable to true if running_processes is set to true
        if running_processes:
            device_with_running_process[computer_ip] = running_processes

    return device_with_running_process


# This function is called by code generation. It checks if there is a device running on the node
if __name__ == "__main__":
    process_name = "python3"
    local_ip, ip_range = get_ip_and_network()
    print(f"Scanning network: {ip_range}")
    device_with_running_process = check_device_with_process(process_name, ip_range)

    if device_with_running_process:
        print("Process running on:")
        for computer, processes in device_with_running_process.items():
            print(f"Device IP address: {computer}")
            print(f"Running process: {', '.join(processes)}")
    else:
        print(f"No device found running : {process_name}")
