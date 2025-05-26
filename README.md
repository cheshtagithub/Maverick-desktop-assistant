🧠 Maverick - Voice Assistant
Maverick is a Python-based desktop voice assistant designed to help you with everyday tasks using voice commands. It can:
Answer questions using Wikipedia
Provide current weather updates
Fetch the latest news headlines
Tell jokes
Open websites like Google, YouTube, LinkedIn, and more
Play music from a local folder

🚀 Getting Started
Follow these steps to set up and run Maverick on your machine.

1. Clone the Repository
```bash
git clone https://github.com/cheshtagithub/Maverick-desktop-Assistant.git
cd Desktop_assistant
```
2. Install Dependencies
Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt
```
3. Configure API Keys
For weather and news features, add your API keys in the script:

weather_api_key — get it from OpenWeatherMap
news_api_key — get it from NewsAPI

Update these keys in the appropriate variables inside main.py.
4. Run the Assistant
```bash
python main.py
```
🛠️ Dependencies
The main Python libraries used include:

SpeechRecognition — for voice input

pyttsx3 — for text-to-speech output

requests — to fetch weather and news data

wikipedia — to retrieve information from Wikipedia

pyjokes — to tell jokes

pyaudio — to capture microphone input

Refer to requirements.txt for the full list.

🎤 Features

Voice Interaction: Uses Google Speech Recognition API for converting your voice to text

Wikipedia Search: Answers your questions by summarizing Wikipedia articles

Weather Updates: Real-time weather information based on your location

News Headlines: Latest US news fetched using NewsAPI

Music Player: Plays music files stored locally on your computer

Website Launcher: Opens popular websites and local applications via voice commands
