## Starting to code

Now, we'll start creating the code behind our steganography method.

Start off by creating a new Python file called `encode.py`.

??? question "Where can I write and run Python code?"

    === "CoCalc"

        CoCalc can work if you took ENG-240 and you still have access to your Grinnell account.

        Access it at <https://cocalc.com/projects>.

    === "Google Colab"

        If you have a Google account, you can use Colab and create a notebook there.

        You can find it at <https://colab.research.google.com>.

        Colab uses a different format than we're used to from CoCalc, where rather than having a code file you write code in cells.
        There is a [tutorial on Colab](https://colab.research.google.com/notebooks/basic_features_overview.ipynb) if you are interested.

    === "Your computer"
        
        If you have an easy time installing and running new software, you can install Python directly.

        You can start at <https://www.python.org/downloads/>.

## Scaffolding

We'll start off by planning out the steps our progam must take, from the lowest level upwards.

!!! failure "TODO: DO I DEFINE ENCODE AND DECODE EVER?"

First, we'll define a function with almost no code and just comments saying what we need to do.

``` py title="encode.py"
def encode_message():
    # Ask the user what their secret message will be

    # Ask the user what file to use as a cover text

    # Encode the length of the secret message as a binary code,
    # then convert it to whitespace

    # Place the encoded length at the end of the first file line

    # For every letter in the secret message, do these steps.
    for TODO_FILL_IN_LOOP:
        # Use the translation table to convert it to a binary code (0s and 1s)

        # Turn that binary code into whitespace

        # Place the generated whitespace at the end of the line

    # Ask the user what file to save the result to

# run the program when the file is run
encode_message()
```

!!! warning

    This code will not yet be able to run, it's just a skeleton of our program.

Now, let's go through and start filling in things below those comments. I'll make changes in small batches, and highlight which lines changed.

First, we can use the `input()` function to ask for user input where it is relevant.

``` py title="encode.py - User input" hl_lines="3 6 21"
def encode_message():
    # Ask the user what their secret message will be
    secret_message = input('Secret message? ')

    # Ask the user what file to use as a cover text
    cover_text = input('Cover text file? ')

    # Encode the length of the secret message as a binary code,
    # then convert it to whitespace

    # Place the encoded length at the end of the first file line

    # For every letter in the secret message, do these steps.
    for TODO_FILL_IN_LOOP:
        # Use the translation table to convert it to a binary code (0s and 1s)

        # Turn that binary code into whitespace

        # Place the generated whitespace at the end of the line

    # Ask the user what file to save the result to
    output_file = input('Output text file? ')

# run the program when the file is run
encode_message()
```

Next, we can add logic to open the files the user specifies and handle errors.

``` py title="encode.py - File opening" hl_lines="7-8 24-25"
def encode_message():
    # Ask the user what their secret message will be
    secret_message = input('Secret message? ')

    # Ask the user what file to use as a cover text
    cover_text = input('Cover text file? ')
    with open(cover_text, 'r') as input_file:
        lines = input_file.readlines()

    # Encode the length of the secret message as a binary code,
    # then convert it to whitespace

    # Place the encoded length at the end of the first file line

    # For every letter in the secret message, do these steps.
    for TODO_FILL_IN_LOOP:
        # Use the translation table to convert it to a binary code (0s and 1s)

        # Turn that binary code into whitespace

        # Place the generated whitespace at the end of the line

    # Ask the user what file to save the result to
    output_file = input('Output text file? ')
    with open(output_file, 'w') as output_file:
        output_file.writelines(lines)

# run the program when the file is run
encode_message()
```

!!! note

    We should technically handle errors if the file fails to open for any reason,
    but I don't want to add the extra complexity. We never handled these errors in
    our code from class, either.


## Mapping characters
### Allowed characters

There are existing systems that map characters onto binary codes, but they aren't quite
right for us because they can handle a lot of characters but also take up more space.

We want to use the fewest characters possible,
because that will let us keep our steganography slightly more hidden.

!!! question

    What characters should we allow in the secret message?

For this tutorial, the minimal characters we want to support is the 26 lowercase letters.

!!! tip 

    But we can store more than just that without wasting space!

    The binary code for 25 (the 26th number, counting from 0) is `11001`, which doesn't fill all the possible positions with `1`s.

    We can actually fit up to 32 total options into five positions.

We can add a **dictionary** to our code to store the mapping of our 32 characters.

```py title="encode.py - letter_to_code dictionary"
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

# (the rest of your code below)
```

??? question "What's a dictionary?"

    In Python, a dictionary is an abstraction that lets us map keys (characters) to values (binary codes).

    This dictionary lets us look up an allowed letter and gives us the code in 0s and 1s.

    ```py title="Example"
    letter_to_code('w')
    # -> '10110'
    ```
### Binary to whitespace

Now we have an easy way to get the binary codes for our letters, but we
need to turn them into spaces and tabs before we can hide them in the cover file.

We can make a function to do this:

```py title="encode.py - Code to whitespace function"
letter_to_code = {
    # (hidden)
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

# (the rest of your code below)
```

!!! example

    Now, we can call this function on a code to convert it!

    ```py
    code = letter_to_code(f)          # '101'
    space = code_to_whitespace(code)  # '\t \t'
    ```

    Notice how the `1`s become `\t`, and the `0` becomes a space.

### Check secret text

Finally, now that we have a limited set of allowed characters we should
check that the user's secret code doesn't have any characters we don't allow.

We can do this with a simple check.

```py title="encode.py - Checking secret text" hl_lines="5-11"
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

    # (rest of code hidden)
```

## Length header

Now, we can start calculating how to hide the code in the file.

For our first step, we will calculate the length of the message and store it
on the first line of the file.

### Encode length

To store the length of the message, we must convert it into a binary code that stores its value.
Then, we can turn that code into whitespace.

!!! warning

    This is different from how we use binary codes in the `letter_to_code` dictionary.

    Its goal is to turn specific letters into unique codes, but we want to turn a number into
    the code that represents it (like how the binary code `1010` represents the number 10).

We could write a function to turn a number into the binary code that represents it, but I don't
think that is as important to understanding this process.
Instead, we'll use a feature of Python to do the conversion.

```py title="encode.py - Encode length header" hl_lines="9-13"
def encode_message():
    # (code before hidden)

    # Ask the user what file to use as a cover text
    cover_text = input('Cover text file? ')
    with open(cover_text, 'r') as input_file:
        lines = input_file.readlines()

    # Encode the length of the secret message as a binary code,
    # then convert it to whitespace
    secret_message_length = len(secret_message)
    length_code = f'{secret_message_length:b}'
    length_whitespace = code_to_whitespace(length_code)

    # Place the encoded length at the end of the first file line
    
    # (code after hidden)
```

### Store in file

We'll need to store whitespace at the end of the line to hide the header.

This is an operation we will do a lot, so it's worth making a function at the top of the file.

```py title="encode.py - Add whitespace at end function" hl_lines="8-13"
letter_to_code = {
    # (hidden)
}

def code_to_whitespace(code):
    # (hidden)

def add_whitespace_at_end(line, whitespace):
    # get the start of the line, but remove extra space characters from the end
    line_content = line.rstrip('\r\n \t')

    # add our whitespace at the end, along with a new newline
    return line_content + whitespace + '\n'
```

With that function defined, we can use it to store the header.

```py title="encode.py - Store length header" hl_lines="16"
def encode_message():
    # (code before hidden)

    # Ask the user what file to use as a cover text
    cover_text = input('Cover text file? ')
    with open(cover_text, 'r') as input_file:
        lines = input_file.readlines()

    # Encode the length of the secret message as a binary code,
    # then convert it to whitespace
    secret_message_length = len(secret_message)
    length_code = f'{secret_message_length:b}'
    length_whitespace = code_to_whitespace(length_code)

    # Place the encoded length at the end of the first file line
    lines[0] = add_whitespace_at_end(lines[0], length_whitespace)
    
    # (code after hidden)
```

!!! note

    We modify the `lines` array that we read from the cover file.

    When we write to the output file at the end of the function, our
    changes will be included with that.

## Storing secret message

Now, we need to take the secret message and store it in the file.
Each letter will get one line, but we will start at `lines[1]` because `lines[0]` is already used by the header.

Yay, we can finally replace in the part marked `TODO_FILL_IN_LOOP`!

```py title="encode.py - Store secret message" hl_lines="8 10 13 16-17"
def encode_message():
    # (code above hidden)

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

    # (code below hidden)
```

??? question "What is that "enumerate" thing?"

    `enumerate` lets us get not only the items of a string, but also their positions.

    We need to know the position so we can find the corresponding position in the lines list.
    
### Avoiding an error

!!! failure "Error" 

    But wait! There's an important thing we forgot to check!

    We used the line as position `pos + 1`, but if the secret message is longer than the number of lines in the cover file this code will crash.

To avoid that error, we can check the length before we try to store the message.

```py title="encode.py - Check cover file length" hl_lines="9-14"
def encode_message():
    # (code before hidden)

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

    # (code after hidden)
```

## Running the code

Now that we've written this code file, it should be ready to run!

To do that, we'll need a cover text. You can choose any text file, but I'll also provide one.

!!! note "File downloads"

    === "Cover file"

        [Download `lighthouses.txt`](static/lighthouses.txt){:download="lighthouses.txt"}

        This is an excerpt from [*Lighthouses: Their history and romance*](https://www.gutenberg.org/ebooks/76041) by William John Hardy on Project Gutenberg.

    === "Code file"

        [Download `encode.py`](static/encode.py){:download="encode.py"}

        I hope you were following along, but I'll provide my finished code for this part if you need it.

Save the file to the same directory as your code, and then run it with `python encode.py`.

Here's what to respond to each prompt:

1. Secret message: A short message of your choice, using the allowed characters
2. Cover text: `lighthouses.txt`, or the name of the text file you choose.
3. Output file: `hidden.txt`

When it's done, you can open `hidden.txt`. It'll look just like before, unless you select the lines and reveal the extra spaces.

You probably can't read the secret message anymore, right? Don't worry, in the next step we'll make a program to [decode the secret](decoding.md)!
