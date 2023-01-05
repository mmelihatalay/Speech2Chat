import pyttsx3

class ReadText():

    def __init__(self):
        self._engine = pyttsx3.init()

    def say(self, text="No text provided!"):
        self._engine.say(text)
        self._engine.runAndWait()


if __name__ == "__main__":
    rt = ReadText()
    rt.say("Hello World")