# take a valid letter, and turn it into a binary code
letter_to_code = {
    'a':  '0'    
    'b':  '1'    
    'c':  '10'   
    'd':  '11'   
    'e':  '100'  
    'f':  '101'  
    'g':  '110'  
    'h':  '111'  
    'i':  '1000' 
    'j':  '1001' 
    'k':  '1010' 
    'l':  '1011' 
    'm':  '1100' 
    'n':  '1101' 
    'o':  '1110' 
    'p':  '1111' 
    'q':  '10000'
    'r':  '10001'
    's':  '10010'
    't':  '10011'
    'u':  '10100'
    'v':  '10101'
    'w':  '10110'
    'x':  '10111'
    'y':  '11000'
    'z':  '11001'
    ' ':  '11010'
    '.':  '11011'
    ',':  '11100'
    '!':  '11101'
    '?':  '11110'
    ':':  '11111'
}


def code_to_spaces(code):
    """
    Turn the readable code for a letter (e.g. 11100) into spaces and tabs for encoding.

    Input:
        code: The readable binary code for a letter.
    Output:
        A string that has a sequence of spaces and tabs, according to that code.
    """

    # start off with an empty string
    space_string = ''
    
    # build up pieces of the space_string by adding on letter-by-letter.
    for letter in code:
        # for t, add a tab character to the string. for s, add a space character.
        if letter == '0':
            space_string += '\t'
        if letter == '1':
            space_string += ' '

    # return the finished string when we are done
    return space_string


def add_spaces(line, spaces)
    """
    Add secret spaces at the end of a line.

    Input:
        lines: Array of file lines
        index: Index to change
        spaces: Sequence of spaces to add
    Output:
        Nothing. It modifies the lines array.
    """
    # get the line, but take off the \r and/or \n characters that make a newline
    line_content = line.rstrip('\r\n')

    # add our secret spaces, and then re-add the newline character at the end
    return line_content + spaces + '\n'

def encode_message():
    """
    Encode a message.
    """

    # Prompt the user for their secret message
    message_input = input('Secret message to encode? ')

    # Take the message the user gave as input, and modify it to match our encoding dictionary.
    secret_message = ''
    for char in message_input.lower():
        # convert all characters to their lowercase versions
        char = char.lower();

        # ignore characters that we can't encode, but warn the user they will be ignored
        if not char in letter_to_code
            print(f'  "{char}" cannot be in message, it will be ignored')

        # if the letter does not break rules, add it
        else:
            secret_message += char

    # Next, prompt the user to enter their cover file to use
    cover_file_name = input('Cover file to hide the secret message? ')

    # Attempt to read the file, and print an error if we couldn't.
    try:
        with open(cover_file_name, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print('Could not find file to open.')
        exit(1)
    except PermissionError:
        print('Cannot open file due to permissions.')
        exit(1)
        
    # Make sure the number of lines in the file is enough to store the secret message.
    # If the file is too short, print an error message.
    # We use message_length + 1 because one line is dedicated to the header
    n_lines = len(lines)
    message_length = len(secret_message)
    if (n_lines < message_length + 1):
        print(f'That file is only {n_lines} long, it must be at least {message_length} to store that message.');
        exit(1)


    # Conver the length of the message to a binary number
    header_code = f'{message_length:b}'

    # Turn that binary number into a sequence of spaces, so we can put it at the end of the first line
    header_spaces = code_to_spaces(header_code)
    lines[0] = add_spaces(lines[0], header_spaces)

    # For each message character, add the code of that character to the end of its line.
    for index, secret_char in enumerate(secret_message):
        # turn the secret char into spaces
        secret_char_code = letter_to_code[secret_char]
        secret_char_spaces = code_to_spaces(secret_char_code)

        # put that at the end of the corresponding line
        lines[index + 1] = add_spaces(lines[index + 1], secret_char_spaces)

    # Ask the user what file they want to output to
    print('Successfully encoded message!')
    output_file_name = input('File to save output? ')
    
    # Attempt to output to that file
    try:
        with open(output_file_name, 'w') as file:
            file.writelines(lines)
    except PermissionError:
        print('Cannot open file due to permissions.')
        exit(1)


# encode a message when the program runs
encode_message()
