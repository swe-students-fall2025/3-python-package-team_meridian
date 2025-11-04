[![CI / CD](https://github.com/swe-students-fall2025/3-python-package-team_meridian/actions/workflows/build.yaml/badge.svg)](https://github.com/swe-students-fall2025/3-python-package-team_meridian/actions/workflows/build.yaml)
PyPI: https://pypi.org/project/PyFortuneCookie/

# PyFortuneCookie

PyFortuneCookie is a Python package that generates your **daily fortune cookie** — complete with a lucky number, color and day!  

## Team Members
[Sina Liu](https://github.com/SinaL0123)
[Aayan Mathur](https://github.com/aayanmathur)
[Daniel Huang](https://github.com/DplayerXAX)
[Togawa Saki](https://github.com/TogawaSaki0214)
[Abdul Mendahawi](https://github.com/amendahawi)

---

## Installation

Clone or download this repository, then install it locally (in editable mode):

```bash
pipenv install
pipenv run pip install -e .
````

If you don’t have **pipenv**, install it first:

```bash
pip install pipenv
```

---

## Run Locally (for teammates)

If you want to run this project on your own machine (e.g., to test or modify it):

```bash
# 1️⃣ Clone the repository
git clone https://github.com/swe-students-fall2025/3-python-package-team_meridian.git

cd pyfortunecookie

# 2️⃣ Install pipenv and dependencies
pip install pipenv
pipenv install

# 3️⃣ Enter the virtual environment
pipenv shell

# 4️⃣ Run the tests (optional, to verify everything works)
pipenv run pytest

# 5️⃣ Run the package
python3 -m pyfortunecookie
```

💡 You can exit the environment anytime with:

```bash
exit
```

---

## Usage

You can run PyFortuneCookie either from the **command line** or directly as a **Python module**.

### ▶️ Option 1: Run as command-line tool

```bash
pipenv run pyfortunecookie
```

### ▶️ Option 2: Run as a Python module

```bash
pipenv run python -m pyfortunecookie
```

### ▶️ Option 3: Import and use functions in your code

```python
from pyfortunecookie.core import get_fortune, get_lucky_number, get_color

print(get_fortune())
print(get_lucky_number())
print(get_color())
```

---

## Example Output

When you run the command:

```bash
pipenv run pyfortunecookie
```

You might see something like this:

```
🥠 Welcome to PyFortune Cookie!

Today's fortune: Your curiosity will lead to something amazing today ✨
Your lucky number: 37
Your lucky color: Lavender
```

Each time you run it, you’ll get a new random fortune, number, and color!

---

## Features

| Function             | Description                      |
| -------------------- | -------------------------------- |
| `get_fortune()`      | Returns a random fortune message |
| `get_lucky_number()` | Generates a random lucky number  |
| `get_color()`        | Returns a random lucky color     |

---

## Run Tests

Make sure everything works properly with:

```bash
pipenv run pytest
```

All tests are located inside the `tests/` directory.

---

## Project Structure

```
pyfortunecookie/
├── src/
│   └── pyfortunecookie/
│       ├── __init__.py
│       ├── __main__.py
│       └── core.py
├── tests/
│   └── test_core.py
├── Pipfile
├── pyproject.toml
└── README.md
```