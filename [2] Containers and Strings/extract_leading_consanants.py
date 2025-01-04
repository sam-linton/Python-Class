
def is_vowel(letter):
    return letter in 'aeiou'

def pig_latin(word):
    i = 0
    while not is_vowel(word[i]):
        i += 1
    suffix = 'yay' if i == 0 else 'ay'
    return word[i:] + word[:i] + suffix
    
word = input('input a word: ')
while len(word) > 0:
    print(pig_latin(word))
    word = input('input a word: ')