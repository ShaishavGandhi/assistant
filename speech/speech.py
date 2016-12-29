import pyttsx
from threading import Thread

class Speech(object):

    engine = None

    def __init__(self):
        self.engine = pyttsx.init()

    def speak(self, sentence):
        thread = Thread(target = self.speakNew, args = (sentence, ))
        thread.start()
        thread.join()

    def speakNew(self, sentence):
        self.engine.say(sentence)
        self.engine.startLoop()
