def print_digits(n):
    if n == 0:
        return

    print_digits(n // 10)
    print(n % 10, end=" ")


n = int(input("Введіть натуральне число N: "))
print_digits(n)