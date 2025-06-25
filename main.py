# main.py
from utils import bot_says
from logic import handle_query

def start_bot():
    print("Hello! I'm CryptoBuddy, your AI-powered crypto sidekick.")
    print("Ask me about trending cryptos, eco-friendly coins, long-term investments, or current prices.")
    print("Disclaimer: For educational purposes only. Always DYOR.\n")

    while True:
        user_input = input("You: ").strip().lower()
        if user_input in ["exit", "quit", "bye"]:
            bot_says("Alright! Stay smart, and see you next time 🚀")
            break
        handle_query(user_input)

if __name__ == "__main__":
    start_bot()
