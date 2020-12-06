# This Project is Taking a Word and Convert it to a BIG BLOCK LETTER with O

letters_code = [[[' OOO '], ['O   O'], ['OOOOO'], ['O   O'], ['O   O'], [' ']],  # A
                [['OOOO '], ['O   O'], ['OOOO '], ['O   O'], ['OOOO '], [' ']],  # B
                [['OOOOO'], ['O    '], ['O    '], ['O    '], ['OOOOO'], [' ']],  # C
                [['OOOO '], ['O   O'], ['O   O'], ['O   O'], ['OOOO '], [' ']],  # D
                [['OOOOO'], ['O    '], ['OOOOO'], ['O    '], ['OOOOO'], [' ']],  # E
                [['OOOOO'], ['O    '], ['OOOOO'], ['O    '], ['O    '], [' ']],  # F
                [['OOOOO'], ['O    '], ['O OOO'], ['O   O'], ['OOOOO'], [' ']],  # G
                [['O   O'], ['O   O'], ['OOOOO'], ['O   O'], ['O   O'], [' ']],  # H
                [[' OOO '], ['  O  '], ['  O  '], ['  O  '], [' OOO '], [' ']],  # I
                [[' OOO '], ['  O  '], ['  O  '], ['O O  '], ['OOO  '], [' ']],  # J
                [['O  OO'], ['O O  '], ['OO   '], ['O O  '], ['O  OO'], [' ']],  # K
                [['OO   '], ['O    '], ['O    '], ['O   O'], ['OOOOO'], [' ']],  # L
                [['O   O'], ['O O O'], ['O O O'], ['O   O'], ['O   O'], [' ']],  # M
                [['O   O'], ['OO  O'], ['O O O'], ['O  OO'], ['O   O'], [' ']],  # N
                [[' OOO '], ['O   O'], ['O   O'], ['O   O'], [' OOO '], [' ']],  # O
                [['OOOO '], ['O   O'], ['OOOO '], ['O    '], ['O    '], [' ']],  # P
                [[' OOO '], ['O   O'], ['O O O'], [' OOO '], ['   OO'], [' ']],  # Q
                [['OOOO '], ['O   O'], ['OOOO '], ['O   O'], ['O   O'], [' ']],  # R
                [['OOOOO'], ['O    '], ['OOOOO'], ['    O'], ['OOOOO'], [' ']],  # S
                [['OOOOO'], ['  O  '], ['  O  '], ['  O  '], ['  O  '], [' ']],  # T
                [['O   O'], ['O   O'], ['O   O'], ['O   O'], [' OOO '], [' ']],  # U
                [['O   O'], ['O   O'], ['O   O'], [' O O '], ['  O  '], [' ']],  # V
                [['O   O'], ['O O O'], ['O O O'], ['O O O'], [' O O '], [' ']],  # W
                [['O   O'], [' O O '], ['  O  '], [' O O '], ['O   O'], [' ']],  # X
                [['O   O'], ['O   O'], [' OOO '], ['  O  '], ['  O  '], [' ']],  # Y
                [['OOOOO'], ['   O '], ['  O  '], [' O   '], ['OOOOO'], [' ']],  # Z
                [['   '], ['   '], ['   '], ['   '], ['   '], [' ']],  # SPACE
                ]

alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,  # Dictionary for letter position in letter code.
            'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
            'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,
            'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
            'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, ' ': 26}
print('Enter a word which you would like to be converted into block letter:')
print('Please type it CAPITAL')
word = input('')  # take a word or can be sentence
word_length = len(word)  # length of word to know how much should repeat the letter converter
output_file = open('output.txt', 'w')  # Create output.txt file
for i in range(6):  # the tall of  each letter
    for letter in range(word_length):  # repeat for how many word
        output = letters_code[alphabet[word[letter]]][i]  # put the number of letter in alphabet and convert it to code
        clean_output = ' '.join([str(elem) for elem in output] + [' '])  # remove the [''] from list
        if letter == word_length - 1:  # Go next line
            clean_output += '\n'
        output_file.write(str(clean_output))  # print the out put in output.txt
output_file.close(),
print('FINISHED, YOUR WORK IS ON output.txt')
