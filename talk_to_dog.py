#!/usr/bin/env python3
"""
Talk to Dog - Interactive ASCII art dog conversation
Switched from a command-line interface to a tkinter GUI.
"""

import os
import re
import sys
import json
import tempfile
import urllib.request
from urllib.error import URLError, HTTPError

try:
    import tkinter as tk
    from tkinter import messagebox, font
except ImportError:
    tk = None
    messagebox = None
    font = None

__version__ = "4.0.0"
REMOTE_SCRIPT_URL = "https://raw.githubusercontent.com/leothepicoder2026/Talk-to-dog/main/talk_to_dog.py"
GITHUB_RELEASES_API_URL = "https://api.github.com/repos/leothepicoder2026/Talk-to-dog/releases/latest"

GUI_OUTPUT = None


def display_menu():
    """Display the menu of preset options."""
    print("\n" + "=" * 50)
    print("         WELCOME TO TALK TO DOG! 🐕")
    print("=" * 50)
    print("\nChoose what to say to the dog:\n")
    print("1. Say Hello")
    print("2. Ask How It's Doing")
    print("3. Tell a Joke")
    print("4. Compliment the Dog")
    print("5. Ask for Advice")
    print("6. Pet the Dog")
    print("7. Ask About Favorite Food")
    print("8. Play Fetch")
    print("9. Ask to Do a Trick")
    print("10. Ask About Dreams")
    print("11. Tell the Dog You Love It")
    print("12. Ask the Dog to Sing")
    print("13. Play Hide and Seek")
    print("14. Ask About Friends")
    print("15. Give a Treat")
    print("0. Exit")
    print("\n" + "=" * 50)


def show_response(ascii_art, speech, effect=None):
    """Display the dog response either in GUI or in the console fallback."""
    if GUI_OUTPUT:
        display_response_gui(ascii_art, speech)
    else:
        display_dog(ascii_art, speech)


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
    show_response(dog_art, speech)


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
    show_response(dog_art, speech)


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
    show_response(dog_art, speech)


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
    show_response(dog_art, speech)


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
    show_response(dog_art, speech)


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
    show_response(dog_art, speech)


def dog_favorite_food():
    """Dog talks about its favorite food."""
    dog_art = """
     ^__^
     (oo)\\_______
     (__)\\_______) /~~/
        ||----w |
        ||     ||
"""
    speech = "My favorite food? Bones and treats!\nWhat's yours? 🦴"
    show_response(dog_art, speech)


def dog_play_fetch():
    """Dog plays fetch."""
    dog_art = """
        / \\__
       (    @\\___
       /         O
      /   (_____/
     /_____/   U
"""
    speech = "Let's play fetch! Throw the ball!\nI'm ready to run! 🏃‍♂️🐕"
    show_response(dog_art, speech)


def dog_do_trick():
    """Dog does a trick."""
    dog_art = """
       / \\__
      (    @\\___
      /   O    O
     /   (_____/
    /_____/   U
"""
    speech = "Watch this! *rolls over*\nDid I do good? 🐕"
    show_response(dog_art, speech, effect="pitch")


def dog_dreams():
    """Dog talks about its dreams."""
    dog_art = """
     ^__^
     (oo)\\_______
     (__)\\_______) /~~/
        ||----w |
        ||     ||
"""
    speech = "I dream about chasing squirrels\nand endless belly rubs! 🌙🐕"
    show_response(dog_art, speech, effect="soft")


def dog_love():
    """Dog receives love."""
    dog_art = """
       / \\__
      (    @\\___
      /         O
     /   (_____/
    /_____/   U
"""
    speech = "I love you too! You're my best friend! ❤️🐕"
    show_response(dog_art, speech, effect="heart")


def dog_sing():
    """Dog sings a song."""
    dog_art = """
        / \\__
       (    @\\___
       /   O    O
      /   (_____/
     /_____/   U
"""
    speech = "🎵 Woof woof, bark bark,\nI love to sing in the park! 🎵"
    show_response(dog_art, speech, effect="melody")


def dog_hide_seek():
    """Dog plays hide and seek."""
    dog_art = """
     ^__^
     (oo)\\_______
     (__)\\_______) /~~/
        ||----w |
        ||     ||
"""
    speech = "Ready or not, here I come!\n*searches around* 🐕🔍"
    show_response(dog_art, speech, effect="sneak")


def dog_friends():
    """Dog talks about its friends."""
    dog_art = """
       / \\__
      (    @\\___
      /         O
     /   (_____/
    /_____/   U
"""
    speech = "My friends are the best!\nCats, birds, and you! 🐱🐦"
    show_response(dog_art, speech, effect="happy")


