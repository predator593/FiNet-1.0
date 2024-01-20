'''
# accept a string and split it with the cidr notation  ---> 1
# store the no.of subnets required ---> 2
# 
# calculate & check the [2^n] value is > or == to the no.of subnets given that is [2]
# now once the no.is found add the valueb of n to the cidr | new_cidr_value = cidr value + n -------> 3
#
# once the new cidr is found then convert the cidr value[maximum of 32] into the binary format 

# once the binary format is done count the no.of zeros and their position which is imp to identify the octet and 
#to determine the need to perform another 2^n formula and to determine the submnet mask [little heavy task to build logic]

# after the formula for finding the ip address range is done --------> 4

#  combine 1+2+3+4 => output and separate the network address , Range , last ip address  .

'''

# finding the 2^n value :


from ast import Break


def A(a) :
    n=0
    while 2**n < a:
        n+=1 
    return n

# convertion to binary 
def B(b) :
    binary_form = bin(b)[2:]
    return binary_form

# finding the octet position of subnetmasking
def E(n):
    if n <= -1 or n > 8:
        return None  # Handle invalid input
    result = 0
    for exponent in range(7, 7 - n, -1):
        result += 2 ** exponent
    return result

#new cidr configuration for the 32 bit size
def C(c):
    d=0
    d1=0
    if 0<=c and c<=8 :
         if c==8:
            print("255.0.0.0")
         else :
            print("\n","Subnet Mask : ",E(c),".0.0.0")
            d=8-c 
         return d
    elif 9<=c and c<=16  :
        if c==16:
            print("255.255.0.0")
        else:
            d = c-8 
            print("\n","Subnet Mask : "," 255.",E(d),".0.0") 
            d1=16-c
        return d1
    elif 17<=c and c<=24  :
        if c==24:
            print("255.255.255.0")
            print("\nsry cant provide for more its already housefull")
            end()
        else :
            d=c-16
            print("\n","Subnet Mask : "," 255.255.",E(d),".0") 
            d1=24-c
        return d1
    elif 25<=c and c<=32  :
        if c==32 :
            print("255.255.255.255")
        else : 
           d = 32-c
           print("\n","Subnet Mask : "," 255.255.255",E(d)) 
           d1=c-24
        return d1
    else:
        return None       

# check 255 limit
def G(g):
    # Check if the input is a string
    if g.isnumeric():
        g=int(g)
        if g > 0 and g <=255 :
            print("valid")
            return g
        else :
            print("invalid ")
    elif g.isalpha():
        print("be in your limits ")
    else :
        print("u r a existential crisis !!")

# range allocation of ipv4
def H(ip_address,ip_range,Subnets):
    W,X,Y,Z = map(int, ip_address.split('.'))
    for _ in range(Subnets):

        # Calculate the network address
        network_address = f"{W}.{X}.{Y}.{Z}"
        # Calculate the IP range
        ip_range_start = f"{W}.{X}.{Y}.{Z + 1}"
        Z += ip_range
        
        if Z > 255:
            carry, Z = divmod(Z, 256)
            Y += carry
            if Y > 255:
                carry, Y = divmod(Y, 256)
                X += carry
                if X > 255:
                    carry, X = divmod(X, 256)
                    W += carry
                    if W > 255:
                        print("Subnets exhausted.")
                        break
        
        ip_range_end = f"{W}.{X}.{Y}.{Z - 1}"
        
        # Calculate the broadcast address
        broadcast_address = f"{W}.{X}.{Y}.{Z}"
        
        # Print the subnet details
        print(f"Network Address: {network_address}\t\tIP Range: [{ip_range_start}-{ip_range_end}]\t\tBroadcast IP: {broadcast_address}")
        
        # Increment the network address by 1
        Z += 1

ipv4withcidr = input("ipv4 / cidr : ")
subnets = int(input("No.of Subnets :"))

ipv4withoutcidr = ipv4withcidr.split('/')
oldcidr = int(ipv4withoutcidr[1])

ipv4=ipv4withoutcidr[0].split('.')
octet1=ipv4[0]
octet2=ipv4[1]
octet3=ipv4[2]
octet4=ipv4[3]
z=G(octet1)
y=G(octet2)
x=G(octet3)
w=G(octet4)


newcidr = oldcidr + A(subnets)

binarycidr = B(newcidr)

N = C(newcidr)

iprange = 2**N - 2 

print(ipv4withoutcidr[0] , "/" , newcidr, " : " , binarycidr , ":" ,"no.of 0's =",N, " : " ,"ip range =", iprange)


#now we need to add ip range with w until it is full and stop then start filling next one[x] 

H(ipv4withoutcidr[0],iprange,subnets)

