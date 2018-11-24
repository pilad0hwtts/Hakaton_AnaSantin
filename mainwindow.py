# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 405)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.PulsPB = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PulsPB.sizePolicy().hasHeightForWidth())
        self.PulsPB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(74)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(False)
        self.PulsPB.setFont(font)
        self.PulsPB.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PulsPB.setStyleSheet("text-align:center;\n"
"padding: 0.1%;")
        self.PulsPB.setMaximum(250)
        self.PulsPB.setProperty("value", 100)
        self.PulsPB.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.PulsPB.setTextVisible(True)
        self.PulsPB.setOrientation(QtCore.Qt.Vertical)
        self.PulsPB.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.PulsPB.setFormat(" %v ")
        self.PulsPB.setObjectName("PulsPB")
        self.verticalLayout_5.addWidget(self.PulsPB)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.PulsPlusBtn = QtWidgets.QPushButton(self.centralwidget)
        self.PulsPlusBtn.setObjectName("PulsPlusBtn")
        self.horizontalLayout_3.addWidget(self.PulsPlusBtn)
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.PulsMinusBtn = QtWidgets.QPushButton(self.centralwidget)
        self.PulsMinusBtn.setObjectName("PulsMinusBtn")
        self.horizontalLayout_3.addWidget(self.PulsMinusBtn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.MsgEdit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MsgEdit.sizePolicy().hasHeightForWidth())
        self.MsgEdit.setSizePolicy(sizePolicy)
        self.MsgEdit.setObjectName("MsgEdit")
        self.verticalLayout_3.addWidget(self.MsgEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.AmpPB = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AmpPB.sizePolicy().hasHeightForWidth())
        self.AmpPB.setSizePolicy(sizePolicy)
        self.AmpPB.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.AmpPB.setStyleSheet("text-align:center;\n"
"padding: 0.1%;")
        self.AmpPB.setMaximum(3)
        self.AmpPB.setProperty("value", 1)
        self.AmpPB.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.AmpPB.setTextVisible(True)
        self.AmpPB.setOrientation(QtCore.Qt.Vertical)
        self.AmpPB.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.AmpPB.setFormat("")
        self.AmpPB.setObjectName("AmpPB")
        self.verticalLayout_6.addWidget(self.AmpPB)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.AmpPlusBtn = QtWidgets.QPushButton(self.centralwidget)
        self.AmpPlusBtn.setObjectName("AmpPlusBtn")
        self.horizontalLayout_5.addWidget(self.AmpPlusBtn)
        spacerItem2 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.AmpMinusBtn = QtWidgets.QPushButton(self.centralwidget)
        self.AmpMinusBtn.setObjectName("AmpMinusBtn")
        self.horizontalLayout_5.addWidget(self.AmpMinusBtn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.stressLevelPB = QtWidgets.QProgressBar(self.centralwidget)
        self.stressLevelPB.setProperty("value", 24)
        self.stressLevelPB.setObjectName("stressLevelPB")
        self.horizontalLayout_4.addWidget(self.stressLevelPB)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startBtn.sizePolicy().hasHeightForWidth())
        self.startBtn.setSizePolicy(sizePolicy)
        self.startBtn.setObjectName("startBtn")
        self.horizontalLayout_2.addWidget(self.startBtn)
        spacerItem4 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setObjectName("stopBtn")
        self.horizontalLayout_2.addWidget(self.stopBtn)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AnaSantin"))
        self.label.setText(_translate("MainWindow", "Пульс"))
        self.PulsPlusBtn.setText(_translate("MainWindow", "+"))
        self.PulsMinusBtn.setText(_translate("MainWindow", "-"))
        self.label_2.setText(_translate("MainWindow", "Уровень активности"))
        self.AmpPlusBtn.setText(_translate("MainWindow", "+"))
        self.AmpMinusBtn.setText(_translate("MainWindow", "-"))
        self.startBtn.setText(_translate("MainWindow", "Старт"))
        self.stopBtn.setText(_translate("MainWindow", "Стоп"))
