# main.py

from utils import bot_says, bot_intro, confirm_exit, clear_screen, typing_effect, color_text
from logic import handle_query

def start_bot():
    clear_screen()   # Clears the terminal for a clean start
    bot_intro()      # Prints the introduction message
    

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["exit", "quit", "bye"]:
            if confirm_exit():
                typing_effect("Exiting... See you next time 🚀")
                bot_says("Goodbye! Stay smart, stay safe in crypto! 🌟")
                break
            else:
                bot_says("No worries, let's keep going!")

        else:
            handle_query(user_input)   # Pass input to the chatbot logic


if __name__ == "__main__":
    start_bot()
