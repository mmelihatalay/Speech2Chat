import speech_recognition as sr  

class CatchSpeech():

        def __init__(self, lang="tr-tr"):
            self.r = sr.Recognizer()
            self.language = lang

        def listen(self):
            with sr.Microphone() as source:                                                                       
                print("Speak:")                                                                                   
                self._audio = self.r.listen(source)

        def toTextGoogle(self):
            try:
                txt = self.r.recognize_google(self._audio, language=self.language)
                return txt
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

if __name__ == "__main__":

    speech = CatchSpeech(lang="tr-tr")
    speech.listen()
    print(speech.toTextGoogle())