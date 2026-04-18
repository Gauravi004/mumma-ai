import webbrowser
import requests
import google.generativeai as genai

# Simple speak function (CI-friendly)
def speak(text):
    print("AI says:", text)


def processText(text):
    text = text.lower()

    if "youtube" in text:
        speak("Opening YouTube")
        print("URL: https://www.youtube.com")

    elif "github" in text:
        speak("Opening GitHub")
        print("URL: https://github.com")

    elif "facebook" in text:
        speak("Opening Facebook")
        print("URL: https://www.facebook.com")

    elif "twitter" in text:
        speak("Opening Twitter")
        print("URL: https://twitter.com")

    elif "instagram" in text:
        speak("Opening Instagram")
        print("URL: https://www.instagram.com")

    elif "linkedin" in text:
        speak("Opening LinkedIn")
        print("URL: https://www.linkedin.com")

    elif "whatsapp" in text:
        speak("Opening WhatsApp")
        print("URL: https://web.whatsapp.com")

    elif "gmail" in text:
        speak("Opening Gmail")
        print("URL: https://mail.google.com")

    elif "google" in text:
        speak("Opening Google")
        print("URL: https://www.google.com")

    elif text.startswith("play"):
        speak("Playing song (demo mode)")

    elif "news" in text:
        try:
            r = requests.get(
                "https://newsapi.org/v2/top-headlines?country=us&apiKey=6376c2c9190f4415835f92c5058e1658"
            )
            news = r.json()
            articles = news.get('articles', [])

            if articles:
                article = articles[0]
                speak("Title: " + article.get('title', 'No title'))
                speak("Description: " + article.get('description', 'No description'))
            else:
                speak("No news available")

        except Exception as e:
            speak("Error fetching news")
            print("Error:", e)

    elif "bye" in text or "exit" in text or "stop" in text:
        speak("Bye bye! Take care!")

    else:
        try:
            genai.configure(api_key="YOUR_API_KEY_HERE")  # optional
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(text)
            speak(response.text.strip())
        except Exception:
            speak("AI response not available in demo mode")


# Test mode (for Jenkins & Docker)
if __name__ == "__main__":
    print("Running in CI test mode...")

    test_commands = [
        "youtube",
        "github",
        "news",
        "google",
        "play song",
        "hello"
    ]

    for cmd in test_commands:
        print(f"\nProcessing: {cmd}")
        processText(cmd)

    print("\nAll test commands executed successfully.")
