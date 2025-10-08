def sum(n: int) -> int:
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

n = int(input("Enter a positive integer: "))
print(f"Sum of the digits: {sum(n)}")