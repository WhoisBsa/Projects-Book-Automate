#! python3
# Mad Libs - Read a .txt file and allow
#            the user to add their own texts anywhere
#            ADJECTIVE, NOUN, ADVERB or VERB appear in the file

import re, sys

# Open the file 
mad_libs = open(sys.argv[1])
content = mad_libs.read()
mad_libs.close()
print('Initial File: ')
print(content)
# Regex for words 
check_word = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')

# Loop to check for the words to replace
while True:
    result = check_word.search(content)
    if result == None:
        break

    if result.group() == ('ADJECTIVE')or('ADVERB'):
        change_word = str(input(f'Enter an {result.group().lower()}: '))
    elif result.group() == ('NOUN')or('VERB'):
        change_word = str(input(f'Enter a {result.group().lower()}: '))

    content = check_word.sub(change_word, content, 1)


print('\nFinal File:')
print(content)

# Choose name of your file and then save in the directory
name = str(input('Name your file: '))
newFile = open(name + '.txt', "w")
newFile.write(content)

