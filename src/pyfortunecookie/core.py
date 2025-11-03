from os import nice
import random
from typing import Optional

_TAROT = {
    "The Fool": "New beginnings, take a leap of faith.",
    "The Magician": "Your skills will shape reality.",
    "The High Priestess": "Trust your intuition.",
    "The Empress": "Abundance grows where you nurture.",
    "The Emperor": "Structure brings stability.",
    "The Hierophant": "Tradition and guidance shape your path.",
    "The Lovers": "Meaningful connections influence your decisions.",
    "The Chariot": "Focus and willpower drive victory.",
    "Strength": "Quiet courage overcomes fear.",
    "The Hermit": "Solitude reveals deeper answers.",
    "Wheel of Fortune": "Things will shift—be adaptable.",
    "Justice": "Balance and fairness will restore order.",
    "The Hanged Man": "Change perspective to see clearly.",
    "Death": "A chapter ends so something new can begin.",
    "Temperance": "Moderation creates harmony.",
    "The Devil": "Beware of illusions and temptation.",
    "The Tower": "Old structures must fall before renewal.",
    "The Star": "Hope quietly returns.",
    "The Moon": "The truth is hidden beneath uncertainty.",
    "The Sun": "Joy, clarity, and success await.",
    "Judgement": "Your past transforms into resolution.",
    "The World": "Completion brings fulfillment."
}

_TAROT_GROUP = {
    "seeking_change": [
        "The Fool", "The Tower", "Death", "The Chariot", "Judgement", "Wheel of Fortune"
    ],
    "needing_clarity": [
        "The High Priestess", "The Moon", "The Hermit", "The Hanged Man", "Justice"
    ],
    "needing_support": [
        "Strength", "Temperance", "The Star", "The Sun", "The Empress", "The World"
    ]
}
_FORTUNES = [
    "Today is a good day to start small.",
    "A pleasant surprise is waiting for you.",
    "Your code will compile on the first try.",
    "Help others and luck will help you.",
    "Take a short walk; ideas will follow.",
    "A cup of coffee will solve half your problems. ☕",
    "You will soon discover a hidden strength. 💪",
    "Your curiosity is your superpower. 🔍"
]

_PALETTES = {
    "soft": ["peach", "mint", "lavender", "sky", "lemon"],
    "bold": ["crimson", "indigo", "emerald", "amber", "teal"],
    "mono": ["black", "white", "gray"]
}

_RUNES = {
    "Fehu": "Wealth, new beginnings, prosperity.",
    "Uruz": "Strength and endurance.",
    "Thurisaz": "Conflict, challenge, or protection.",
    "Ansuz": "Wisdom, communication, divine inspiration.",
    "Raidho": "Journey, movement, or progress.",
    "Kenaz": "Creativity, revelation, transformation.",
    "Gebo": "Gift, partnership, generosity.",
    "Wunjo": "Joy, harmony, well-being."
}

def get_fortune(rng: Optional[random.Random] = None) -> str:
    """Return a random fortune sentence."""
    rng = rng or random
    return rng.choice(_FORTUNES)

def get_lucky_number(seed: Optional[int] = None, min_value: int = 1, max_value: int = 99) -> int:
    """Return a lucky number (optionally deterministic if seed provided)."""
    if min_value > max_value:
        raise ValueError("min_value must be <= max_value")
    rng = random.Random(seed) if seed is not None else random
    return rng.randint(min_value, max_value)

def get_color(palette: str = "soft", rng: Optional[random.Random] = None) -> str:
    """Return a lucky color from the selected palette."""
    if palette not in _PALETTES:
        raise ValueError(f"Unknown palette '{palette}'. Valid: {', '.join(_PALETTES)}")
    rng = rng or random
    return rng.choice(_PALETTES[palette])

def get_tarot_reading(intent: Optional[str] = None, rng: Optional[random.Random] = None) -> str:
    """
    Return a tarot reading with slight bias based on intent.
    Valid intents: seeking_change, needing_clarity, needing_support
    """
    rng = rng or random

    if intent in _TAROT_GROUP:
        if rng.random() < 0.7:
            pool = _TAROT_GROUP[intent]
        else:
            pool = [c for c in _TAROT.keys() if c not in _TAROT_GROUP[intent]]
    else:
        pool = list(_TAROT.keys())

    card = rng.choice(pool)
    meaning = _TAROT[card]
    return f"{card}: {meaning}"

def get_rune_reading(n=3, rng: Optional[random.Random] = None) -> str:
    """Return a rune reading with n runes."""
    if n < 1:
        raise ValueError("n must be at least 1")
    rng = rng or random
    selected_runes = rng.sample(list(_RUNES.keys()), k=n)
    readings = [f"{rune}: {_RUNES[rune]}" for rune in selected_runes]
    return readings

