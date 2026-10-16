def print_digits(n):
    if n == 0:
        return

    print(n % 10, end=" ")
    print_digits(n // 10)


n = int(input("Введіть натуральне число N: "))
print_digits(n)