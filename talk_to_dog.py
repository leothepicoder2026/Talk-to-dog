#!/usr/bin/env python3
"""
Talk to Dog - Interactive ASCII art dog conversation
Select different preset options and get responses from a friendly ASCII dog!
"""

import os
import re
import sys
import tempfile
import urllib.request
from urllib.error import URLError, HTTPError

__version__ = "2.0.0"
REMOTE_SCRIPT_URL = "https://raw.githubusercontent.com/leothepicoder2026/Talk-to-dog/main/talk_to_dog.py"

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
    speech = "The dog did not say anything, but it looks very happy! 🥰"
    display_dog(dog_art, speech)


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


def parse_version(value):
    """Parse a version string like '1.2.3' into a tuple of integers."""
    return tuple(int(part) for part in value.strip().split('.') if part.isdigit())


def fetch_remote_script():
    """Download the remote script content from the configured URL."""
    try:
        with urllib.request.urlopen(REMOTE_SCRIPT_URL, timeout=10) as response:
            encoding = response.headers.get_content_charset() or "utf-8"
            return response.read().decode(encoding)
    except (HTTPError, URLError, ValueError) as exc:
        print(f"⚠️  Update check failed: {exc}")
        return None


def get_remote_version():
    """Read the version from the remote script."""
    content = fetch_remote_script()
    if content is None:
        return None

    match = re.search(r'^__version__\s*=\s*["\']([^"\']+)["\']', content, re.MULTILINE)
    return match.group(1).strip() if match else None


def save_update(content):
    """Save the fetched remote script to the current file path."""
    current_file = os.path.abspath(__file__)
    backup_path = current_file + ".bak"

    try:
        with open(backup_path, "w", encoding="utf-8") as backup_file:
            with open(current_file, "r", encoding="utf-8") as current:
                backup_file.write(current.read())

        with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8", dir=os.path.dirname(current_file)) as temp_file:
            temp_file.write(content)
            temp_path = temp_file.name

        os.replace(temp_path, current_file)
        print(f"✅ Update applied successfully. A backup was saved to: {backup_path}")
        return True
    except OSError as exc:
        print(f"❌ Failed to save update: {exc}")
        return False


def check_for_update():
    """Check if a newer version exists and offer to apply it."""
    print("🔎 Checking for updates...")
    remote_version = get_remote_version()
    if not remote_version:
        print("No update information available.")
        return

    try:
        if parse_version(remote_version) > parse_version(__version__):
            print(f"A new version is available: {remote_version} (installed: {__version__})")
            answer = input("Would you like to update now? [Y/n]: ").strip().lower()
            if answer in ("", "y", "yes"):
                remote_script = fetch_remote_script()
                if remote_script and save_update(remote_script):
                    print("Please run the script again to use the new version.")
                    sys.exit(0)
            else:
                print("Update skipped. You can check again later.")
        else:
            print(f"You're already running the latest version: {__version__}")
    except ValueError:
        print("Unable to compare versions. Update check canceled.")


def main():
    """Main program loop."""
    check_for_update()
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
