# What is this "steganography" stuff?

## Steganography

Before I go much further, I want to share a quick definition.

**Steganography** is the hiding of secret text within some medium, and there are lots of different choices for what medium to use.

??? info "Greek roots"

    **steganos (covered) + -graphia (description)**

    from [Etymonline](https://www.etymonline.com/word/steganography)

One common medium is photos, because they can have a lot of redundant data which makes them easy to hide information in without changing the appearance.

Steganography cares about three attributes: [^1]

1. **Capacity**: How efficiently can secret data be stored?
2. **Security**: How hard is it to detect and decode?
3. **Robustness**: How well can it resist being messed with?

Improving one often hurts others, so it's a balancing act.

## Text steganography

In text steganography, our chosen medium is written (almost always typed) text.

!!! note "Vocab"

    The **secret message** (or secret) is the text we want to hide.

    The **cover text** (or cover) is the text we use to obscure the secret message.

There are three major approaches to hiding the secret message within text steganography: [^2]

1. **Format**: Subtly reformat the cover text (i.e. changing character positions).
2. **Linguistic**: Use knowledge about language to modify the cover text's word usage.
3. **Statistical**: Generate a misleading cover text from scratch, based on real data.

??? info "Text creation vs. modification"

    Both **Format-based** and **Linguistic** approaches require an existing text to act as the cover text,
    and they encode information into that text by changing it in hard-to-detect ways.

    The **Statistical** approach generates a new text based on known language patterns.
    One recognized way of doing so is with a Markov Chain, and there has also been research into using Gen AI for this purpose.

Text steganography is an **interesting challenge** in terms of the three attributes steganography values,
because human brains are really good at noticing inconsistencies in text.

## This tutorial

In this tutorial, we're going to explore a very simple format-based steganographic technique that adds spaces to the document in order to store the secret message.

!!! warning

    The technique I am going to teach you is not effective at keeping secrets.
    In fact, it is extremely low in terms of Capacity, Security, and Robustness.

    However, it's **simple enough to understand** and that's worth more to me. We're here to learn!

In the next step, we'll [plan and understand the design](planning-design.md).

[^1]: Majeed et al. (2021). A Review on Text Steganography Techniques. In *Mathematics*, <https://www.mdpi.com/2227-7390/9/21/2829>.
[^2]: Majeed et al. (2021).
