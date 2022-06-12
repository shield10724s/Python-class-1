intro = input('Enter your introduction: ')
print('intro')
character_count = 0
word_count = 1
for i in intro:
    character_count = character_count+1
    if(i == ' '):
        word_count = word_count+1
print('Number of words in the string: ', word_count)
print('Number of characters in the string: ', character_count)