def dog_treat():
    """Dog gets a treat."""
    dog_art = """
        / \\__
       (    @\\___
       /   O    O
      /   (_____/
     /_____/   U
"""
    speech = "Yummy treat! Thank you!\n*munch munch* 🍖"
    show_response(dog_art, speech, effect="chime")


def display_dog(ascii_art, speech):
    """Display the dog ASCII art with a speech bubble."""
    print("\n" + "=" * 50)

    # Display dog
    print(ascii_art)

    # Display speech bubble
    lines = speech.split('\n')
    max_length = max(len(line) for line in lines)

    print("\n    " + "┌" + "─" * (max_length + 2) + "┐")
    for line in lines:
        print(f"    │ {line:<{max_length}} │")
    print("    " + "└" + "─" * (max_length + 2) + "┘")
    print("    " + " \\")
    print("     \\")

    print("\n" + "=" * 50)


def display_response_gui(ascii_art, speech):
    """Display the dog response in the GUI text widget."""
    if not GUI_OUTPUT:
        return

    GUI_OUTPUT.config(state='normal')
    GUI_OUTPUT.delete('1.0', tk.END)

    lines = speech.split('\n')
    max_length = max(len(line) for line in lines)
    bubble_lines = ["    " + "┌" + "─" * (max_length + 2) + "┐"]
    for line in lines:
        bubble_lines.append(f"    │ {line:<{max_length}} │")
    bubble_lines.append("    " + "└" + "─" * (max_length + 2) + "┘")
    bubble_lines.append("    \\")
    bubble_lines.append("     \\")

    GUI_OUTPUT.insert(tk.END, ascii_art + "\n")
    GUI_OUTPUT.insert(tk.END, "\n" + "\n".join(bubble_lines))
    GUI_OUTPUT.config(state='disabled')


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
        if messagebox:
            messagebox.showwarning("Update Check Failed", f"⚠️  Update check failed: {exc}")
        else:
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
        if messagebox:
            messagebox.showinfo("Update Applied", f"✅ Update applied successfully. A backup was saved to: {backup_path}")
        else:
            print(f"✅ Update applied successfully. A backup was saved to: {backup_path}")
        return True
    except OSError as exc:
        if messagebox:
            messagebox.showerror("Save Update Failed", f"❌ Failed to save update: {exc}")
        else:
            print(f"❌ Failed to save update: {exc}")
        return False


def check_for_update(parent=None):
    """Check if a newer version exists and offer to apply it."""
    remote_version = get_remote_version()
    if not remote_version:
        return

    try:
        if parse_version(remote_version) > parse_version(__version__):
            message = f"A new version is available: {remote_version} (installed: {__version__}).\nWould you like to update now?"
            if messagebox and messagebox.askyesno("Update Available", message, parent=parent):
                remote_script = fetch_remote_script()
                if remote_script and save_update(remote_script):
                    if messagebox:
                        messagebox.showinfo("Restart Required", "Please restart the application to use the new version.", parent=parent)
                    sys.exit(0)
            else:
                if messagebox:
                    messagebox.showinfo("Update Skipped", "Update skipped. You can check again later.", parent=parent)
        else:
            if messagebox:
                messagebox.showinfo("No Update Available", f"You're already running the latest version: {__version__}", parent=parent)
            else:
                print(f"You're already running the latest version: {__version__}")
    except ValueError:
        if messagebox:
            messagebox.showerror("Update Error", "Unable to compare versions. Update check canceled.", parent=parent)
        else:
            print("Unable to compare versions. Update check canceled.")


def fetch_latest_release_notes():
    """Download the latest release notes from the GitHub releases API."""
    try:
        request = urllib.request.Request(
            GITHUB_RELEASES_API_URL,
            headers={"User-Agent": "Talk-to-Dog-App"}
        )
        with urllib.request.urlopen(request, timeout=10) as response:
            encoding = response.headers.get_content_charset() or "utf-8"
            data = response.read().decode(encoding)
            release_info = json.loads(data)
            return release_info.get("body", "No release notes are available.")
    except (HTTPError, URLError, ValueError, json.JSONDecodeError) as exc:
        if messagebox:
            messagebox.showwarning("Changelog Fetch Failed", f"⚠️  Unable to fetch the latest changelog: {exc}")
        else:
            print(f"⚠️  Unable to fetch the latest changelog: {exc}")
        return None


def show_latest_changelog(parent=None):
    """Show the latest release description from GitHub in a dialog."""
    notes = fetch_latest_release_notes()
    if notes is None:
        return

    if messagebox:
        messagebox.showinfo("Latest Changelog", notes, parent=parent)
    else:
        print("\nLatest Changelog:\n")
        print(notes)


