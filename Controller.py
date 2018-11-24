from PyQt5.QtCore import QTimer
from MainThread import MainThread
from mainwindow import Ui_MainWindow
from time import sleep


class Controller(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        self.tmr=QTimer()
        self.MainThread=MainThread()
        self.startBtn.clicked.connect(self.startEmu)
        self.stopBtn.clicked.connect(self.stopEmu)
        self.tmr.timeout.connect(self.timeTick)
        self.PulsPlusBtn.clicked.connect(self.PulsPlus)
        self.PulsMinusBtn.clicked.connect(self.PulsMinus)
        self.AmpPlusBtn.clicked.connect(self.AmpPlus)
        self.AmpMinusBtn.clicked.connect(self.AmpMinus)

    def stopEmu(self):
        self.tmr.stop()

    def startEmu(self):

        self.tmr.start(500)


    def timeTick(self):

        self.MainThread.operation()
        active=self.MainThread.A
        self.PulsPB.setValue(self.MainThread.HR)
        self.AmpPB.setValue(active)
        activeValue=None
        if(active<1):
            activeValue="Покой"
        elif(active<2):
            activeValue="Низкий"
        elif(active<3):
            activeValue="Средний"
        else:
            activeValue="Высокий"

        self.stressLevelPB.setValue(self.MainThread.stressLevel)
        self.AmpPB.setFormat(activeValue)
        self.MsgEdit.setText(self.MainThread.result)


    def setAmplitude(self, amplitude):
        self.AmpPB.setValue(apmplitude)

    def setPulse(self, pulse):
        self.PulsPB.setValue(pulse)


    def PulsPlus(self):
        self.MainThread.addToRangeHealthRate(5)

    def PulsMinus(self):
        self.MainThread.addToRangeHealthRate(-5)

    def AmpPlus(self):
        self.MainThread.addToRangeAmplitude(1)

    def AmpMinus(self):
        self.MainThread.addToRangeAmplitude(-1)
