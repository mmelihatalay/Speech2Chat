from CatchSpeechSR import CatchSpeech
from ChatCompletion import ChatGPT
from TextProcess import ReadText

speech = CatchSpeech(lang = "en-us")
speech.listen()
text = speech.toTextGoogle()

chatGPT = ChatGPT()
res = chatGPT.response(prompt = text)
print(res)
rt = ReadText()
rt.say(res)