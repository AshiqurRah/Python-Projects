def is_palindrome(string):
    return string == string[::-1]

is_pal = is_palindrome("racecar")
print(is_pal)