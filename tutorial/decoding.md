# Decoding

Now that we've implemented our encoding, we can start decoding those messages!

**Create a new file** called `decode.py`, and then we can start adding stuff to it.

## Scaffolding

To follow the same pattern as the previous chapter, let's make a scaffold for our decoding process.

!!! info "New Term"

    A **stego text** is a text that has a message hidden inside of it through steganographic processes.

I'll skip the intermediate steps this time, and just give the outline with user input and opening the file.

```py title="decode.py"
def decode_message():
    # Ask the user what file to decode
    stego_text = input('Stego text to decode? ')
    with open(stego_text, 'r') as input_file:
        lines = input_file.readlines()

    # Read the header from the top of the file
    # and convert it to a binary code

    # Determine what number that code represents

    # For every line that has a secret letter, do these steps.
    for TODO_FILL_IN_LOOP:
        # Extract the spaces from the end of the line

        # Convert the spaces into a binary code

        # Convert the binary code into a letter

    # Print the decoded message so the user can see it

# run the program when the file is run
decode_message()
```

As you can see, this program has the same general structure: we deal with the header first, then deal with each character in the secret message.

The big difference is how we handle the letters. Now we are going from whitespace to letters, so we must do all of our steps in the opposite order.

!!! note

    To make this possible, we'll develop functions that work in the opposite direction from the ones we made before.

    We'll go in the same order as our steps within the loop: first extracting, then converting to a binary code, then converting to a letter.

## Extracting whitespace

To extract the whitespace from the end of the line, we're going to use a regular expression.

??? question "What is a regular expression?"

    Regular expressions are built to help match patterns in text.

    They are a set of rules that tells the computer what patterns it is looking for, but there's lots of syntax that gets confusing
    because each "instruction" to the computer is only a single character of text.

    Once you've created a regular expression, you can use it to search a string for things that match its pattern.

Here's what I'm gonna do: I am going to show you a regular expression, it's gonna be ugly, and then you can check out an explanation if you want.

The expression is: `([ \t]+)$`.

??? question "How does that thing work?"

    Let's start reading at the center.

    1. "`[ \t]`" is a group, and that's why there are square brackets. The items inside the group are the space and tab characters, the ones we used to hide our secret message.

        This chunk reads in natural language as "match either of these characters."

    2. Then, we have `+`. This means "repeated one or more times," so the expression matches a sequence of one or more spaces and tabs.

    3. Next, we have the `()`. These mark the stuff inside as a group, which lets us extract the spaces and tabs later when we do the search.

    4. Finally, there's the `$`. This means "the end of the line," and it's what makes sure we only find spaces and tabs that are actually at the end where we put them--not in the middle.

Now that we have the regular expression, we can write a function that uses it to extract the whitespace.

Put this function, as well as the import statement, at the top of your file.

```py title="decode.py - Extracting whitespace"
import re

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

# (your other code below)
```

## Whitespace to code

Once the whitespace is extracted, we can turn it from a sequence of spaces and tabs
back into a binary code of 1s and 0s.

The function that does this looks very similar to the one we wrote before.

!!! tip

    Generally, we keep the `import` statements at the very top of the file before any functions or other definitions.

    I won't draw attention to it again and it won't break anything if you mess it up, it's just good style.

```py title="decode.py - Whitespace to code"
import re

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

# (the rest of your code below)
```

!!! note

    We are adding 0 and 1 to our code, but not the literal numbers. Just like before, this is combining strings together.

    `'1' + '1'` is `11`, not `2`.

## Code to letter

The final step is to make a reverse mapping from binary codes to letters. This will mirror the dictionary we made before, like the other steps.

```py title="decode.py - Code to letter"
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

# (the rest of your code below)
```

## Decoding the header

We've set up all the machinery we'll need, so now we can start filling out the blank sections in our scaffold for the program.

First, let's get the binary code of the header.

```py title="decode.py - Getting the header's code" hl_lines="11-12"
# (everything above hidden)

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

    # For every line that has a secret letter, do these steps.
    for TODO_FILL_IN_LOOP:
        # Extract the spaces from the end of the line

        # Convert the spaces into a binary code

        # Convert the binary code into a letter

    # Print the decoded message so the user can see it

# run the program when the file is run
decode_message()
```

To turn the header code into a number, we'll need to convert it from base 2 to base 10--the opposite of what we did before. Python also has a built-in way to do this.

```py title="decode.py - Converting header code to base 10" hl_lines="9"
# (hidden above)

    # Read the header from the top of the file
    # and convert it to a binary code
    header_whitespace = extract_whitespace(lines[0])
    header_code = whitespace_to_code(header_whitespace)

    # Determine what number that code represents
    secret_message_length = int(header_code, 2)

# (hidden below)
```

??? question "What is that function call?"

    When we call `int` on a string, Python will try to convert it into a number.

    Here's an example with the number 12.

    ```py title="Example"
    int('12')
    # -> 12 ✅
    ```

    The thing is, our number isn't in base 10--it's in base 2. That's what the second parameter controls. If we left this out, we'd get the wrong answer.

    For instance, in base 2 the number 7 is `111`.

    ```py title="Example"
    int('111')
    # -> 111 ❌

    int('111', 2)
    # -> 7 ✅
    ```

## Decoding secret letters

Knowing the value of the header also tells us how many lines have a secret letter on them, so now it's possible for us to fill in those parts of the loop.

Like in our `whitespace_to_code` function, we'll need a string that we add onto the end of to keep track of the decoded message as we go. Then, we can just call the functions that we've already defined to decode everything!

```py title="decode.py - Decoding secret letters" hl_lines="18-19 21 24 27-28 31"
# (everything above hidden)

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
```

## Running the code

Okay, we're all set! Now we can decode the stego file we created in the previous chapter.

!!! note "Code download"

    [Download `decode.py`](static/decode.py){:download="decode.py"}

    Like before, here's my finished code if you want it for any reason.

Save the file to the same directory as your code, and then run it with `python decode.py`.

When it asks you for a file, enter `hidden.txt` or whatever name you chose for the stego file before. It should spit out the secret message!

!!! info

    Feel free to play around with the code more. If you want, you could make it a little bug bounty! There are some
    known errors I left in for simplicity, and I bet you can find them!

If you're ready to go on, check out the little conclusion I wrote: [Step back.](step-back.md)
