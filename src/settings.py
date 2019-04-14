import os

DEBUG: bool = bool(int(os.environ['DEBUG']))
URL = "https://speech.googleapis.com/v1/speech:recognize?key={}"