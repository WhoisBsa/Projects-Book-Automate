#-*- coding: utf-8 -*-
# Strong passwords detection

import re


def stripRegex(password):
    """ Strip the password"""
    password = re.sub(r'\s', '', password)
    return password


def strongPass():
    stgPass = re.compile(r'''^
                (?=.*[A-Za-z])          # uppercase and lowercase
                (?=.*\d)                # digits
                (?=.*[@$!%*#?&])        # special chars
                [A-Za-z\d@$!%*#?&]{8,}$ # all. Min of 8 chars
                ''', re.VERBOSE)
    return stgPass


def checkPass(password):
    """ Check Password """
    result = re.match(strongPass(), password)
    
    if result:
        printResult(result)
    else:
        printResult(result)
        option = input('Do you want to generate a password? [Y/N]: ').upper().strip()
        while option not in 'YN':
            option = input('Just Y or N, please: ').upper().strip()
        if option == 'N':
            print('=' * 44)
            print(f"{'=':<2}OK. Good luck and hope you're not hacked{'=':>2}")
            print('=' * 44)
        else:
            printPass(password)
        

def mkPass(size=8):
    """ Make a strong password """
    from random import choice
    import string

    chars = []
    chars.extend([i for i in string.ascii_letters])
    chars.extend([i for i in string.digits])
    chars.extend([i for i in '@$!%*#?&'])
    passwd = ''
    
    for i in range(size):
        passwd += choice(chars)
    
    while True:
        result = re.match(strongPass(), passwd)
        if result:
                break
        else:
            passwd = ''
            for i in range(size):
                passwd += choice(chars)
                 
    return passwd


def printPass(password):
    """ Print the password """
    password = mkPass()
    print('=' * 38)
    print(f'{"=":<2}Your password has been generated!!{"=":>2}')
    print(f'{"=":<4}Your new password is: {password}{"=":>4}')
    print('=' * 38)


def printResult(resul):
    """ Print Result """
    if resul:
        print('=' * 40)
        print(f'{"=":<2}Your password is secure. Good job!:){"=":>2}')
        print('=' * 40)
    else:
        print()
        print('-' * 25)
        print(f'{"":<2}Your password is weak{"":>2}')
        print('-' * 25)


def main():
    """Main Function"""
    print('=' * 30)
    print(f'{"=":<2}Strong Passwords Detection{"=":>2}')
    print('=' * 30)

    password = str(input('Password: '))          
    password = stripRegex(password)
    password = checkPass(password)

if __name__ == '__main__':
    main()
