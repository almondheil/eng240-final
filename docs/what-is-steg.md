# What is steganography?

Before I go much further, I want to share a quick definition.

**Steganography** is the hiding of secret text within some medium, and there are a lot of ways to interpret "medium."

One common medium is photos, because they can have a lot of redundant data which makes them easy to hide information in without changing the appearance.

??? info "Greek roots"

    **steganos (covered) + -graphia (description)**

    from [Etymonline](https://www.etymonline.com/word/steganography)

Steganography cares about three attributes: [^1]

1. **Capacity**: How efficiently can secret data be stored?
2. **Security**: How hard is it to detect and decode?
3. **Robustness**: How well can it resist being messed with?

Improving one often hurts others, so it's a balancing act.

# Text steganography

In text steganography, our chosen medium is **written text**. (almost always typed)

There are three major approaches to text steganography: [^1]

1. **Format**: Change the format of text (e.g. character positions) so subtly they won't be noticed.
2. **Linguistic**: Use knowledge about language properties to disguise changes that encode data.
3. **Statistical**: Generate a text from scratch to hide information, based on real data.

??? info "Existing or new text?"

    Both **Format-based** and **Linguistic** approaches require an existing text to act as the cover text,
    and they encode information into that text by changing it in sneaky ways.

    The **Statistical** approach generates a new text based on known language patterns.
    One recognized way of doing so is with a Markov Chain, and there has also been research into using Gen AI for this purpose.

Text steganography is an **interesting challenge** in terms of the three attributes steganography values,
because human brains are really good at noticing inconsistencies in text.

# In this tutorial

In this tutorial, we're going to explore a very simple format-based steganographic technique that adds spaces to the document in order to store the secret message.

!!! warning

    The technique I am going to teach you is not good, don't use it if you need secrecy.

    It's terrible in terms of Capacity, Security, and Robustness, but unlike the latest research 
    it's **simple enough** to get your head around in a reasonable amount of time.

In the next step, we'll [plan and understand the design.](planning-design.md)

[^1]: Majeed et al. (2021). A Review on Text Steganography Techniques. In *Mathematics*, <https://www.mdpi.com/2227-7390/9/21/2829>.

