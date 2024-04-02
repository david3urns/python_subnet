#!/usr/bin/env/python3
#python subnetting script
#this script will ask the user if they are providing an IP with CIDR, or if they are providing a number of hosts or a number of networks required and
#provide the corresponding information

import ipaddress

def validate_ip(ip):
    try:
        ipaddress.ip.address(ip)
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
    #parse the IP address and CIDR
    network = ipaddress.ip_network(ip_cidr, strict=False)

    #get network address
    network_address = network.network_address

    #get netmask
    netmask_address = network.netmask

    #get the broadcast address
    broadcast_address = network.broadcast_address

    #get address range
    address_range = f"{network_address +1 } to {broadcast_address - 1}"

    return network_address, netmask_address, broadcast_address, address_range

def calc_ip_with_cidr(num_hosts):
    #calculate CIDR based on the required number of hosts
    prefix_length = 32 - (num_hosts.bit_length() -1)
    cidr = f"/{prefix_length}"

    return cidr

def calc_ip_w_cidr_netwk(num_networks):
    #calculate CIDR based on required number of networks
    prefix_length = 32 -(num_networks.bit_length() -1)
    cidr = f"/{prefix_length}"

    return cidr

def main():
    #determine user input type
    while True:
        input_type = input ("Do you have an IP address with CIDR (enter 1) or do you have the number of hosts or networks needed (enter 2)? ")

        if input_type == "1":
            while True:
                ip_cidr = input ("Enter an IP address with a CIDR Notation (ex: 192.168.1.1/24): ")
                if validate_cidr(ip_cidr):
                    break
                else:
                    print("Invalid CIDR notation, please try again.")
            break

        elif input_type == "2":
            while True:
                choice = input("Do you want to specify the number of hosts (press 1) or the number of networks (press 2) needed? ")
                if choice == "1":
                    while True:
                        num_hosts = int(input("Enter the number of hosts you need addresses for: "))
                        if num_hosts > 0:
                            break
                        else:
                            print("Invalid number of hosts, please enter an interger.")

                    cidr = calc_ip_with_cidr(num_hosts)
                    print(f"Recommended CIDR notation for {num_hosts} hosts:", cidr)
                    ip_cidr = input("Enter IP address (optional): ").strip() + cidr
                    break

                elif choice == "2":
                    while True:
                        num_networks = int(input("Enter the number of networks you need addresses for: "))
                        if num_networks > 0:
                            break
                        else:
                            print("Invalid number of networks, please enter an interger.")

                    cidr = calc_ip_w_cidr_netwk(num_networks)
                    print(f"Recommended CIDR notation for {num_networks} networks:", cidr)
                    ip_cidr = input("Enter IP address(optional): ").strip() + cidr
                    break
                else:
                    print("Invalid input. Please enter 1 or 2.")

            break
        else:
            print("Invalid input. Please enter 1 or 2.")

    #calculate subnet info if IP/CIDR provided
    if ip_cidr:
        network_address, netmask_address, broadcast_address, address_range = calc_subnet_info(ip_cidr)

        #print the results
        print("Network Address:", network_address)
        print("Netmask Address:", netmask_address)
        print("Broadcast Address:", broadcast_address)
        print("Address Range:", address_range)

if __name__ == "__main__":
    main()
