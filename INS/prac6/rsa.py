# RSA Algorithm

import random
import math


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def gen_prime(num):
    prime = []
    for i in range(2, num+1):
        if is_prime(i):
            prime.append(i)
    return prime


prime_num = gen_prime(20)

q = random.choice(prime_num)
p = random.choice(prime_num)

# def key_gen():
# this return a list containing [e,d,n]
p = random.choice(prime_num)
q = random.choice(prime_num)
# def is_same(p,q):
#     if p == q:
#         p = random.choice(prime_num)
#     is_same(p, q)

# p, q = is_same(a, b)

n = p * q
phi_n = (p-1) * (q-1)
print(p, q)
print(n, phi_n)
e = 0
for i in range(2, phi_n):
    if math.gcd(i, phi_n) == 1:
        e = i
# d = ( phi_n * i ) + 1 / e
# loop until i is not an absolute value

print(e)
print(math.gcd(1, phi_n))
