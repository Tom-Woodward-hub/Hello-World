print("display all prime numbers between 1-250")

import math
prime_list = []

for n in range(1, 250):
    prime=True
    for x in range(2, n):
        if n%x == 0:
            prime=False
            break
    else:
        prime_list.append(n)

print(prime_list)
