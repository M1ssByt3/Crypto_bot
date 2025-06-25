# CryptoBudy Chatbot

* On task I create an interactive rule-based chatbot that analyzes cryptocurrency data and provides investment advice based on profitability (e.g., price trends) and sustainability (e.g., energy efficiency, project viability).
This project is designed for learning purposes, demonstrating:

🔗 API integration

🗣️ Conversational chatbot design

 # Core Functionalities:

✅ Check Trending Coins: currently trending based on price trends from the dataset.

✅ Get Sustainable Crypto Suggestions: eco-friendly coin based on energy usage and sustainability score.

✅ Long-Term Investment Suggestions:
Recommend coins that are not only trending but also energy-efficient and have high sustainability — great for long-term growth.

✅ Live Price Fetching:
Uses the CoinGecko API to fetch and display real-time prices for supported cryptocurrencies.

✅ Interactive Chat Loop:
Engages in a continuous conversation loop until the user decides to exit.

✅ Helpful Fallback Guidance:
If the chatbot doesn't understand a question, it offers a helpful menu of options.

✅ Typing Effect + Stylized Replies:
Simulates typing delays, emojis and colored outputs for a more interactive feel.

# Limitations
⚠️ Uses a static dataset for sustainability, market cap, and trends — not dynamically fetched.

⚠️ Keyword-based; doesn’t fully process natural language sentences or follow-up questions.

⚠️ No memory of prior conversations (no session-based context).

# Future Improvements
🧠 Add NLP support (e.g., spaCy or fuzzy matching).

# Set up

* nltk	Tokenizes user input to identify keywords.
* pycoingecko	Fetches real-time crypto prices via API.
* Virtual Env (venv)	Keeps project dependencies isolated from other Python projects.
* Libraries: Use if-else logic or ChatterBot (optional) for conversation flow.
* Data: Predefined crypto datasets (provided below).
