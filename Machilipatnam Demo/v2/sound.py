from gtts import gTTS


def voice(string):
        tts = gTTS(text=string, lang='en')
        tts.save("done.mp3")

voice("Here's Your order, Have fun and enjoy your stay here")
