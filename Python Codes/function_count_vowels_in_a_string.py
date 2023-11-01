def count_vowels(string):
    vowels = "aeiouAEIOU"
    return len([char for char in string if char in vowels])

count = count_vowels("Hellow, World")
print(count)