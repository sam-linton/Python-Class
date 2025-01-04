
def cipher(phrase, offset):
    letters = 'abcdefghijklmnopqrstuvwxyz '
    letters += letters.upper()
    num_letters = len(letters)
    code = ''
    for letter in phrase:
        index = letters.index(letter)
        new_index = (index + offset + num_letters) % len(letters)
        code = code + letters[new_index]
    return code

code = cipher('hello mommy', 3)
print(code)
decode = cipher(code, -3)
print(decode)