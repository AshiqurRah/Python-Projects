char = input("Enter a character: ")

if len(char) == 1:
    char = char.lower()

    if char in ('a', 'e', 'i', 'o', 'u'):
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
else:
    print("Enter a single character.")