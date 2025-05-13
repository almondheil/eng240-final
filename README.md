# ENG-240 Final

Final project for Professor Simpson's ENG-240 class, Fall 2025.

# Repo structure

- My finished code is in `code` dir.

- The tutorial has its build configuration in `mkdocs.yml`, and its contents in `tutorial` dir.

- `LICENSE` is the MIT license over this software and this tutorial

- `requirements.txt` contains the dependencies for building the tutorial with python

# Running the code

To encode:

```bash
python code/encode.py
```

To decode:

```bash
python code/decode.py
```

# Building the tutorial pages

First, install dependencies

```bash
pip install -r requirements.txt
```

Then you can just go for it:

```bash
mkdocs serve  # run live, open in your browser
```

or

```bash
mkdocs build  # create files you can use wherever
```
