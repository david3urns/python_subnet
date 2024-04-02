#!/usr/bin/env python3
# Python subnetting script
# This script asks the user if they are providing an IP with CIDR, or if they are providing a number of hosts or a number of networks required and
# provides the corresponding information

import ipaddress

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False
    
def validate_cidr(cidr):
    try:
        ipaddress.ip_network(cidr, strict=False)
        return True
    except ValueError:
        return False
    
def calc_subnet_info(ip_cidr):
    # Parse the IP address and CIDR
    network = ipaddress.ip_network(ip_cidr, strict=False)

    # Get network address
    network_address = network.network_address

    # Get netmask
    netmask_address = network.netmask

    # Get the broadcast address
    broadcast_address = network.broadcast_address

    # Get address range
    address_range = f"{network_address + 1} to {broadcast_address - 1}"

    return network_address, netmask_address, broadcast_address, address_range

def calc_ip_with_cidr(num_hosts):
    # Calculate CIDR based on the required number of hosts
    prefix_length = 32 - (num_hosts + 2).bit_length()
    cidr = f"/{prefix_length}"

    return cidr

def calc_ip_w_cidr_netwk(num_networks):
    # Calculate CIDR based on required number of networks
    prefix_length = 32 - num_networks.bit_length()
    cidr = f"/{prefix_length}"

    return cidr

def main():
    while True:
        print("")
        print("Subnet Calculator")
        print("")
        print(" 1. Provide IP/CIDR to get information about the provided subnet.")
        print(" 2. Provide a number of hosts you need to subnet.")
        print(" 3. Provide the number of networks needed for subnetting.")
        print(" 4. Exit")
        print("")
        input_type = input("Please enter a selection from above: ")

        if input_type == "1":
            while True:
                print("")
                ip_cidr = input("Enter an IP address with a CIDR Notation (ex: 192.168.1.1/24): ")
                if validate_cidr(ip_cidr):
                    break
                else:
                    print("Invalid CIDR notation, please try again.")
            display_subnet_info(ip_cidr)
            if input("Press Enter to return to the main menu or 'q' to exit: ").strip().lower() == 'q':
                break

        elif input_type == "2":
            while True:
                print("")
                num_hosts = int(input("Enter the number of hosts you need addresses for: "))
                if num_hosts > 0:
                    break
                else:
                    print("Invalid number of hosts, please enter a positive integer.")

            cidr = calc_ip_with_cidr(num_hosts)
            print(f"Recommended CIDR notation for {num_hosts} hosts:", cidr)
            ip_cidr = input("Enter IP address (optional): ").strip() + cidr
            display_subnet_info(ip_cidr)
            if input("Press Enter to return to the main menu or 'q' to exit: ").strip().lower() == 'q':
                break

        elif input_type == "3":
            while True:
                print("")
                num_networks = int(input("Enter the number of networks you need addresses for: "))
                if num_networks > 0:
                    break
                else:
                    print("Invalid number of networks, please enter a positive integer.")

            cidr = calc_ip_w_cidr_netwk(num_networks)
            print(f"Recommended CIDR notation for {num_networks} networks:", cidr)
            ip_cidr = input("Enter IP address(optional): ").strip() + cidr
            display_subnet_info(ip_cidr)
            if input("Press Enter to return to the main menu or 'q' to exit: ").strip().lower() == 'q':
                break

        elif input_type == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid input, please try again.")

def display_subnet_info(ip_cidr):
    # Calculate subnet information if IP/CIDR provided
    if ip_cidr:
        network_address, netmask_address, broadcast_address, address_range = calc_subnet_info(ip_cidr)

        # Print the results
        print("Network Address:", network_address)
        print("Netmask Address:", netmask_address)
        print("Broadcast Address:", broadcast_address)
        print("Address Range:", address_range)


if __name__ == "__main__":
    main()
