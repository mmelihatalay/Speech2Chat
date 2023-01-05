import openai

class ChatGPT():

    def __init__(self, model_engine="text-davinci-003"):
        openai.api_key = "<openAI API key>"
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
