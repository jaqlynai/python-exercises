alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#atbash cipher
def atbash_cipher(message):
    output = ''

    for letter in message:
        letter = letter.lower()

        letter_index = alphabet.index(letter)
        new_letter_index = (letter_index + 1) * -1 #negative runs through alphabet list backwards
        new_letter = alphabet[new_letter_index]

        output += new_letter

    return output

print(atbash_cipher('svool'))