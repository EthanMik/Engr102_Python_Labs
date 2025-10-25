def is_prime(n: int) -> bool:
    for d in range(2, 10):
        if d == n: continue
        if n % d == 0:
            return False
    return True

primes = 0
for n in range(2, 73):
    if is_prime(n): primes += 1

print(f"There are {primes} in between 1 and 73")