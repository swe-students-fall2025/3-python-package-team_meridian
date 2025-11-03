"""
In Python packages, this file called __main__.py is run when the package is run
directly from command line, as opposed to importing it into another program.
"""

from pyfortunecookie.core import get_fortune, get_lucky_number, get_color, get_tarot_reading, get_fortune_by_choice, get_lucky_day

def main():
    print("🥠 Welcome to PyFortune Cookie!\n")
    print(f"Today's fortune: {get_fortune()}")
    print(f"Your lucky number: {get_lucky_number()}")
    print(f"Your lucky color: {get_color()}")
    
    # Get lucky day and format it nicely
    lucky_day = get_lucky_day()
    print(f"Your lucky day: {lucky_day['day']} - {lucky_day['message']}")
    
    print("\n🔮 Tarot Reading:")
    print(get_tarot_reading())

    # Interactive personalized fortune
    print("\n🎴 Personalized Fortune (by your choices):")

    # Ask user for their choices
    elements = ["fire", "water", "earth", "air"]
    times = ["dawn", "noon", "dusk", "midnight"]
    symbols = ["star", "moon", "sun", "cloud"]

    while True:
        choice1 = input(f"Choose an element {elements}: ").strip().lower()
        if choice1 in elements:
            break
        print(f"Invalid choice. Please choose one of {elements}.")

    while True:
        choice2 = input(f"Choose a time {times}: ").strip().lower()
        if choice2 in times:
            break
        print(f"Invalid choice. Please choose one of {times}.")

    while True:
        choice3 = input(f"Choose a symbol {symbols}: ").strip().lower()
        if choice3 in symbols:
            break
        print(f"Invalid choice. Please choose one of {symbols}.")

    # Generate personalized fortune
    choice_result = get_fortune_by_choice(choice1, choice2, choice3)

    # Print results
    print("\n✨ Your Personalized Fortune ✨")
    print(f"Element: {choice_result['element']}")
    print(f"Time: {choice_result['time']}")
    print(f"Symbol: {choice_result['symbol']}")
    print(f"Combination: {choice_result['combination']}")
    print(f"Fortune: {choice_result['fortune']}")
    print(f"Lucky Number: {choice_result['lucky_number']}")
    print(f"Lucky Color: {choice_result['lucky_color']}")


if __name__ == "__main__":
    main()
