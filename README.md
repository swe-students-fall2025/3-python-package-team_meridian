[![CI / CD](https://github.com/swe-students-fall2025/3-python-package-team_meridian/actions/workflows/build.yaml/badge.svg)](https://github.com/swe-students-fall2025/3-python-package-team_meridian/actions/workflows/build.yaml)

PyPI: [https://pypi.org/project/pyfortunecookie-teammeridian/](https://pypi.org/project/pyfortunecookie-teammeridian/

# PyFortuneCookie

PyFortuneCookie is a Python package that generates your **daily fortune cookie** — complete with a lucky number, color and day!  

## Team Members
[Sina Liu](https://github.com/SinaL0123)

[Aayan Mathur](https://github.com/aayanmathur)

[Daniel Huang](https://github.com/DplayerXAX)

[Haonan Cai](https://github.com/TogawaSaki0214)

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

### Welcome Screen
```

🥠 Welcome to PyFortune Cookie!

Select a category:

1. Zodiac & MBTI Summary
2. Tarot Reading
3. Personalized Fortune
4. Rune Reading
5. Lucky Day
   Enter 1 / 2 / 3 / 4 / 5:

```

### Category 1 – Zodiac & MBTI Summary
```

Enter your zodiac (e.g., Aries, Libra, Pisces): Libra
Enter your MBTI (e.g., INFP, ESTJ): INFP

🌙 Your Fortune Summary 🌙
Zodiac: Libra | MBTI: INFP
Fortune: Your curiosity is your superpower. 🔍 Let your imagination guide you!
Lucky Number: 42
Lucky Color: lavender
Lucky Day: Friday - A blessed day awaits you.

```

### Category 2 – Tarot Reading
```

🔮 Tarot Reading:
The Star: Hope quietly returns.

```

### Category 3 – Personalized Fortune
```

🎴 Personalized Fortune (by your choices):
Choose an element ['fire', 'water', 'earth', 'air']: fire
Choose a time ['dawn', 'noon', 'dusk', 'midnight']: dawn
Choose a symbol ['star', 'moon', 'sun', 'cloud']: star

✨ Your Personalized Fortune ✨
Element: fire
Time: dawn
Symbol: star
Combination: You are passionate and energetic, seeking new beginnings, guided by guidance and aspiration.
Fortune: 🔥 🌅 ⭐ Reach for the stars; they're closer than you think!

```

### Category 4 – Rune Reading
```

🔮 Rune Reading:

* Gebo: Gift, partnership, generosity.
* Ansuz: Wisdom, communication, divine inspiration.
* Wunjo: Joy, harmony, well-being.

```

### Category 5 – Lucky Day
```

☀️ Lucky Day:
Day: Tuesday - Your determination will pay off today.

```

### Exit
```

Would you like to choose another category? (y/n): n
🌟 Thank you for using PyFortune Cookie! Goodbye! 🌟

```

---

## Features

| Function | Description |
| ----------------------------- | -------------------------------------------------------------- |
| `get_zodiac_mbti_summary()` | Generates a complete fortune summary based on the user's Zodiac sign and MBTI type, including lucky number, color, day, and fortune message |
| `get_tarot_reading()` | Returns a tarot card reading with interpretation |
| `get_fortune_by_choice()` | Returns a personalized fortune based on user-selected element, time, and symbol |
| `get_rune_reading(n=None)` | Returns a rune reading with a random number (`n`) of runes and their meanings |
| `get_lucky_day()` | Returns a randomly selected lucky day and its symbolic meaning |



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
3-python-package-team_meridian/
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
