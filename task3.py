def is_power_of_two(n):
    if n == 1:
        return True

    if n < 1 or n % 2 != 0:
        return False

    return is_power_of_two(n // 2)


n = int(input("Введіть натуральне число N: "))

if is_power_of_two(n):
    print("YES")
else:
    print("NO")