original_string = input("Enter a string:")

reversed_string = ""

for char in original_string[::-1]:
    reversed_string += char

print("Reversed string:", reversed_string)