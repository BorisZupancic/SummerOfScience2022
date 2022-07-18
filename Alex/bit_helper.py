import numpy as np
from inspect import signature

def transistor(input, control):
    return input and control

t = transistor

def AND(a, b):
    return a and b

def NOT(a):
    return not a

def OR(a, b):
    return NOT(AND( NOT(a), NOT(b)))


# Hey... no peeking!

























































def XOR_solution(a, b):
    return AND( OR(a, b), NOT(AND(a ,b)))

def add_solution(a, b):
    bit1 = XOR_solution(a, b)
    bit2 = AND(a, b)
    return bit1, bit2

def full_add_solution(a, b, c):
    Sum, carry1 = add_solution(a, b)
    bit1, carry2 = add_solution(Sum, c)
    bit2 = OR(carry1, carry2) 
    return bit1, bit2

def add_multi_solution(bits1, bits2):
    length = max(len(bits1), len(bits2))
    a = np.pad(bits1, (0, length-len(bits1)))
    b = np.pad(bits2, (0, length-len(bits2)))
    output_bits = np.full((length + 1), False)
    
    carry = False
    for i in range(length):
        output_bits[i], carry = full_add_solution(a[i], b[i], carry)
    
    output_bits[length] = carry
    return output_bits

def binary_to_int(bits):
    values = 2 ** np.arange(len(bits))
    return np.sum(bits * values)

def int_to_binary(num, length=None):
    if not num:
        return np.full((length), False)
    
    s = int(np.floor(np.log2(num))) + 1
    
    if length:
        bits = np.full((length), False)
    else:
        bits = np.full((s), False)

    for i in np.arange(0, s)[::1]:
        place_value = 2**i
        bits[i] = place_value <= num
        num -= bits[i]*2**i 
        
    return bits

def truth_table(func):
    n = len(signature(func).parameters)
    num_bits = np.array([int_to_binary(i, length=n) for i in np.arange(2**n)], dtype=int)
    for bits in num_bits:
        out = func(*bits)
        
        if hasattr(out, '__len__'):
            print(f'{func.__name__}({", ".join(map(str, bits))}) = {tuple(map(int, out))}')
        else:
            print(f'{func.__name__}({", ".join(map(str, bits))}) = ({int(out)})')
            
        