#
# Pig Latin
#
def pig_latin(word):
    if word[0] in "aeiou":
        return word + 'yay'
    else:
        return word[1:] + word[0] + 'ay'
    
# The program
word = input('Input word: ')
while len(word) > 0:
    print(pig_latin(word))
    word = input('Input word: ')
    
