# library to match text patterns
import re

# reverse of our letter to code association from the previous file, since we are going the other direction
code_to_letter = {
    '0'     : 'a', 
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
    '11010' : ' ', 
    '11011' : '.', 
    '11100' : ',', 
    '11101' : '!', 
    '11110' : '?', 
    '11111' : ':', 
}


def spaces_to_code(spaces):
    """
    Turn a sequence of spaces into a binary code.

    Input:
        spaces: Sequence of spaces
    Output:
        A binary code, like '1011'
    """

    # start with empty string
    code_string = ''

    # for each character in the space string, turn it into a number.
    for space in spaces:
        if space == '\t':
            code_string += '0'
        if space == ' ':
            code_string += '1'

    # return the finished string
    return code_string

def extract_spaces(line):
    """
    Extract the hidden spaces from the end of a line and return them.

    Input:
        line: Line to extract from
    Output:
        A string containing the spaces if it was found, or None if no string was found.
    """

    # get the main content of the line with no ending newline
    line_content = line.rstrip('\r\n')

    # use a regular expression to get the tabs and spaces.
    # these are ugly to read, but what this does is select a sequence of tabs and spaces (of any length) at the end of the line.
    search = re.search("([ \t]+)$", line_content)

    # if nothing was found, return that there is nothing to extract.
    # otherwise, return the sequence of spaces and tabs that was matched
    if search is None:
        return None
    else:
        return search.group(1)


def decode_message():
    input_file_name = input('File to try and decode? ')

    # Attempt to open the file to read its lines
    try:
        with open(input_file_name, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print('Could not find file to open.')
        exit(1)
    except PermissionError:
        print('Cannot open file due to permissions.')
        exit(1)

    # Check for the header showing the length on the first line
    header_spaces = extract_spaces(lines[0])
    if header_spaces is None:
        print('Did not detect a header at the top of the file, cannot decode.')
        exit(1)

    # Convert the spaces into a code
    header_code = spaces_to_code(header_spaces)

    # Convert the header code into a number using base 2 (binary)
    header_number = int(header_code, 2)

    # go through every line after the header up to the message length, and decode the letters
    decoded_message = ''
    for index in range(header_number):
        # extract the spaces from that line. if there are no spaces, print out an error and fail.
        line_spaces = extract_spaces(lines[index + 1])
        if line_spaces is None:
            # when printing error add 2 to index. one for the header offset, and one for the file lines starting counting at 1 not 0.
            print(f'No spaces could be decoded on line {index + 2}, cannot decode.')
            exit(1)
    
        # turn those spaces into a binary code, and look up that code in the association table to find its letter.
        line_code = spaces_to_code(line_spaces)
        decoded_letter = code_to_letter[line_code]

        # add the letter to the end of our message
        decoded_message += decoded_letter

    # print the final result
    print(decoded_message)

# when our program runs, decode a message
decode_message()
