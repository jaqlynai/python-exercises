'''
Jaqlyn A
Dec 3 2021
Celsius-Fahrenheit Conversion
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def c_to_f(c):
    f = c * (9/5) + 32
    return f

def f_to_c(f):
    c = f - 32 * (5/9)
    return c

while True:
    user_choice = input('Would you like to convert °C to °F (1) or °F to °C (2)? ')
    if user_choice == '1':
        while True:
            user_celsius = input('Enter your °C temperature: ')
            try:
                user_celsius = float(user_celsius)
                print('Your new temperature would be ' + str(c_to_f(user_celsius)) + '°F.')
                break
            except ValueError:
                print('Please enter a number value.')
                continue
    elif user_choice == '2':
        while True:
            user_fahrenheit = input('Enter your °F temperature: ')
            try:
                user_fahrenheit = float(user_fahrenheit)
                print('Your new temperature would be ' + str(f_to_c(user_fahrenheit)) + '°C.')
                break
            except ValueError:
                print('Please enter a number value.')
                continue
    else:
        print('Please enter 1 or 2.')
        continue

