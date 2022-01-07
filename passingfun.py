def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    gretting = func("Hi, I am created by a function passed as an argument.")
    print(gretting)


greet(shout)
greet(whisper)
