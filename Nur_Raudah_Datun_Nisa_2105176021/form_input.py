# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tugas.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys, image


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1187, 935)
        self.Jenis = QtWidgets.QFrame(Form)
        self.Jenis.setGeometry(QtCore.QRect(10, 0, 1061, 961))
        self.Jenis.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.Jenis.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Jenis.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Jenis.setObjectName("Jenis")
        self.label = QtWidgets.QLabel(self.Jenis)
        self.label.setGeometry(QtCore.QRect(240, 270, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Jenis)
        self.label_2.setGeometry(QtCore.QRect(350, 50, 451, 101))
        self.label_2.setStyleSheet("font: 8pt \"MS Serif\";\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"font: 30pt \"Sitka\";")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.Jenis)
        self.label_4.setGeometry(QtCore.QRect(920, 10, 71, 51))
        self.label_4.setStyleSheet("\n"
"image: url(:/newPrefix/img/ICON.png);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("img/ICON.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.Jenis)
        self.label_5.setGeometry(QtCore.QRect(800, 20, 61, 31))
        self.label_5.setStyleSheet("image: url(:/newPrefix/img/KM.png);")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("img/KM.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.Jenis)
        self.label_6.setGeometry(QtCore.QRect(860, 10, 61, 51))
        self.label_6.setStyleSheet("image: url(:/newPrefix/img/unmul.png);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("img/unmul.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.Jenis)
        self.label_7.setGeometry(QtCore.QRect(990, 0, 61, 61))
        self.label_7.setStyleSheet("image: url(:/newPrefix/img/Cuplikan_layar_2024-04-19_222635-removebg-preview.png);")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("img/Cuplikan_layar_2024-04-19_222635-removebg-preview.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.Jenis)
        self.label_8.setGeometry(QtCore.QRect(40, 450, 301, 61))
        self.label_8.setStyleSheet("font: 20pt \"Sitka\";")
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(self.Jenis)
        self.lineEdit.setGeometry(QtCore.QRect(40, 550, 981, 31))
        self.lineEdit.setStyleSheet("font: 14pt \"Arial\";\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.Jenis)
        self.comboBox.setGeometry(QtCore.QRect(40, 630, 981, 31))
        self.comboBox.setStyleSheet("font: 14pt \"MS Sans Serif\";\n"
"font: 12pt \"Arial\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(4, "")
        self.comboBox_2 = QtWidgets.QComboBox(self.Jenis)
        self.comboBox_2.setGeometry(QtCore.QRect(40, 710, 981, 31))
        self.comboBox_2.setStyleSheet("font: 14pt \"MS Sans Serif\";\n"
"font: 12pt \"Arial\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(3, "")
        self.spinBox = QtWidgets.QSpinBox(self.Jenis)
        self.spinBox.setGeometry(QtCore.QRect(40, 790, 981, 31))
        self.spinBox.setStyleSheet("font: 14pt \"Arial\";")
        self.spinBox.setObjectName("spinBox")
        self.label_9 = QtWidgets.QLabel(self.Jenis)
        self.label_9.setGeometry(QtCore.QRect(40, 520, 91, 21))
        self.label_9.setStyleSheet("font: 14pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.Jenis)
        self.label_10.setGeometry(QtCore.QRect(40, 600, 121, 21))
        self.label_10.setStyleSheet("font: 14pt \"Arial\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.Jenis)
        self.label_11.setGeometry(QtCore.QRect(40, 680, 121, 21))
        self.label_11.setStyleSheet("font: 14pt \"Arial\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.Jenis)
        self.label_12.setGeometry(QtCore.QRect(40, 760, 121, 21))
        self.label_12.setStyleSheet("font: 14pt \"Arial\";")
        self.label_12.setObjectName("label_12")
        self.label_3 = QtWidgets.QLabel(self.Jenis)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 191, 171))
        self.label_3.setStyleSheet("image: url(:/newPrefix/img/Espresso-removebg-preview.png);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("img/Espresso-removebg-preview.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_13 = QtWidgets.QLabel(self.Jenis)
        self.label_13.setGeometry(QtCore.QRect(90, 350, 151, 31))
        self.label_13.setStyleSheet("font: 13pt \"Arial\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.Jenis)
        self.label_14.setGeometry(QtCore.QRect(50, 380, 181, 31))
        self.label_14.setStyleSheet("font: 15pt \"Sitka\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.Jenis)
        self.label_15.setGeometry(QtCore.QRect(320, 270, 55, 16))
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.Jenis)
        self.label_16.setGeometry(QtCore.QRect(340, 190, 171, 151))
        self.label_16.setStyleSheet("image: url(:/newPrefix/img/ristrett000o-removebg-preview.png);")
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("img/ristrett000o-removebg-preview.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.Jenis)
        self.label_17.setGeometry(QtCore.QRect(370, 350, 151, 31))
        self.label_17.setStyleSheet("font: 13pt \"Arial\";")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.Jenis)
        self.label_18.setGeometry(QtCore.QRect(320, 380, 181, 31))
        self.label_18.setStyleSheet("font: 15pt \"Sitka\";")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.Jenis)
        self.label_19.setGeometry(QtCore.QRect(580, 150, 221, 191))
        self.label_19.setStyleSheet("image: url(:/newPrefix/img/Americano-removebg-preview.png);")
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("img/Americano-removebg-preview.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.Jenis)
        self.label_20.setGeometry(QtCore.QRect(640, 350, 151, 31))
        self.label_20.setStyleSheet("font: 13pt \"Arial\";")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.Jenis)
        self.label_21.setGeometry(QtCore.QRect(600, 380, 181, 31))
        self.label_21.setStyleSheet("font: 15pt \"Sitka\";")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.Jenis)
        self.label_22.setGeometry(QtCore.QRect(840, 200, 241, 141))
        self.label_22.setStyleSheet("image: url(:/newPrefix/img/macchiato-removebg-preview.png);")
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("img/macchiato-removebg-preview.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.Jenis)
        self.label_23.setGeometry(QtCore.QRect(910, 350, 151, 31))
        self.label_23.setStyleSheet("font: 13pt \"Arial\";")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.Jenis)
        self.label_24.setGeometry(QtCore.QRect(860, 380, 181, 31))
        self.label_24.setStyleSheet("font: 15pt \"Sitka\";")
        self.label_24.setObjectName("label_24")
        self.pushButton = QtWidgets.QPushButton(self.Jenis)
        self.pushButton.setGeometry(QtCore.QRect(40, 857, 981, 31))
        self.pushButton.setStyleSheet("\n"
"background-color:rgb(0, 170, 0);\n"
"color:rgb(255, 255, 255);\n"
"font-size:20px;\n"
"font-weight:200px;")
        self.pushButton.setObjectName("pushButton")
        self.label_25 = QtWidgets.QLabel(self.Jenis)
        self.label_25.setGeometry(QtCore.QRect(790, 900, 371, 31))
        self.label_25.setStyleSheet("font: 12pt \"Sitka\";")
        self.label_25.setObjectName("label_25")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "\n"
"beautiful coffee"))
        self.label_2.setText(_translate("Form", "Beautiful Coffee"))
        self.label_8.setText(_translate("Form", "Isi Pesanan Anda"))
        self.comboBox.setItemText(0, _translate("Form", "Espresso"))
        self.comboBox.setItemText(1, _translate("Form", "Ristretto"))
        self.comboBox.setItemText(2, _translate("Form", "Americano"))
        self.comboBox.setItemText(3, _translate("Form", "Macchiato"))
        self.comboBox_2.setItemText(0, _translate("Form", "Besar"))
        self.comboBox_2.setItemText(1, _translate("Form", "Normal"))
        self.comboBox_2.setItemText(2, _translate("Form", "Kecil"))
        self.label_9.setText(_translate("Form", "Nama :"))
        self.label_10.setText(_translate("Form", "Jenis Kopi :"))
        self.label_11.setText(_translate("Form", "Ukuran"))
        self.label_12.setText(_translate("Form", "Jumlah"))
        self.label_13.setText(_translate("Form", "Espresso"))
        self.label_14.setText(_translate("Form", "IDR 30.000.00"))
        self.label_17.setText(_translate("Form", "Ristretto"))
        self.label_18.setText(_translate("Form", "IDR 25.000.00"))
        self.label_20.setText(_translate("Form", "Americano"))
        self.label_21.setText(_translate("Form", "IDR 30.000.00"))
        self.label_23.setText(_translate("Form", "Macchiato"))
        self.label_24.setText(_translate("Form", "IDR 35.000.00"))
        self.pushButton.setText(_translate("Form", "Pesan"))
        self.label_25.setText(_translate("Form", "By Nur Raudah Datun Nisa"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
