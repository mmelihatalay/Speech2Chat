import openai
import json
import os

class ChatGPT():

    def __init__(self, model_engine="text-davinci-003"):
        configFile = "config.json"
        if not os.path.isfile(configFile):
            raise Exception(f"\"{configFile}\" does not exist!")
        with open(configFile) as f:
            config = json.load(f)
        try:
            openai.api_key = config["openAIKey"]
        except KeyError:
            raise Exception("Key value \"openAIKey\" not in config.json")
        self.model_engine = model_engine

    def response(self, prompt):
        self.prompt = prompt
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=self.prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        return completion.choices[0].text

if __name__ == "__main__":

    chatGPT = ChatGPT()
    prompt = "Can you explain me how many planets there are in solar system?"
    print(chatGPT.response(prompt))