# Speech2Chat

First of all some external libraries are required:
```
  pip install openai
  
  pip install speechrecognition
  
  pip install pyttsx3
  ```
Secondly, you need an API Key from openAI. This API Key should be saved in config.json.

Finally, run
```
python ./main.py
```

# Talk2ChatGPT

Talk2ChatGPT has only one function which is talk2ChatGPT with two optional input.
```
talk2ChatGPT(lang="en-us", read=True)
lang is for language of speech recognition
read is for reading the answer from ChatGPT. If True read, else False do not read
```
