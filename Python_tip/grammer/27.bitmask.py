A = 11101010
B = 00110101

print (A&B)

print(A|B)

print(~A)

print(A^B)

def counter(A):
    small = 1
    num_bits = 0
    
    while small <= A:
        if small & A:
            num_bits+=1
        small <<= 1
    return num_bits
