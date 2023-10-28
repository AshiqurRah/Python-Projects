num = int(input("Enter a number: "))

is_num_perfect_square = False

if num > 0:
    sqrt = num ** 0.5

    if sqrt.is_integer():
        is_num_perfect_square = True

if is_num_perfect_square:
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")



