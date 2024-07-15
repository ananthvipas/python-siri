import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use a female voice, for example

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'siri' in command:
                command = command.replace('siri', '').strip()
                print(f"Command: {command}")
    except sr.UnknownValueError:
        print("Sorry, I did not get that.")
    except sr.RequestError:
        print("Sorry, my speech service is down.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return command

def run_siri():
    while True:
        command = take_command()
        if command:
            if 'play' in command:
                song = command.replace('play', '').strip()
                talk('playing ' + song)
                pywhatkit.playonyt(song)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('Current time is ' + time)
            elif 'who is hacker' in command:
                person = command.replace('who is hacker ', '').strip()
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)

            elif 'about information technology' in command:
                person = command.replace('about information technology ', '').strip()
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)

            elif 'date' in command:
                talk('sorry, I have a headache')

            elif 'are you single' in command:
                talk('I am in a relationship with wifi')

            elif 'joke' in command:
                talk(pyjokes.get_joke())

            elif 'your name' in command:
                talk('siri')

            elif 'siri' in command or 'hey' in command:
                talk('Hi sir, how can I help you?')

            elif 'big prime number' in command or 'biggest prime number' in command:
                talk('M 8 2 5 8 9 9 3 3 ')

            elif 'note' in command:
                talk('What would you like me to note down?')
    
            elif 'about you' in command:
                talk('my self siri, ')

            elif 'shutdown' in command or 'bye' in command:
                talk('Shutting down. Goodbye!')
                break
            else:
                talk('Please say the command again.')

if __name__ == "__main__":
    run_siri()
