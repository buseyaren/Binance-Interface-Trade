# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arayuz.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_coins(object):
    def setupUi(self, coins):
        coins.setObjectName("coins")
        coins.resize(1277, 736)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(95, 127, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 127, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 127, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        coins.setPalette(palette)
        coins.setTabletTracking(False)
        self.list_1 = QtWidgets.QListView(coins)
        self.list_1.setGeometry(QtCore.QRect(150, 150, 171, 271))
        self.list_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.list_1.setObjectName("list_1")
        self.button_1 = QtWidgets.QPushButton(coins)
        self.button_1.setGeometry(QtCore.QRect(180, 430, 113, 32))
        self.button_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_1.setObjectName("button_1")
        self.list_2 = QtWidgets.QListView(coins)
        self.list_2.setGeometry(QtCore.QRect(330, 150, 151, 271))
        self.list_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.list_2.setObjectName("list_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(coins)
        self.buttonBox.setGeometry(QtCore.QRect(940, 600, 164, 32))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.button_2 = QtWidgets.QPushButton(coins)
        self.button_2.setGeometry(QtCore.QRect(330, 430, 113, 32))
        self.button_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_2.setObjectName("button_2")
        self.list_3 = QtWidgets.QListView(coins)
        self.list_3.setGeometry(QtCore.QRect(490, 150, 151, 271))
        self.list_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.list_3.setObjectName("list_3")
        self.button_3 = QtWidgets.QPushButton(coins)
        self.button_3.setGeometry(QtCore.QRect(500, 430, 113, 32))
        self.button_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_3.setObjectName("button_3")
        self.list_4 = QtWidgets.QListView(coins)
        self.list_4.setGeometry(QtCore.QRect(650, 150, 151, 271))
        self.list_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.list_4.setObjectName("list_4")
        self.button_4 = QtWidgets.QPushButton(coins)
        self.button_4.setGeometry(QtCore.QRect(660, 430, 113, 32))
        self.button_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_4.setObjectName("button_4")
        self.list_5 = QtWidgets.QListView(coins)
        self.list_5.setGeometry(QtCore.QRect(810, 150, 151, 271))
        self.list_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.list_5.setObjectName("list_5")
        self.button_5 = QtWidgets.QPushButton(coins)
        self.button_5.setGeometry(QtCore.QRect(820, 430, 113, 32))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(158, 255, 146))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 193, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(158, 255, 146))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 193, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(158, 255, 146))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 193, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        self.button_5.setPalette(palette)
        self.button_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_5.setObjectName("button_5")
        self.label = QtWidgets.QLabel(coins)
        self.label.setGeometry(QtCore.QRect(200, 120, 60, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(coins)
        self.label_2.setGeometry(QtCore.QRect(370, 120, 70, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(coins)
        self.label_3.setGeometry(QtCore.QRect(540, 120, 60, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(coins)
        self.label_4.setGeometry(QtCore.QRect(680, 120, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(coins)
        self.label_5.setGeometry(QtCore.QRect(830, 120, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(coins)
        QtCore.QMetaObject.connectSlotsByName(coins)

    def retranslateUi(self, coins):
        _translate = QtCore.QCoreApplication.translate
        coins.setWindowTitle(_translate("coins", "coins"))
        self.button_1.setText(_translate("coins", "COİN"))
        self.button_2.setText(_translate("coins", "FİYAT"))
        self.button_3.setText(_translate("coins", "MİKTAR"))
        self.button_4.setText(_translate("coins", "DÜŞÜK"))
        self.button_5.setText(_translate("coins", "YÜKSEK"))
        self.label.setText(_translate("coins", "Coinler"))
        self.label_2.setText(_translate("coins", "Fiyat Tutarı"))
        self.label_3.setText(_translate("coins", "Miktar"))
        self.label_4.setText(_translate("coins", "En Düşük Tutar"))
        self.label_5.setText(_translate("coins", "En Yüksek Tutar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    coins = QtWidgets.QWidget()
    ui = Ui_coins()
    ui.setupUi(coins)
    coins.show()
    sys.exit(app.exec_())