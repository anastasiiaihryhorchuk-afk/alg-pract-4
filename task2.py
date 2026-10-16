def print_numbers(a, b):
    print(a, end=" ")

    if a == b:
        return
    if a < b:
        print_numbers(a + 1, b)
    else:
        print_numbers(a - 1, b)


a = int(input("Введіть число A: "))
b = int(input("Введіть число B: "))

print_numbers(a, b)