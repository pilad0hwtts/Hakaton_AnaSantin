import random

class Talker():
    def __init__(self):
        self.message = ""
        self.helpNeeded = False
        self.denied = False
        self.messageList = ["Попробуй выпить воды", "Сделай несколько глубоких вдохов", "Выйди на улицу и подыши свежим воздухом"]
        self.currentCountToNewAdvice = 0


    def getNewAdvice(self):
        if (self.currentCountToNewAdvice == 0):
            self.helpNeeded = True
            self.message = self.messageList[random.randint(0, len(self.messageList) - 1)]
        self.currentCountToNewAdvice = (self.currentCountToNewAdvice + 1) % 10
        return self.message
    