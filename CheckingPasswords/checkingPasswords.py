#-*- coding: utf-8 -*-
# Strong passwords detection

import re


def stripRegex(password):
    """ Strip the password"""
    password = re.sub(r'\s', '', password)
    return password

def checkPass(password):
    """ Check Password """
    countNum = countLower = countUpper = 0
    check = re.compile(r'([a-zA-Z0-9!@#$%&\*-_=+,<\.>;:?])')
    
    for i in check.findall(password):
        if i.isnumeric():
            countNum += 1
        if i.islower():
            countLower += 1
        if i.isupper():
            countUpper += 1

    if countNum == 0 or countUpper == 0 or countLower == 0:
        print()
        print('-' * 25)
        print(f'{"":<2}Your password is weak{"":>2}')
        print('-' * 25)
        option = input('Do you want to generate a password? [Y/N]: ').upper().strip()
        while option not in 'YN':
            option = input('Just Y or N, please: ').upper().strip()
        if option == 'N':
            print('=' * 44)
            print(f"{'=':<2}OK. Good luck and hope you're not hacked{'=':>2}")
            print('=' * 44)
        else:
            password = mkPass()
            print('=' * 38)
            print(f'{"=":<2}Your password has been generated!!{"=":>2}')
            print(f'{"=":<4}Your new password is: {password}{"=":>4}')
            print('=' * 38)
    else:
        print('=' * 40)
        print(f'{"=":<2}Your password is secure. Good job!:){"=":>2}')
        print('=' * 40)

def mkPass(size=8):
    """ Make a strong password """
    from random import randint
    import string

    chars = []
    chars.extend([i for i in string.ascii_letters])
    chars.extend([i for i in string.digits])
    chars.extend([i for i in '!@#$%&*-_=+,<.>;:?'])
    count = 0
    passwd = ''
    
    for i in range(size):
        passwd += chars[randint(0,  len(chars) - 1)]
    while True:
        for i in passwd:
            if i.isnumeric():
                count += 1
        if count == 0:
            passwd = ''
            for i in range(size):
                passwd += chars[randint(0,  len(chars) - 1)]
        else:
            break
            
    return passwd


def main():
    """Main Function"""
    print('=' * 30)
    print(f'{"=":<2}Strong Passwords Detection{"=":>2}')
    print('=' * 30)
    password = str(input('Password: '))
    while len(password) < 8:
        password = str(input('Too short. Try again: '))
            
    password = stripRegex(password)
    password = checkPass(password)

if __name__ == '__main__':
    main()
