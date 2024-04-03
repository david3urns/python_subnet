#formula is 2 ^ subnet bits - class bits

#class bits
class_a = 8
class_b = 16
class_c = 24

#the number of subnets we are trying to determine
num_subnets = 512

#cidr notation
cidr = 17
print("CIDR provided is ", cidr)

#now I need to turn this into bit length

subnet_bit_length = cidr    #.bit_length()

#print(subnet_bit_length)

exponent = subnet_bit_length - class_a

print("The exponent is ", exponent)

result = 2 ** exponent

print("The result is ", result, "The expected result is ", num_subnets)

cidr_table = { 8 : 0,
              9 : 2,
              10 : 4,
              11 : 8,
              12 : 16,
              13 : 32,
              14 : 64,
              15 : 128,
              16 : 256,
              17 : 512,
              18 : 1024,
              19 : 2048,
              20 : 4096,
              21 : 8192,
              22 : 16384,
              23 : 32768,
              24 : 65536,
              25 : 131072,
              26 : 262144,
              27 : 524288,
              28 : 1048576,
              29 : 2097152,
              30 : 4194304
}

#print(cidr_table[20])
#print(cidr_table[27])

x = 2
#subnet_list = dict.fromkeys(range(8,31), (x ^ 2))

subnet_list = []
for number in range(7, 30):
    subnet_list.append(number + 1)
#print(subnet_list)

power = 22
power_list = []
for i in range(1, power+1):
    power_list.append(2 ** i)
power_list.insert(0, 0)
#print(power_list)

subnet_dict = {}
for key in subnet_list:
    for value in power_list:
        subnet_dict[key] = value
        power_list.remove(value)
        break

print(subnet_dict)

subnet_dict_class_a = subnet_dict

subnet_dict_class_b = {}
