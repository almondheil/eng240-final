letter_to_code = {
    'a': '0',      # letters
    'b': '1',
    'c': '10',
    'd': '11',
    'e': '100',
    'f': '101',
    'g': '110',
    'h': '111',
    'i': '1000',
    'j': '1001',
    'k': '1010',
    'l': '1011',
    'm': '1100',
    'n': '1101',
    'o': '1110',
    'p': '1111',
    'q': '10000',
    'r': '10001',
    's': '10010',
    't': '10011',
    'u': '10100',
    'v': '10101',
    'w': '10110',
    'x': '10111',
    'y': '11000',
    'z': '11001',
    ',': '11010',  # punctuation
    '.': '11011',
    '!': '11100',
    '?': '11101',
    '-': '11110',
    ' ': '11111'   # space
}

def code_to_whitespace(code):
    # Use code to generate a string of whitespace
    whitespace = ''
    for digit in code:
        # Insert a ' ' or a '\t' depending on code digit
        if (digit == 0):
            whitespace += ' '
        else:
            whitespace += '\t'

    # Return the calculated string
    return whitespace

def add_whitespace_at_end(line, whitespace):
    # get the start of the line, but remove extra space characters from the end
    line_content = line.rstrip('\r\n \t')

    # add our whitespace at the end, along with a new newline
    return line_content + whitespace + '\n'

def encode_message():
    # Ask the user what their secret message will be
    secret_message = input('Secret message? ')

    # Make the secret message lowercase
    secret_message = secret_message.lower()
    # If we find a letter that's not in our mapping, quit the program
    for letter in secret_message:
        if not letter in letter_to_code:
            print('Letter' + letter + 'not allowed in message.')
            exit(1)

    # Ask the user what file to use as a cover text
    cover_text = input('Cover text file? ')
    with open(cover_text, 'r') as input_file:
        lines = input_file.readlines()

    # Make sure the cover text is long enough to store the secret message
    # (one line per character, plus a header)
    num_lines = len(lines)
    if (num_lines < len(secret_message) + 1):
        print('Cover file is too short to store message')
        exit(1)

    # Encode the length of the secret message as a binary code,
    # then convert it to whitespace
    secret_message_length = len(secret_message)
    length_code = f'{secret_message_length:b}'
    length_whitespace = code_to_whitespace(length_code)

    # Place the encoded length at the end of the first file line
    lines[0] = add_whitespace_at_end(lines[0], length_whitespace)

    # For every letter in the secret message, do these steps.
    for (pos, letter) in enumerate(secret_message):
        # Use the translation table to convert it to a binary code (0s and 1s)
        code = letter_to_code[letter]

        # Turn that binary code into whitespace
        whitespace = code_to_whitespace(code)

        # Place the generated whitespace at the end of the line
        # (add 1 to pos, since position 0 in lines is taken by header)
        lines[pos + 1] = add_whitespace_at_end(lines[pos + 1], whitespace)

    # Ask the user what file to save the result to
    output_file = input('Output text file? ')
    with open(output_file, 'w') as output_file:
        output_file.writelines(lines)

# run the program when the file is run
encode_message()
