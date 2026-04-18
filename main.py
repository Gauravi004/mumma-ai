from flask import Flask, request
import requests
import google.generativeai as genai

app = Flask(__name__)

def speak(text):
    return f"AI says: {text}"

def processText(text):
    text = text.lower()

    if "youtube" in text:
        return "https://www.youtube.com"

    elif "github" in text:
        return "https://github.com"

    elif "google" in text:
        return "https://www.google.com"

    elif "news" in text:
        try:
            r = requests.get(
                "https://newsapi.org/v2/top-headlines?country=us&apiKey=6376c2c9190f4415835f92c5058e1658"
            )
            news = r.json()
            articles = news.get('articles', [])

            if articles:
                article = articles[0]
                return article.get('title', 'No news available')
            else:
                return "No news available"

        except Exception:
            return "Error fetching news"

    else:
        return "Mumma AI is running 🚀"


# 🔹 Web route
@app.route("/")
def home():
    return "Mumma AI is running successfully 🚀"

@app.route("/ask")
def ask():
    query = request.args.get("q", "")
    return processText(query)


# 🔹 Main
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
