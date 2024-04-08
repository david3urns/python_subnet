import ipaddress

def validate_ip(ip_addr):
    try:
        ipaddress.ip_address(ip_addr)
        return True
    except ValueError:
        return False

def validate_cidr(cidr):
    try:
        cidr = int(cidr)
        if 0 < cidr < 33:
            return True
        else:
            return False
    except ValueError:
        return False

def calc_subnet_info(ip_addr, cidr):
    if validate_ip(ip_addr) and validate_cidr(cidr):
        ip_cidr = f"{ip_addr}/{cidr}"
        network = ipaddress.ip_network(ip_cidr, strict=False)
        network_address = network.network_address
        netmask_address = network.netmask
        broadcast_address = network.broadcast_address
        address_range = f"{network_address + 1} to {broadcast_address - 1}"
        print("Network Address:", network_address)
        print("Netmask Address:", netmask_address)
        print("Broadcast Address:", broadcast_address)
        print("Address Range:", address_range)
    else:
        print("Invalid IP address or CIDR.")

def calc_num_hosts(num_hosts_needed):
    if num_hosts_needed > 0:
        prefix_length = 32 - (num_hosts_needed + 2).bit_length()
        cidr = f"/{prefix_length}"
        print(f"Recommended CIDR notation for {num_hosts_needed} hosts:", cidr)
        return cidr
    else:
        print("Invalid number of hosts.")

def calc_class_subnet(net_class, num_nets_needed):
    subnet_dict = {
        'A': range(8, 31),
        'B': range(16, 31),
        'C': range(24, 31)
    }

    if net_class.upper() in subnet_dict:
        subnet_range = subnet_dict[net_class.upper()]
        for cidr in subnet_range:
            if 2 ** (32 - cidr) >= num_nets_needed:
                print(f"You will need a CIDR notation of /{cidr} to accommodate {num_nets_needed} subnets on a class {net_class.upper()} network.")
                return f"/{cidr}"
        print(f"Cannot accommodate {num_nets_needed} subnets on a class {net_class.upper()} network.")
    else:
        print("Invalid address class.")

def main():
    while True:
        print("")
        print("Subnet Calculator")
        print(" 1. Provide IP/CIDR to get information about the provided subnet.")
        print(" 2. Provide a number of hosts you need to subnet.")
        print(" 3. Determine how many subnets you can make based on address class.")
        print(" 4. Exit")
        print("")
        input_type = input("Please enter a selection from above: ")

        if input_type == '1':
            ip_cidr_in = input("Please provide a valid IP address with CIDR notation (e.g. 192.168.1.1/24): ")
            ip_in, cidr_in = ip_cidr_in.split("/")
            calc_subnet_info(ip_in, cidr_in)

        elif input_type == '2':
            num_hosts_in = int(input("How many hosts would you like to create a subnet for: "))
            calc_num_hosts(num_hosts_in)

        elif input_type == '3':
            addr_class_in = input("What class address would you like to subnet, A, B, or C? ").strip().upper()
            num_subnets_in = int(input("How many subnets would you like to create? "))
            calc_class_subnet(addr_class_in, num_subnets_in)

        elif input_type == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main()