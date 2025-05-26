import speech_recognition as sr
import os
import webbrowser
import pyttsx3
from datetime import datetime
import wikipedia
import random
import requests
import pyjokes

# API keys (replace with your actual keys)
***REMOVED***
***REMOVED***

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Speaks the given text aloud."""
    engine.say(text)
    engine.runAndWait()

def greet():
    """Greets user based on time of day."""
    hour = int(datetime.now().hour)
    if 5 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 17:
        speak("Good afternoon!")
    elif 17 <= hour < 21:
        speak("Good evening!")
    else:
        speak("Good night!")
    speak("I am Maverick, your assistant. How may I help you!")

def takecommand():
    """Listens to user's voice and converts to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I am Listening...")
        print("Listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 2, 6)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception:
        speak("I couldn't understand, can you please say it more clearly")
        return "none"
    return query

def get_weather(city_name):
    """Fetches current weather for the given city."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city_name}&appid={weather_api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()

    if response.status_code == 200 and "main" in data:
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return f"The current temperature in {city_name} is {temperature}°C with {description}."
    else:
        return "City not found or an error occurred while fetching the weather data."

def get_news():
    """Fetches top 5 news headlines."""
    base_url = "https://newsapi.org/v2/top-headlines"
    country = "us"
    complete_url = f"{base_url}?country={country}&apiKey={news_api_key}"
    response = requests.get(complete_url)
    data = response.json()

    print("News API response:", data)  # DEBUG

    if data.get("status") == "ok" and data.get("articles"):
        articles = data["articles"][:5]
        return [article["title"] for article in articles]
    else:
        return []  # Always return list

def tell_joke():
    """Returns a random joke."""
    return pyjokes.get_joke()

# MAIN LOOP
if __name__ == '__main__':
    speak("Initializing Maverick....")
    greet()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace('wikipedia', '')
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception:
                speak("Sorry, I couldn't find that on Wikipedia.")

        elif 'youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")

        elif 'google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'stackoverflow' in query:
            speak("Opening Stack Overflow")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            speak("Playing music for you")
            music_dir = "C:\\music"
            songs = [s for s in os.listdir(music_dir) if s.endswith(('.mp3', '.wav'))]
            if songs:
                random_song = random.choice(songs)
                os.startfile(os.path.join(music_dir, random_song))
                speak(f"Now playing {random_song}")
            else:
                speak("No songs found in the music folder.")

        elif 'linkedin' in query:
            speak("Opening LinkedIn")
            webbrowser.open("linkedin.com")

        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")

        elif 'weather' in query:
            speak("For which city?")
            city = takecommand().lower()
            if city and city != "none":
                weather_info = get_weather(city)
                print(weather_info)
                speak(weather_info)
            else:
                speak("Sorry, I didn't catch the city name. Please try again.")

        elif 'news' in query:
            speak("Fetching latest news headlines.")
            headlines = get_news()
            if headlines:
                for headline in headlines:
                    print(headline)
                    speak(headline)
            else:
                speak("Sorry, I am unable to fetch news at the moment.")

        elif 'joke' in query:
            joke = tell_joke()
            print(joke)
            speak(joke)

        elif 'open' in query:
            speak("Opening it")
            query = query.replace("open", "").strip()
            if query:
                speak(f"Opening {query}")
                os.system('start ' + query)
            else:
                speak("Can't open it")

        elif 'exit' in query or 'stop' in query or 'quit' in query:
            speak("Goodbye! Have a nice day.")
            break
