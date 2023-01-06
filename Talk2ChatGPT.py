from CatchSpeechSR import CatchSpeech
from ChatCompletion import ChatGPT
#from ChatGpt import ChatGpt as ChatGPT
from TextProcess import ReadText

def talk2ChatGPT(lang= "en-us", readText=True):
    while True:
        speech = CatchSpeech(lang = "en-us")
        speech.listen()
        text = speech.toTextGoogle()
        print(f"I said: \"{text}\"\n")
        if not text:
            print("Try again\n")
        else:
            chatGPT = ChatGPT()
            res = chatGPT.response(prompt = text)
            print(f"ChatGPT said: \"{res.strip()}\"\n")
            if ReadText:
                rt = ReadText()
                rt.say(res)
                
            try:
                input("To continue hit \"ENTER\"\nTo exit hit \"CTRL-C\"\n")
            except KeyboardInterrupt:
                print("ChatGPT terminated!")
                break