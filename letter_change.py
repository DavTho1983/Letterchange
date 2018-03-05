input = 'face!@ ^^'

def LetterChanges(str):

    newStr=''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'
    str = str.lower()
    for letter in str :
        if letter.isalpha() :
            id = (alphabet.find(letter)) % 26
            newLetter = alphabet[(id + 1) % 26]
            if newLetter in vowels :
                newLetter = newLetter.upper()

        else :
            newLetter = letter

        newStr += newLetter

    return newStr

# keep this function call here
print(LetterChanges(input))
