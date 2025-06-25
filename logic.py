# logic.py

import nltk
from nltk.tokenize import word_tokenize
from pycoingecko import CoinGeckoAPI
from crypto_data import crypto_db
from utils import bot_says, color_text, typing_effect

# Download NLTK tokenizer (if not already downloaded)
nltk.download('punkt', quiet=True)

# Initialize CoinGecko API
cg = CoinGeckoAPI()

# Mapping crypto names to CoinGecko IDs
coin_ids = {
    "Bitcoin": "bitcoin",
    "Ethereum": "ethereum",
    "Cardano": "cardano"
}


# 🔍 Extract keywords from user input
def extract_keywords(text):
    return set(word_tokenize(text.lower()))


# 🔗 Fetch live price from CoinGecko
def get_live_price(coin):
    coin_id = coin_ids.get(coin)
    if coin_id:
        try:
            typing_effect(f"Fetching {coin} price... ⌛")
            price = cg.get_price(ids=coin_id, vs_currencies='usd')
            if price and coin_id in price:
                return price[coin_id]['usd']
        except Exception:
            return None
    return None


# 🧠 Chatbot logic
def handle_query(user_query):
    keywords = extract_keywords(user_query)

    # 🌱 Sustainability query
    if {"sustainable", "eco", "green"} & keywords:
        coin = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        bot_says(color_text(f"🌱 Consider {coin} — it's highly sustainable and energy-efficient!", "green"))

    # 📈 Trending coins query
    elif {"trending", "up", "rising"} & keywords:
        trending = [
            coin for coin, data in crypto_db.items()
            if data["price_trend"] == "rising"
        ]
        if trending:
            bot_says(color_text(f"📈 Currently trending coins: {', '.join(trending)}", "blue"))
        else:
            bot_says(color_text("😕 No coins are trending upwards right now.", "red"))

    # 🚀 Long-term investment advice
    elif {"growth", "long", "invest", "safe"} & keywords:
        recommended = None
        for coin, data in crypto_db.items():
            if (
                data["price_trend"] == "rising"
                and data["energy_use"] == "low"
                and data["sustainability_score"] >= 0.7
            ):
                recommended = coin
                break

        if recommended:
            bot_says(color_text(f"🚀 {recommended} looks great for long-term, sustainable investing!", "green"))
        else:
            bot_says(color_text("🤷 No perfect match, but Cardano looks promising!", "blue"))

    # 💰 Current price query
    elif {"price", "current", "usd", "value", "cost"} & keywords:
        for coin in crypto_db.keys():
            price = get_live_price(coin)
            if price:
                bot_says(color_text(f"💰 {coin}'s current price: ${price}", "green"))
            else:
                bot_says(color_text(f"❌ Couldn't fetch the price for {coin}.", "red"))

    # ❓ Unrecognized query
    else:
        bot_says(color_text(
            "🤖 Sorry, I didn't catch that.\n"
            "You can ask about:\n"
            "- 🌱 Sustainability (e.g., 'Which coin is sustainable?')\n"
            "- 📈 Trending (e.g., 'What coins are trending?')\n"
            "- 🚀 Long-term investments (e.g., 'Which coin is good for growth?')\n"
            "- 💰 Current prices (e.g., 'What's Bitcoin's current price?')",
            "blue"
        ))
