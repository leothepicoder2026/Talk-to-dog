#!/usr/bin/env python3
"""
Talk to Dog - Interactive ASCII art dog conversation
Select different preset options and get responses from a friendly ASCII dog!
"""

def display_menu():
    """Display the menu of preset options."""
    print("\n" + "="*50)
    print("         WELCOME TO TALK TO DOG! 🐕")
    print("="*50)
    print("\nChoose what to say to the dog:\n")
    print("1. Say Hello")
    print("2. Ask How It's Doing")
    print("3. Tell a Joke")
    print("4. Compliment the Dog")
    print("5. Ask for Advice")
    print("6. Pet the Dog")
    print("0. Exit")
    print("\n" + "="*50)


def dog_says_hello():
    """Dog greets the user."""
    dog_art = """
    / \\__
   (    @\\___
   /         O
  /   (_____/
 /_____/   U
"""
    speech = "WOOF! Hey there, buddy! 🐕"
    display_dog(dog_art, speech)


def dog_asks_doing():
    """Dog asks how you're doing."""
    dog_art = """
     ^__^
     (oo)\\_______
     (__)\\_______) /~~/
        ||----w |
        ||     ||
"""
    speech = "I'm doing pawsome! How about you? 🐕"
    display_dog(dog_art, speech)


def dog_joke():
    """Dog tells a joke."""
    dog_art = """
        / \\__
       (    @\\___
       /         O
      /   (_____/
     /_____/   U
"""
    speech = "Why did the dog go to the bank?\nTo get his BARKING account! 😄"
    display_dog(dog_art, speech)


def dog_compliment():
    """Dog receives a compliment."""
    dog_art = """
       / \\__
      (    @\\___
      /   O    O
     /   (_____/
    /_____/   U
"""
    speech = "Aww, you're making me blush! 🥰\nYou're pretty great yourself!"
    display_dog(dog_art, speech)


def dog_advice():
    """Dog gives advice."""
    dog_art = """
     ^__^
     (oo)\\_______
     (__)\\_______) /~~/
        ||----w |
        ||     ||
"""
    speech = "My life advice: Eat well, play hard,\nand always give your friends love! 🐕"
    display_dog(dog_art, speech)


def dog_pet():
    """Dog gets petted."""
    dog_art = """
       / \\__
      (    @\\___
      /         O
     /   (_____/
    /_____/   U
"""
    speech = "N/A"
    display_dog(dog_art)


def display_dog(ascii_art, speech):
    """Display the dog ASCII art with a speech bubble."""
    print("\n" + "="*50)
    
    # Display dog
    print(ascii_art)
    
    # Display speech bubble
    lines = speech.split('\n')
    max_length = max(len(line) for line in lines)
    
    print("\n    " + "┌" + "─" * (max_length + 2) + "┐")
    for line in lines:
        print(f"    │ {line:<{max_length}} │")
    print("    " + "└" + "─" * (max_length + 2) + "┘")
    print("    " + " \\ ")
    print("     \\")
    
    print("\n" + "="*50)


def main():
    """Main program loop."""
    options = {
        '1': ('Say Hello', dog_says_hello),
        '2': ('Ask How It\'s Doing', dog_asks_doing),
        '3': ('Tell a Joke', dog_joke),
        '4': ('Compliment the Dog', dog_compliment),
        '5': ('Ask for Advice', dog_advice),
        '6': ('Pet The Dog', dog_pet),
    }
    
    while True:
        display_menu()
        choice = input("Enter your choice (0-6): ").strip()
        
        if choice == '0':
            print("\nThanks for talking to the dog! Goodbye! 👋\n")
            break
        elif choice in options:
            option_name, option_func = options[choice]
            print(f"\n✓ You chose: {option_name}")
            option_func()
        else:
            print("\n❌ Invalid choice! Please enter a number between 0 and 6.")
        
        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
