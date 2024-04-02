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
    prefix_length = 32 - (num_hosts + 2).bit_length()
    cidr = f"/{prefix_length}"

    return cidr

def calc_ip_w_cidr_netwk(addr_class, num_networks):                         #need to correct this. will need to ask user for class a b or c network
    #calculate CIDR based on required number of networks and address class
    prefix_length = 32 - (num_networks + 2).bit_length()
    cidr = f"/{prefix_length}"

    return cidr

def main():
    #determine user input type
    while True:
        print("")
        print("Subnet Calculator")
        print("")
        print(" 1. Provide IP/CIDR to get information about the provided subnet.")
        print(" 2. Provide a number of hosts you need to subnet.")
        print(" 3. Provide an address class and number of networks needed for subnetting.")
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
            break

        elif input_type == "2":
            while True:
                print("")
            #perform host function
            break

        elif input_type == "3":
            #perform network function
            break

        else:
            print("Invalid input, please try again.")
            break

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
