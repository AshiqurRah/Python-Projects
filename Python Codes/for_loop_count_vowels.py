def count_vowels(input_string):
    input_string = input_string.lower()

    vowel_count = 0

    vowels = set("aeiou")

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

input_string = input("Enter a string: ")

result = count_vowels(input_string)
print("Number of vowels in the string:", result)