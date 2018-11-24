import random

class Talker():
    def __init__(self):
        self.message = ""
        self.helpNeeded = False
        self.denied = False
        self.newStressSituation()
        self.messageList = ["Попробуй выпить воды", "Сделай несколько глубоких вдохов", "Выйди на улицу и подыши свежим воздухом"]
        self.countToNewAdvice = 10
        self.currentCountToNewAdvice = 0


    def getMessage(self):
        if (self.denied):
            return "Отказался от помощи"
        if (self.helpNeeded):
            if (self.currentCountToNewAdvice == self.countToNewAdvice):
                self.getNewAdvice()
                self.currentCountToNewAdvice = 0
                self.currentCountToNewAdvice = self.currentCountToNewAdvice + 1
        return self.message
    
    def newStressSituation(self):
        self.helpNeeded = False
        self.message = "Мне кажется, ты волнуешься. Тебе не нужна помощь?"
        self.currentCountToNewAdvice = 0
    
    def newDefaultSituation(self):
        self.denied = False
        self.message = ""

    def getNewAdvice(self):
        self.helpNeeded = True
        self.message = self.messageList[random.randint(0, len(self.messageList) - 1)]
    
    def setWantedHelp(self, value):
        self.denied = value