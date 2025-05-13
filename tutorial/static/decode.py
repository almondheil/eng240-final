import re

code_to_letter = {
    '0'     : 'a',  # letters
    '1'     : 'b', 
    '10'    : 'c', 
    '11'    : 'd', 
    '100'   : 'e', 
    '101'   : 'f', 
    '110'   : 'g', 
    '111'   : 'h', 
    '1000'  : 'i', 
    '1001'  : 'j', 
    '1010'  : 'k', 
    '1011'  : 'l', 
    '1100'  : 'm', 
    '1101'  : 'n', 
    '1110'  : 'o', 
    '1111'  : 'p', 
    '10000' : 'q', 
    '10001' : 'r', 
    '10010' : 's', 
    '10011' : 't', 
    '10100' : 'u', 
    '10101' : 'v', 
    '10110' : 'w', 
    '10111' : 'x', 
    '11000' : 'y', 
    '11001' : 'z', 
    '11010' : ',',  # punctuation
    '11011' : '.', 
    '11100' : '!', 
    '11101' : '?', 
    '11110' : '-', 
    '11111' : ' '   # space
}

def whitespace_to_code(whitespace):
    # Use whitespace to generate a string of code
    code = ''
    for character in whitespace:
        # spaces -> 0s, tabs -> 1s
        if (character == ' '):
            code += '0'
        else:
            code += '1'

    # Return the finished code
    return code

def extract_whitespace(line):
    # Get the main content of the line with no ending newline
    line_content = line.rstrip('\r\n')

    # Search for our regular expression to get tabs and spaces from the end of the line.
    search = re.search("([ \t]+)$", line_content)

    # If nothing was found return None, otherwise return the whitespace that got matched.
    if search is None:
        return None
    else:
        return search.group(1)

def decode_message():
    # Ask the user what file to decode
    stego_text = input('Stego text to decode? ')
    with open(stego_text, 'r') as input_file:
        lines = input_file.readlines()

    # Read the header from the top of the file
    # and convert it to a binary code
    header_whitespace = extract_whitespace(lines[0])
    header_code = whitespace_to_code(header_whitespace)

    # Determine what number that code represents
    secret_message_length = int(header_code, 2)
    print(header_code)
    print(f'secret_message_length is {secret_message_length}')

    # For every line that has a secret letter, do these steps.
    decoded_message = ''
    for pos in range(secret_message_length):
        # Extract the spaces from the end of the line
        line_whitespace = extract_whitespace(lines[pos + 1])

        # Convert the spaces into a binary code
        line_code = whitespace_to_code(line_whitespace)

        # Convert the binary code into a letter
        letter = code_to_letter[line_code]
        decoded_message += letter

    # Print the decoded message so the user can see it
    print('Message:', decoded_message)

# run the program when the file is run
decode_message()
