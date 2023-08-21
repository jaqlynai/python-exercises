'''
Jaqlyn A
Caesar Cipher Code
Jan 6 2021
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#caesar shift function
def caesar_cipher(message, key):
    output = ''
    for x in message:
        letter = x.lower() #makes characters lowercase to match case with pre-defined alphabet list

        if letter == ' ':
            output += letter

        else:
            letter_index = alphabet.index(letter) + key #shifts the index letter as per the shift key

            if letter_index > 25:
                letter_index -= 26 #loops the alphabet back to a after z

            new_letter = alphabet[letter_index]

            if x.isupper():
                output += new_letter.upper() #maintains any uppercase letters in initial message
                
            else:
                output += new_letter


    return output

#main loop
while True:
    
    user_choice = input('Please select one of the following: \n 1. encode \n 2. decode \n 3. quit \n')
    
    if user_choice == '1':
        user_message = input('Please enter your passage: ')
        user_letter = input('What letter should be equivalent to A? ')
        shift_key = ord(user_letter) - ord('a') #use ASCII characters to determine how much the cipher is shifting by
        print('Shifting passage by ' + str(shift_key) + '....')
        print('Your encrypted message is: ' + caesar_cipher(user_message, shift_key))
    
    elif user_choice == '2':
        user_message = input('Please enter your passage: ')
        user_letter = input('What letter should be equivalent to A? ')
        shift_key = ord(user_letter) - ord('a') - 26 #returns a negative shift key for decoding
        print('Shifting passage by ' + str(shift_key) + '....')
        print('Your encrypted message is ' + caesar_cipher(user_message, shift_key))

    elif user_choice == '3':
        print('Goodbye!')
        break

    else:
        print('Please enter 1, 2, or 3.')