# eng240 final

final project for Professor Simpson's ENG-240 class, fall 2025.

# repo structure

- my finished code is in `code` dir.

- the tutorial has its build configuration in `mkdocs.yml`, and its contents in `tutorial` dir.

- `LICENSE` is the MIT license over this software and this tutorial

- `requirements.txt` contains the dependencies for building the docs with python

# running the code

to encode:

```bash
python code/encode.py
```

to decode:

```bash
python code/decode.py
```

# building the tutorial pages

first install dependencies

```bash
pip install -r requirements.txt
```

then you can just go for it

```bash
mkdocs serve
```

or

```bash
mkdocs build
```
