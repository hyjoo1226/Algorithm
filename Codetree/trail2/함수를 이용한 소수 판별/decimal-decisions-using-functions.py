a, b = map(int, input().split())

def prime_num(a, b):
    prime_sum = 0

    for i in range(a, b + 1):
        is_prime = True
        
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        
        if is_prime == True:
            prime_sum += i
    
    return prime_sum

print(prime_num(a, b))