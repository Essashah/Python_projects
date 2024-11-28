import webbrowser
import speech_recognition as sr
import pyttsx3
import requests
import xml.etree.ElementTree as ET
import random

# Initialize the speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Variable to store the user's name and language
user_name = ""
language = "English"  # Default language

# Language dictionaries for responses
responses = {
    "English": {
        "greeting": "Hello! I am Jarvis, your assistant. What is your name?",
        "nice_to_meet": "Nice to meet you, {}! How can I assist you today?",
        "fetching_headlines": "Fetching today's headlines from BBC.",
        "playing_music": "Playing {} on YouTube.",
        "how_are_you": ["I'm just a program, but I'm here to help you!", 
                         "I'm doing well, thanks for asking! How can I assist you today?",
                         "I'm functioning as expected! What can I do for you?"],
        "help": "You can say 'play music', 'headlines', 'open Google', or ask me how I'm doing!",
        "goodbye": "Goodbye!",
        "unknown": "I can help you play music, fetch headlines, open Google, or have a conversation. Just say 'play music', 'headlines', or 'open Google'.",
        "ask_language": "What language would you like to use? You can say English, Spanish, or French.",
        "set_language": "Language set to {}.",
        "joke": ["Why did the scarecrow win an award? Because he was outstanding in his field!",
                 "What do you call fake spaghetti? An impasta!",
                 "Why don't scientists trust atoms? Because they make up everything!"]
    },
    "Spanish": {
        "greeting": "¡Hola! Soy Jarvis, tu asistente. ¿Cuál es tu nombre?",
        "nice_to_meet": "¡Encantado de conocerte, {}! ¿Cómo puedo ayudarte hoy?",
        "fetching_headlines": "Obteniendo los titulares de hoy de la BBC.",
        "playing_music": "Reproduciendo {} en YouTube.",
        "how_are_you": ["Soy solo un programa, pero estoy aquí para ayudarte!", 
                         "¡Estoy bien, gracias por preguntar! ¿Cómo puedo ayudarte hoy?",
                         "¡Estoy funcionando como se espera! ¿Qué puedo hacer por ti?"],
        "help": "Puedes decir 'reproducir música', 'titulares', 'abrir Google' o preguntarme cómo estoy.",
        "goodbye": "¡Adiós!",
        "unknown": "Puedo ayudarte a reproducir música, obtener titulares, abrir Google o tener una conversación. Simplemente di 'reproducir música', 'titulares' o 'abrir Google'.",
        "ask_language": "¿Qué idioma te gustaría usar? Puedes decir inglés, español o francés.",
        "set_language": "Idioma establecido en {}.",
        "joke": ["¿Por qué ganó el espantapájaros un premio? ¡Porque era excepcional en su campo!",
                 "¿Cómo se llama una pasta falsa? ¡Una impasta!",
                 "¿Por qué los científicos no confían en los átomos? ¡Porque lo componen todo!"]
    },
    "French": {
        "greeting": "Bonjour! Je suis Jarvis, votre assistant. Quel est votre nom?",
        "nice_to_meet": "Enchanté de vous rencontrer, {}! Comment puis-je vous aider aujourd'hui?",
        "fetching_headlines": "Récupération des titres d'aujourd'hui de la BBC.",
        "playing_music": "Lecture de {} sur YouTube.",
        "how_are_you": ["Je ne suis qu'un programme, mais je suis ici pour vous aider!", 
                         "Je vais bien, merci de demander! Comment puis-je vous aider aujourd'hui?",
                         "Je fonctionne comme prévu! Que puis-je faire pour vous?"],
        "help": "Vous pouvez dire 'jouer de la musique', 'titres', 'ouvrir Google' ou me demander comment je vais.",
        "goodbye": "Au revoir!",
        "unknown": "Je peux vous aider à jouer de la musique, à obtenir des titres, à ouvrir Google ou à avoir une conversation. Dites simplement 'jouer de la musique', 'titres' ou 'ouvrir Google'.",
        "ask_language": "Quelle langue aimeriez-vous utiliser? Vous pouvez dire anglais, espagnol ou français.",
        "set_language": "Langue définie sur {}.",
        "joke": ["Pourquoi le épouvantail a-t-il remporté un prix? Parce qu'il était exceptionnel dans son domaine!",
                 "Comment appelle-t-on des pâtes fausses? Une impasta!",
                 "Pourquoi les scientifiques ne font-ils pas confiance aux atomes? Parce qu'ils composent tout!"]
    }
}

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, there seems to be an issue with the speech recognition service.")
            return ""

def play_music_on_youtube(song_name):
    url = f"https://www.youtube.com/results?search_query={song_name}"
    webbrowser.open(url)
    speak(responses[language]["playing_music"].format(song_name))

def get_bbc_headlines():
    url = "http://feeds.bbci.co.uk/news/rss.xml"
    response = requests.get(url)
    root = ET.fromstring(response.content)

    headlines = []
    for item in root.findall('.//item'):
        title = item.find('title').text
        headlines.append(title)

    return headlines

def main():
    global user_name, language
    speak(responses[language]["greeting"])
    
    user_name = listen()
    if user_name:
        speak(responses[language]["nice_to_meet"].format(user_name))
    else:
        speak("I didn't catch your name, but that's okay! How can I assist you today?")

    while True:
        command = listen()

        if 'play music' in command:
            speak("What song would you like to listen to?")
            song_name = listen()
            if song_name:
                play_music_on_youtube(song_name)

        elif 'headlines' in command:
            speak(responses[language]["fetching_headlines"])
            headlines = get_bbc_headlines()
            for headline in headlines[:5]:  # Get the first 5 headlines
                speak(headline)
            speak("Those were the top headlines.")

        elif 'open google' in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google.")

        elif 'how are you' in command:
            speak(random.choice(responses[language]["how_are_you"]))

        elif 'what can you do' in command:
            speak(responses[language]["help"])

        elif 'my name is' in command:
            user_name = command.split("my name is")[-1].strip()
            speak(responses[language]["nice_to_meet"].format(user_name))

        elif 'what is my name' in command:
            if user_name:
                speak(f"Your name is {user_name}.")
            else:
                speak("I don't know your name yet. You can tell me by saying 'my name is' followed by your name.")

        elif 'hello' in command or 'hi' in command:
            speak(f"Hello again, {user_name}! How can I assist you?")

        elif 'help' in command:
            speak(responses[language]["help"])

        elif 'stop' in command or 'exit' in command:
            speak(responses[language]["goodbye"])
            break

        elif 'set language' in command:
            speak(responses[language]["ask_language"])
            lang = listen()
            if 'english' in lang:
                language = "English"
            elif 'spanish' in lang:
                language = "Spanish"
            elif 'french' in lang:
                language = "French"
            speak(responses[language]["set_language"].format(language))

        elif 'tell me a joke' in command:
            speak(random.choice(responses[language]["joke"]))

        else:
            speak(responses[language]["unknown"])

if __name__ == "__main__":
    main()