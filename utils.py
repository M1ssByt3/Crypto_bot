import time
import os

def bot_says(message: str, delay=1):
    time.sleep(delay)
    print(f"CryptoBuddy 🤖: {message}")

def typing_effect(text: str, delay: float = 0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Make output colorfull for terminal
def color_text(text, color="green"):
    colors = {
        "green": "\033[92m",
        "red": "\033[91m",
        "blue": "\033[94m",
        "reset": "\033[0m"
    }
    return f"{colors.get(color, '')}{text}{colors['reset']}"


def confirm_exit():
    response = input("Are you sure you want to exit? (y/n): ").strip().lower()
    return response == "y"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def bot_intro():
    print("👋 Hello! I'm CryptoBuddy, your AI-powered crypto sidekick.")
    print("Ask about trending cryptos, eco-friendliness, long-term picks, or live prices.")
    print("⚠️ Disclaimer: This is for educational purposes. Always do your own research!\n")
