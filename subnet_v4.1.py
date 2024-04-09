#!/usr/bin/env/python3
#Python Subnetting Script
#this script is used to assist with various subnet information. If provided with an IP/CIDR, it can provide the network and broadcast address, the netmask, and address range
#this script can also be given the number of hosts you need a subnet for, and provide you with the CIDR notation necessary
#lastly, this script can be given an address class (A, B, or C) and number of subnets desired, and give you the CIDR notation of a CIDR address to meet the number of subnets

import ipaddress
import os
import time

#function to clear the screen
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

#validate the provided IP address
def validate_ip(ip_addr):
    try:
        ipaddress.ip_address(ip_addr)
        return True
    except ValueError:
        return False

#validate the provided CIDR notation
def validate_cidr(cidr):
    cidr = int(cidr)
    if cidr > 0 and cidr < 33:
        return True
    else:
        return False

def calc_subnet_info(ip_addr, cidr):
    clear_screen()
    print("")
    print(f"Calculating subnet information for {ip_addr}/{cidr}")
    ip_cidr = ip_addr + "/" + cidr
    network = ipaddress.ip_network(ip_cidr, strict=False)
    network_address = network.network_address
    netmask_address = network.netmask
    broadcast_address = network.broadcast_address
    address_range = f"{network_address + 1} to {broadcast_address - 1}"

    # Print the results
    print("")
    print("Network Address:", network_address)
    print("Netmask Address:", netmask_address)
    print("Broadcast Address:", broadcast_address)
    print("Address Range:", address_range)
    print("")
    input("Press enter to continue.")


def calc_num_hosts(num_hosts_needed):
    clear_screen()
    if num_hosts_needed > 0 and num_hosts_needed < 16777214:
        prefix_length = 32 - (num_hosts_needed + 2).bit_length()
        cidr = f"/{prefix_length}"
        print(f"You will need a subnet with the CIDR notation of {cidr} to accomidate {num_hosts_needed} hosts.")
        input("Press enter to continue.")
        return cidr
    
    else:
        print("Invalid number of hosts, please enter a number from 1 to 16777214.")
        input("Press enter to continue.")

def calc_class_subnet(net_class, num_nets_needed):
    clear_screen()
    #create a list of CIDR notation for subnets, starting at 8 through 30
    subnet_list = []
    for number in range(7, 30):
        subnet_list.append(number + 1)

    #create a list of powers of 2
    power = 22
    power_list = []
    for i in range(1, power+1):
        power_list.append(2 ** i)
    power_list.insert(0, 0)
    #copy a power list for class b
    power_list_b = power_list[slice(len(power_list))]
    #copy a power list for class c
    power_list_c = power_list[slice(len(power_list))]

    #create the subnet dictionary by combining the subnet list and power of 2 list
    subnet_dict = {}
    for key in subnet_list:
        for value in power_list:
            subnet_dict[key] = value
            power_list.remove(value)
            break

    #begin creating the class b lists by trimming the original lists down to the size of the class b address range (16-30)
    del subnet_list[0:8]
    del power_list_b[15:23]

    #create the class b dictionary
    subnet_dict_b = {}
    for key in subnet_list:
        for value in power_list_b:
            subnet_dict_b[key] = value
            power_list_b.remove(value)
            break

    #begin creating class c lists by trimming the original lists to the size of class c range
    del subnet_list[0:8]
    del power_list_c[7:23]

    #create class c dictionary
    subnet_dict_c = {}
    for key in subnet_list:
        for value in power_list_c:
            subnet_dict_c[key] = value
            power_list_c.remove(value)
            break

    if net_class == 'A'.strip().lower():
        result = [(cidr, value) for cidr, value in subnet_dict.items() if value >= num_nets_needed]
        first_result = str(result[0])
        end_result = print(f"You will need a CIDR notation of /{first_result[1:3]} to accomidate {num_nets_needed} subnets on a class {net_class.upper()} network.")
        input("Press enter to continue.")
        return end_result

    elif net_class == 'B'.strip().lower():
        result = [(cidr, value) for cidr, value in subnet_dict_b.items() if value >= num_nets_needed]
        first_result = str(result[0])
        end_result = print(f"You will need a CIDR notation of /{first_result[1:3]} to accomidate {num_nets_needed} subnets on a class {net_class.upper()} network.")
        input("Press enter to continue.")
        return end_result
    
    elif net_class == 'C'.strip().lower():
        result = [(cidr, value) for cidr, value in subnet_dict_c.items() if value >= num_nets_needed]
        first_result = str(result[0])
        end_result = print(f"You will need a CIDR notation of /{first_result[1:3]} to accomidate {num_nets_needed} subnets on a class {net_class.upper()} network.")
        input("Press enter to continue.")
        return end_result

def main():
    while True:
        clear_screen()
        print("")
        print("Subnet Calculator")
        print("")
        print(" 1. Provide IP/CIDR to get information about the provided subnet.")
        print(" 2. Provide a number of hosts you need to subnet.")
        print(" 3. Determine how many subnets you can make based on address class.")
        print(" 4. Exit")
        print("")
        input_type = input("Please enter a selection from above: ")

        if input_type == '1':
            while True:
                clear_screen()
                ip_cidr_in = input("Please provide a valid IP address with CIDR notation (e.g. 192.168.1.1/24): ")
                if "/" in ip_cidr_in:
                    ip_in, cidr_in = ip_cidr_in.split("/")
                    validate_ip(ip_in)
                    validate_cidr(cidr_in)
                    if validate_ip(ip_in) and validate_cidr(cidr_in) == True:
                        calc_subnet_info(ip_in, cidr_in)
                        break
                else:
                    print("No valid IP/CIDR provided, please enter a valid IP/CIDR (e.g. 192.168.1.1/24): ")
                    input("Press enter to continue.")

        elif input_type == '2':
            while True:
                clear_screen()
                num_hosts_in = int(input("How many hosts would you like to create a subnet for: "))
                calc_num_hosts(num_hosts_in)
                break

        elif input_type == '3':
            while True:
                clear_screen()

                while True:
                    addr_class_in = input("What class address would you like to subnet, A, B, or C? ").strip().lower()
                    if addr_class_in in {"a", "b", "c"}:
                        break
                    else:
                        print("Invalid address class, please enter A, B, or C.")
                        input("Press enter to continue.")

                while True:
                    try:
                        num_subnets_in = int(input("How many subnets would you like to create? "))
                        if num_subnets_in > 0 and num_subnets_in < 4194304:
                            break
                        else:
                            print("Invalid number of subnets, please enter an interger between 0 and 4194304.")
                            input("Press enter to continue.")
                    except ValueError:
                        print("Invalid input, please enter a valid interger.")
                        input("Press enter to continue.")
                calc_class_subnet(addr_class_in, num_subnets_in)
                break

        elif input_type == '4':
            exit()

        else:
            print("Invalid input, please enter a number from 1-4.")
            input("Press enter to continue.")

main()
