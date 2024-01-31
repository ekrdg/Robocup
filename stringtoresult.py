#Working
import speech_recognition as sr
def wavtotext(recordpath):
    # Initialize recognizer class                                       
    r = sr.Recognizer()
    audio = sr.AudioFile(recordpath)
    with audio as source:
        audio = r.record(source)
        a = r.recognize_google(audio)
    city = a.split()[-1]
    return city

print(wavtotext())


