def is_even(num: int) -> bool:
    if num % 2 == 0: return True
    return False

def func(num: int):
    if num < 100 or num > 1000000: return f"Wrong input!"

    num_1 = num % 10
    num = num // 10
    num_2 = num % 10

    if is_even(num_1) and is_even(num_2): 
        return f"Both even! \nSum = {num_1 + num_2}"

    if not is_even(num_1) and not is_even(num_2): 
        return f"Both odd! \nProduct = {num_1 * num_2}"

    return f"One odd, one even."

num = int(input("Enter an integer between 100 and 1000000, inclusive: "))
print(func(num))