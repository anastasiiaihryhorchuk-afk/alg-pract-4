def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n, end=" ")

n = (int(input("Введіть ціле натуральне число: ")))
print_numbers(n)