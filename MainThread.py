import random
from datetime import datetime

class MainThread():

    def __init__(self):
        self.A = 0 #amplitude
        self.HR = 0 #heart rate
        self.minHR = 70
        self.maxHR = 80
        self.averageHR = 75
        self.minA = 1 
        self.maxA = 3
        self.chanseChangeA = 30
        self.countMeausures = 5
        self.lastAmplitude = []
        self.lastHeartRate = []
        self.result = ""
        self.stressLevel = 0
        self.isNotNormalHR = 90
        self.isOK = True
        self.fileName = "log.txt"
        #open(self.fileName, "r")

    def operation(self):
        #Получает текущие значения пульса и физической активности
        self.A = self.getAmplitude()
        self.HR = self.getHeartRate()
        #Добавляет их в выборку так
        #Удаляет устаревшие значения
        if (len(self.lastAmplitude) == self.countMeausures):
            self.lastAmplitude.pop(self.countMeausures - 1)
        self.lastAmplitude.insert(0, self.A)

        if (len(self.lastHeartRate) == self.countMeausures):
            self.lastHeartRate.pop(self.countMeausures - 1)
        self.lastHeartRate.insert(0, self.HR)
        #Если уже набрано минимальное необходимое количество выборок - проводит анализ
        self.result = "Создание выборки. Осталось еще {} данных для проведения анализа".format(self.countMeausures - len(self.lastAmplitude))
        if (len(self.lastAmplitude) == self.countMeausures and len(self.lastHeartRate) == self.countMeausures):
            normalHeartRate = False
            normalAmplitude = False
            for i in range(self.countMeausures):   
                if (self.lastHeartRate[i] < self.isNotNormalHR):
                    normalHeartRate = True
                if (self.lastAmplitude[i] < self.minA):
                    normalAmplitude = True
            if not(normalHeartRate) and normalAmplitude:
                self.result = "Подозрение на стресс"
            if not(normalHeartRate) and not(normalAmplitude):
                self.result = "Физическая активность"
            if normalHeartRate and normalAmplitude:
                self.result = "Состояние покоя"
            if normalHeartRate and not(normalAmplitude):
                self.result = "Слабая физическая активность"
            self.saveData()
        self.stressLevel = (self.HR - self.averageHR) * 100 / (self.averageHR * self.A)

    def getAmplitude(self): 
        amplityde = random.randint(0, self.minA)
        if (random.randint(0, 100) < self.chanseChangeA):
            amplityde = random.randint(self.minA, self.maxA)
        return amplityde

    def getHeartRate(self):
        heartRate = random.randint(self.minHR, self.maxHR)
        return heartRate

    def setActive(self, value):
        self.active = value
    
    def addToRangeAmplitude(self, value):
        if (self.chanseChangeA + value <= 100) and (self.chanseChangeA + value >= 0): 
            self.chanseChangeA = self.chanseChangeA + value
            return True
        else: 
            return False

    def addToRangeHealthRate(self, value):
        if (self.maxHR + value < 200) and (self.minHR + value > 0):
            self.minHR = self.minHR + value
            self.maxHR = self.maxHR + value
            return True
        else:
            return False
    
    def saveData(self):
       # file = open(self.fileName, "r")
       # file.write("Время:{}|Состояние{}".format(datatime.datatime.now().time(), self.result))
       pass
        
