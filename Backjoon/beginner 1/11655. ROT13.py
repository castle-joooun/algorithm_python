s = input()
result = ''

for char in s:
    if char.isalpha():
        check_alphabet = ord(char) + 13

        if (char.isupper() and check_alphabet > 90) or \
                (char.islower() and check_alphabet > 122):
            check_alphabet -= 26
        result += chr(check_alphabet)
    else:
        result += char

print(result)
