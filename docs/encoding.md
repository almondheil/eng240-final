## Starting to code

Now, we'll start creating the code behind our steganography method.

Start off by creating a new Python file called `encode.py`.

??? question "Where can I run Python code?"

    There are a few ways to run Python code, depending on what you can access.

    1. If you took the class and still have access to your Grinnell account, you can use [CoCalc](https://cocalc.com/projects) like we did then.

        You can use the "blank handout for testing python" handout Professor Simpson created for us.

    2. If you have a Google account, you can use [Google Colab](https://colab.research.google.com) and create a notebook there.

        Google has a [tutorial on using Colab](https://colab.research.google.com/notebooks/basic_features_overview.ipynb)
        if you would find that helpful, you can read up to the start of the "Working with python" section and skip the rest.

    3. If you have an easy time installing and running new software, you can [install Python directly](https://www.python.org/downloads/) on your computer.

## Bottom-up approach

We'll start off by planning out the steps our progam must take, from the lowest level upwards.

!!! failure "TODO: DO I DEFINE ENCODE AND DECODE EVER?"

First, we'll define a function with almost no code and just comments saying what we need to do.

``` py title="encode.py"
def encode_message():
    # Ask the user what their secret message will be

    # Ask the user what file to use as a cover text

    # Encode the length of the secret message as a binary code, then convert it to whitespace

    # Place the encoded length at the end of the first file line

    # For every letter in the secret message, do these steps.
    for TODO_FILL_IN_LOOP:
        # Use the translation table to convert it to a binary code (0s and 1s)

        # Turn that binary code into whitespace

        # Place the generated whitespace at the end of the line

    # Ask the user what file to save the result to
```

!!! warning

    This code will not yet be able to run, it's just a skeleton of our program.

Now, let's go through and start filling in things below those comments. I'll make changes in small batches, and highlight which lines changed.

First, we can use the `input()` function to ask for user input where it is relevant.

``` py title="encode.py - user input" hl_lines="3 6 21"
def encode_message():
    # Ask the user what their secret message will be
    secret_message = input('Secret message? ')

    # Ask the user what file to use as a cover text
    cover_text = input('Cover text file? ')

    # Encode the length of the secret message as a binary code, then convert it to whitespace

    # Place the encoded length at the end of the first file line

    # For every letter in the secret message, do these steps.
    for TODO_FILL_IN_LOOP:
        # Use the translation table to convert it to a binary code (0s and 1s)

        # Turn that binary code into whitespace

        # Place the generated whitespace at the end of the line

    # Ask the user what file to save the result to
    output_file = input('Output text file? ')
```

Next, we can add logic to open the files the user specifies and handle errors.

``` py title="encode.py - file opening" hl_lines="7-8 24-25"
def encode_message():
    # Ask the user what their secret message will be
    secret_message = input('Secret message? ')

    # Ask the user what file to use as a cover text
    cover_text = input('Cover text file? ')
    with open(cover_text, 'r') as input:
        lines = input.readlines()

    # Encode the length of the secret message as a binary code, then convert it to whitespace

    # Place the encoded length at the end of the first file line

    # For every letter in the secret message, do these steps.
    for TODO_FILL_IN_LOOP:
        # Use the translation table to convert it to a binary code (0s and 1s)

        # Turn that binary code into whitespace

        # Place the generated whitespace at the end of the line

    # Ask the user what file to save the result to
    output_file = input('Output text file? ')
    with open(output_file, 'w') as output:
        output.writelines(lines)
```

!!! note

    We should technically handle errors if the file fails to open for any reason,
    but I don't want to add the extra complexity. We never handled these errors in
    our code from class, either.


