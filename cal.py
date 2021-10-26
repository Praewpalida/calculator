# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cal.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 550)
        Form.setStyleSheet("#Form{\n"
"background:#92d9ff;\n"
"}")
        self.outputLabel = QtWidgets.QLabel(Form)
        self.outputLabel.setGeometry(QtCore.QRect(40, 30, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setStyleSheet("#Form{\n"
"background:#ffffff;\n"
"}\n"
"\n"
"#outputLabel{\n"
"background:#ffffff;\n"
"}")
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.sevenButton = QtWidgets.QPushButton(Form, clicked= lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(30, 140, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.eightButton = QtWidgets.QPushButton(Form, clicked= lambda: self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(110, 140, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.nineButton = QtWidgets.QPushButton(Form, clicked= lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(190, 140, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.divideButton = QtWidgets.QPushButton(Form, clicked= lambda: self.press_it("/"))
        self.divideButton.setGeometry(QtCore.QRect(270, 140, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.fourButton = QtWidgets.QPushButton(Form, clicked= lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(30, 220, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.fiveButton = QtWidgets.QPushButton(Form, clicked= lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(110, 220, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.sixButton = QtWidgets.QPushButton(Form, clicked= lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(190, 220, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.multiplyButton = QtWidgets.QPushButton(Form, clicked= lambda: self.press_it("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(270, 220, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        self.oneButton = QtWidgets.QPushButton(Form, clicked= lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(30, 300, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.twoButton = QtWidgets.QPushButton(Form, clicked= lambda: self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(110, 300, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.threeButton = QtWidgets.QPushButton(Form, clicked= lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(190, 300, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.minusButton = QtWidgets.QPushButton(Form, clicked= lambda: self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(270, 300, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.equalButton = QtWidgets.QPushButton(Form, clicked= lambda: self.math_it())
        self.equalButton.setGeometry(QtCore.QRect(30, 380, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        self.zeroButton = QtWidgets.QPushButton(Form, clicked= lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(110, 380, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        self.decimalButton = QtWidgets.QPushButton(Form, clicked= lambda: self.dot_it())
        self.decimalButton.setGeometry(QtCore.QRect(190, 380, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimalButton.setFont(font)
        self.decimalButton.setObjectName("decimalButton")
        self.addButton = QtWidgets.QPushButton(Form, clicked= lambda: self.press_it("+"))
        self.addButton.setGeometry(QtCore.QRect(270, 380, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.ceButton = QtWidgets.QPushButton(Form, clicked= lambda: self.remove_it())
        self.ceButton.setGeometry(QtCore.QRect(30, 460, 141, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.ceButton.setFont(font)
        self.ceButton.setObjectName("ceButton")
        self.cButton = QtWidgets.QPushButton(Form, clicked= lambda: self.press_it("C"))
        self.cButton.setGeometry(QtCore.QRect(190, 460, 141, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def remove_it(self):
        screen = self.outputLabel.text()
        screen = screen[:-1]
        self.outputLabel.setText(screen)

    def math_it(self):
        screen = self.outputLabel.text()
        try:
            answer = eval(screen)
            self.outputLabel.setText(str(answer))
        except:
            self.outputLabel.setText("ERROR")

    def dot_it(self):
        screen = self.outputLabel.text()

        if screen[-1] == ".":
            pass
        else:
            self.outputLabel.setText(f'{screen}.')

    def press_it(self, pressed):
        if pressed == "C":
            self.outputLabel.setText("0")
        else:
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculator"))
        self.outputLabel.setText(_translate("Form", "0"))
        self.sevenButton.setText(_translate("Form", "7"))
        self.eightButton.setText(_translate("Form", "8"))
        self.nineButton.setText(_translate("Form", "9"))
        self.divideButton.setText(_translate("Form", "/"))
        self.fourButton.setText(_translate("Form", "4"))
        self.fiveButton.setText(_translate("Form", "5"))
        self.sixButton.setText(_translate("Form", "6"))
        self.multiplyButton.setText(_translate("Form", "*"))
        self.oneButton.setText(_translate("Form", "1"))
        self.twoButton.setText(_translate("Form", "2"))
        self.threeButton.setText(_translate("Form", "3"))
        self.minusButton.setText(_translate("Form", "-"))
        self.equalButton.setText(_translate("Form", "="))
        self.zeroButton.setText(_translate("Form", "0"))
        self.decimalButton.setText(_translate("Form", "."))
        self.addButton.setText(_translate("Form", "+"))
        self.ceButton.setText(_translate("Form", "CE"))
        self.cButton.setText(_translate("Form", "C"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    
