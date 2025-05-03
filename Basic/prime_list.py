
# Sieve_of_Eratosthenes

def prime_list(n):
    prime = [True] * (n+1)
    prime[0] = prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(i*i, n + 1, i):
                prime[j] = False

    prime_numbers = [i for i, is_prime in enumerate(prime) if is_prime]
    prime_numbers = []
    for z in range(2, n+1):
        if prime[z]:
            prime_numbers.append(z)
    return prime_numbers

print(prime_list(100))