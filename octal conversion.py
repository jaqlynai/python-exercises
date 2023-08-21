# Jaqlyn Ai
# Feb 10 2022
# Octal Conversions
 
from tkinter import N


class Binary(object):
    """Represents a binary number
 
    Attributes:
      binary_number: string
    """
 
    def __init__(self, binary_number=''):
        self.binary_number = binary_number
       
    def __str__(self):
        return self.binary_number
   
    def tobase10(self):
        decimalnum=0
        binnum = self.binary_number
        binnum = binnum[::-1] #reverse string
        #print(binnum)
        for i in range(len(binnum)):
            decimalnum += int(binnum[i])*2**i
        return decimalnum
   
    def tobinary(self,decnum):
        exp = 0
        while 2**exp <= decnum:
            exp +=1
        exp = exp - 1
        binum = '1'
        remainder = decnum - 2**exp
        exp = exp -1
        while exp >= 0:
            if remainder >= 2**exp:
                remainder = remainder - 2**exp
                binum =binum+'1'
            else:
                binum =binum+ '0'
            exp = exp-1
        return binum
    
    #my code: binary to octal
    def toOctal(self):
        binnum = self.binary_number
        total = ''
        digit_count = len(binnum)

        while digit_count > 0:

            oct_digit = 0    
            bin_digit = ''

            for digit in binnum[::-1]: #loops through binary number backwards
                if digit_count < 3: #runs if there are less than three digits left
                    bin_digit += binnum
                    break

                if len(bin_digit) < 3: #sections binary number into groups of three
                    bin_digit += digit

            for exp in range(len(bin_digit)):
                exp = int(exp)
                oct_digit += int(bin_digit[exp]) * 2**exp

            total = str(oct_digit) + total
            #removes group of three from original binary number
            binnum = binnum.removesuffix(binnum[len(binnum)-3:])
            digit_count -= 3

        return total     

# ***************** end of class Binary *******************

#my code: octal class
class Base8(object):
 
    def __init__(self, base8num = ''):
        self.base8num = base8num
 
    def __str__(self):
         return self.base8num
 
    def toBase10(self):
        decimalnum = 0
        base8 = self.base8num
        base8 = base8[::-1]
        for x in range(len(base8)):
            decimalnum += int(base8[x]) * 8 ** x
        return decimalnum
   
    def toBase8(self, decimalnum):
        decimalnum = int(decimalnum)

        if decimalnum < 8:
            return str(decimalnum)
       
        b8num = ''
        exp = 0
 
        while 8 ** exp < decimalnum:
            exp += 1
 
        while exp >= 0:
           
            for digit in range(8):
               
                if digit * 8**exp == decimalnum:
                    b8num = b8num + str(digit)
                    decimalnum -= digit * 8**exp
                    break
               
                elif digit * 8**exp > decimalnum:
                    digit = digit - 1
                    b8num = b8num + str(digit)
                    decimalnum -= digit * 8**exp
                    break
               
                if digit == 7 and digit * 8**exp < decimalnum:
                    b8num = b8num + str(digit)
                    decimalnum -= digit * 8**exp
                    break
               
                if decimalnum < 0:
                    break

            exp -= 1
 
        if str(b8num)[0] == '0': #strips code of extra zero at beginning (if any)
            nonzero_num = str(b8num)[1:]
            return int(nonzero_num)
 
        else:
            return b8num
            
    def toBinary(self):
        binary = '' #final number
        
        base8 = self.base8num
        
        for digit in base8[::-1]: #loops through each digit of the octal number
            exp = 0
            binum = ''
            
            while 2**exp <= int(digit): #finds highest bit for the digit
                exp += 1
            
            exp -= 1
            remainder = int(digit) #remainder set to digit value

            while exp >= 0:
                    
                if remainder >= 2**exp:
                    remainder -= 2**exp
                    binum += '1'

                else:
                    binum += '0'

                exp -= 1

            while len(binum) != 3: #fills in extra zeroes so each digit is three bits
                binum = '0' + binum
            '''while len(binum) % 3 != 0: #fills in extra zeroes so each digit is three bits
                binum = '0' + binum'''
                
            binary = binum + binary
                
        return binary
 
# **************** end of class Base8 ****************


while True:

    user_choice = input('Please choose what you would like to convert:\n\
    1. Octal to Decimal\n\
    2. Decimal to Octal\n\
    3. Octal to Binary\n\
    4. Binary to Octal\n\
    ')

    if user_choice == '1':
        octal = input('Please enter octal number here: ')
        oct_to_dec = Base8(octal)
        print(octal, '(octal) =', oct_to_dec.toBase10(), '(decimal)')
    elif user_choice == '2':
        decimal = input('Please enter decimal number here: ')
        dec_to_oct = Base8(decimal)
        print(decimal, '(decimal) =', dec_to_oct.toBase8(decimal), '(octal)')
    elif user_choice == '3':
        octal = input('Please enter octal number here: ')
        oct_to_bin = Base8(octal)
        print(octal, '(octal) =', oct_to_bin.toBinary(), '(binary)')
    elif user_choice == '4':
        binary = input('Please enter binary number here: ')
        bin_to_oct = Binary(binary)
        print(binary, '(binary) =', bin_to_oct.toOctal(), '(octal)')
    else:
        print('Please enter 1, 2, 3, or 4.')
        continue

    play_again = input('Would you like to go again? (Y/N) ')
    if play_again == 'Y' or play_again == 'y':
        continue
    else:
        print('Goodbye!')
        quit()