def build_gui():
    """Build and run the tkinter GUI."""
    global GUI_OUTPUT

    if tk is None:
        print("Tkinter is not available. Falling back to the command-line interface.")
        return main_cli()

    root = tk.Tk()
    root.title("Talk to Dog")
    root.geometry("980x620")
    root.minsize(860, 520)

    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)

    button_frame = tk.Frame(root, width=260, padx=10, pady=10)
    button_frame.grid(row=0, column=0, sticky="ns")
    button_frame.grid_propagate(False)
    button_frame.grid_columnconfigure(0, weight=1)

    output_frame = tk.Frame(root, padx=10, pady=10)
    output_frame.grid(row=0, column=1, sticky="nsew")
    output_frame.grid_rowconfigure(0, weight=1)
    output_frame.grid_columnconfigure(0, weight=1)

    root.state('zoomed')

    GUI_OUTPUT = tk.Text(output_frame, wrap="none", state='disabled', bg="#f8f8f8", bd=2, relief='sunken')
    scrollbar = tk.Scrollbar(output_frame, orient="vertical", command=GUI_OUTPUT.yview)
    GUI_OUTPUT.configure(yscrollcommand=scrollbar.set)
    GUI_OUTPUT.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=1, sticky="ns")

    if font:
        mono_font = font.Font(family="Courier", size=11)
        GUI_OUTPUT.configure(font=mono_font)

    actions = [
        ("Say Hello", dog_says_hello),
        ("Ask How It's Doing", dog_asks_doing),
        ("Tell a Joke", dog_joke),
        ("Compliment the Dog", dog_compliment),
        ("Ask for Advice", dog_advice),
        ("Pet the Dog", dog_pet),
        ("Ask About Favorite Food", dog_favorite_food),
        ("Play Fetch", dog_play_fetch),
        ("Ask to Do a Trick", dog_do_trick),
        ("Ask About Dreams", dog_dreams),
        ("Tell the Dog You Love It", dog_love),
        ("Ask the Dog to Sing", dog_sing),
        ("Play Hide and Seek", dog_hide_seek),
        ("Ask About Friends", dog_friends),
        ("Give a Treat", dog_treat),
    ]

    for index, (label, action) in enumerate(actions):
        button = tk.Button(button_frame, text=label, command=action)
        button.grid(row=index, column=0, pady=4, sticky="ew")

    update_button = tk.Button(button_frame, text="Check for Updates", command=lambda: check_for_update(parent=root))
    update_button.grid(row=len(actions), column=0, pady=(20, 4), sticky="ew")

    changelog_button = tk.Button(button_frame, text="View Latest Changelog", command=lambda: show_latest_changelog(parent=root))
    changelog_button.grid(row=len(actions) + 1, column=0, pady=4, sticky="ew")

    exit_button = tk.Button(button_frame, text="Exit", command=root.quit)
    exit_button.grid(row=len(actions) + 2, column=0, pady=4, sticky="ew")

    welcome_art = """
    / \\__
   (    @\\___
   /         O
  /   (_____/
 /_____/   U
"""
    show_response(welcome_art, "Welcome to Talk to Dog! Choose a button to chat with your friendly pup.")

    root.after(100, lambda: check_for_update(parent=root))
    root.mainloop()


def main_cli():
    """Fallback command-line interface."""
    check_for_update()
    options = {
        '1': ('Say Hello', dog_says_hello),
        '2': ("Ask How It's Doing", dog_asks_doing),
        '3': ('Tell a Joke', dog_joke),
        '4': ('Compliment the Dog', dog_compliment),
        '5': ('Ask for Advice', dog_advice),
        '6': ('Pet The Dog', dog_pet),
        '7': ('Ask About Favorite Food', dog_favorite_food),
        '8': ('Play Fetch', dog_play_fetch),
        '9': ('Ask to Do a Trick', dog_do_trick),
        '10': ('Ask About Dreams', dog_dreams),
        '11': ('Tell the Dog You Love It', dog_love),
        '12': ('Ask the Dog to Sing', dog_sing),
        '13': ('Play Hide and Seek', dog_hide_seek),
        '14': ('Ask About Friends', dog_friends),
        '15': ('Give a Treat', dog_treat),
    }

    while True:
        display_menu()
        choice = input("Enter your choice (0-15): ").strip()

        if choice == '0':
            print("\nThanks for talking to the dog! Goodbye! 👋\n")
            break
        elif choice in options:
            option_name, option_func = options[choice]
            print(f"\n✓ You chose: {option_name}")
            option_func()
        else:
            print("\n❌ Invalid choice! Please enter a number between 0 and 15.")

        input("Press Enter to continue...")


def main():
    """Entry point for the application."""
    if tk is not None:
        build_gui()
    else:
        main_cli()


if __name__ == "__main__":
    main()
