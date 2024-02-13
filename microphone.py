import speech_recognition as sr

recognizer = sr.Recognizer()

def get_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return (recognize_speech(audio))

def recognize_speech(audio):
    try:
        text = recognizer.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
    except sr.RequestError:
        print("Sorry, there was an error processing your request.")