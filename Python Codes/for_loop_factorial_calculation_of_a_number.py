num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num+1):
    factorial += i 

print(f"The factorial of {num} is {factorial}")


# Input a number for which you want to print the multiplication table
number = int(input("Enter a number: "))

# Define the range (e.g., up to 10 for a 10x multiplication table)
table_range = 10

# Use a for loop to print the multiplication table
print(f"Multiplication Table for {number}:")

for i in range(1, table_range + 1):
    result = number * i
    print(f"{number} x {i} = {result}")
