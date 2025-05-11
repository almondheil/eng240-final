# Planning our design

## Origin of design

The design we'll be implementing today is based on the [SNOW project](https://darkside.com.au/snow/) by Matthew Kwan.

It hides whitespace (spaces and tabs) at the end of lines, making it harder to notice the secret message. We'll use a mix of spaces
and tabs to encode this message, making it a binary code.

??? info annotate "Binary codes"

    === "Explanation"

        The term binary comes up a lot in computer science, but it just means base 2.

        Our normal counting system is called base 10 because we have 10 symbols for numbers (0-9),
        so "binary" means we have 2 symbols for numbers.

        - For readability, I'll write these symbols as 0 and 1.
        - To turn them into hidden whitespace, we'll made 0s into tabs and 1s into spaces.

    === "Counting and carrying"

        Just like in base 10, when we get to the highest number in one digit can hold, we add a new digit to the left. (1)

        Here's a comparison counting up to the number ten. Notice the carrying in the Base 2 column! (2)

        | Base 10 | Base 2 |
        | ------- | ------ |
        | 0 | 0 |
        | 1 | 1 |
        | 2 | 10 |
        | 3 | 11 |
        | 4 | 100 |
        | 5 | 101 |
        | 6 | 110 |
        | 7 | 111 |
        | 8 | 1000 |
        | 9 | 1001 |
        | 10| 1010 |

1.  For instance, 999 + 1 = 1000.
2.  One example is going from 7 to 8, where we carry three digits.

## Encoding and decoding

In order to turn letters into these binary codes, we'll need to decide on a mapping from letters to binary codes. This will be called our **translation table.**

We can decide on the mapping of our translation table later, for now let's look at an overview of how the process works.

!!! example "Encoding"

    Each letter in the secret message will be assigned to one line of the cover text, in order.

    For every letter in the secret message, we will do these steps:

    1. Use the translation table to convert it to a binary code (0s and 1s).

    2. Turn that binary code into whitespace, by replacing all the 0s with tabs and all the 1s with spaces.

    3. Place the generated whitespace at the end of the line.

Once the message is hidden, we also need a way to read it afterwards by decoding it. It uses the reverse of each step.

!!! example "Decoding"

    For every line that has a secret hidden letter, do these steps:

    1. Find the hidden whitespace.

    2. Turn the whitespace into a binary code, by replacing all the tabs with 0s and all the spaces with 1s.

    3. Use the translation table to convert the binary code to a letter.

    Once we're done, we will have found the whole message!

## Detecting hidden letters

However, there's one thing that I've left out.

!!! question

    When decoding, how do we know which lines have a hidden letter?

I encourage you to think about the question and try to find an answer, then expand the box below when you are ready to see
what direction I am choosing to go in.

??? tip annotate "My answer"

    === "Design choice"

        I wish I could hear what you thought of, but this is a static medium. I can think of two ways to figure it out:

        1. Look for lines that have whitespace at the end, and assume they are secret letters.
        2. Store the number of lines with letters at the top of the file, also in a hidden format.

        In this tutorial, I'm going to follow the second option because it gives a useful learning opportunity.

    === "Steps to do that"

        To store the length of the message, we can use binary codes again!

        Instead of mapping letters to sequences, here we'll convert our length from base 10 into base 2. (1)

        Once we turn that code into a sequence of whitespace, we can place it on the first line of the file as a header that
        tells us how many hidden letters to expect.

1.  For instance, the base-10 number 12 turns into the binary code 1100.

Now that we've established the general flow, let's [write some code for encoding](encoding.md)!
