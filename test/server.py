# -*- coding: utf-8 -*-
# Created by Yassine Kharrat
# Form implementation generated from reading ui file 'pytrans_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from googletrans import LANGUAGES, Translator


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        lang_list = []
        lang_little_list = []
        for lang in LANGUAGES:
            lang_list.append(LANGUAGES[lang])
            lang_little_list.append(lang)
        print(lang_list)
        print(lang_little_list)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(885, 600)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 450, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(
            "background-color:rgb(19, 152, 41);\n" "color:rgb(255, 255, 255);\n"
        )
        self.pushButton.setObjectName("pushButton")
        self.Input_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.Input_combobox.setGeometry(QtCore.QRect(0, 40, 371, 38))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setItalic(False)
        self.Input_combobox.setFont(font)
        self.Input_combobox.setObjectName("Input_combobox")
        self.Text1 = QtWidgets.QTextEdit(self.centralwidget)
        self.Text1.setGeometry(QtCore.QRect(0, 90, 371, 301))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setItalic(False)
        self.Text1.setFont(font)
        self.Text1.setObjectName("Text1")
        self.Input_combobox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.Input_combobox_2.setGeometry(QtCore.QRect(490, 40, 391, 38))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setItalic(False)
        self.Input_combobox_2.setFont(font)
        self.Input_combobox_2.setObjectName("Input_combobox_2")
        for ele in lang_list:
            self.Input_combobox.addItem(ele)
            self.Input_combobox_2.addItem(ele)

        self.Text2 = QtWidgets.QTextEdit(self.centralwidget)
        self.Text2.setGeometry(QtCore.QRect(490, 90, 391, 301))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setItalic(False)
        self.Text2.setFont(font)
        self.Text2.setObjectName("Text2")
        self.Text2.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 885, 30))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout_pytranslator = QtWidgets.QAction(MainWindow)
        self.actionAbout_pytranslator.setObjectName("actionAbout_pytranslator")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut("Ctrl+X")
        self.actionAbout_pytranslator.setShortcut("Ctrl+T")
        self.actionExit.triggered.connect(self.Quit)
        self.menuHelp.addAction(self.actionAbout_pytranslator)
        self.menuHelp.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.actionAbout_pytranslator.triggered.connect(self.show_popup)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(
            lambda: self.clicked(lang_list, lang_little_list)
        )

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pytranslator"))
        self.pushButton.setText(_translate("MainWindow", "Translate"))
        self.Input_combobox.setItemText(0, _translate("MainWindow", "Choose language"))
        self.Input_combobox_2.setItemText(
            0, _translate("MainWindow", "Choose language")
        )
        self.menuHelp.setTitle(_translate("MainWindow", "Info"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionAbout_pytranslator.setText(_translate("MainWindow", "About app"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def clicked(self, full_lang_list, little_lang_list):
        def Translate(src, text, dest):
            translator = Translator()
            Output = translator.translate(text, dest, src)
            print(Output.text)
            self.Text2.setText(Output.text)

        print("Clicked")
        text1 = self.Text1.toPlainText()
        print(text1)
        text_cmbox = self.Input_combobox.currentText()
        if text_cmbox in full_lang_list:
            index = self.Input_combobox.currentIndex() - 1
            print(index)
            src = little_lang_list[index]
            text_combo2 = self.Input_combobox_2.currentText()
            if text_combo2 in full_lang_list:
                index2 = self.Input_combobox_2.currentIndex()
                print(index2)
                dest = little_lang_list[index2]
                Translate(src, text1, dest)
            else:
                print("Not in My list")
        else:
            print("Not in the list")

    def Quit(self):
        app.exit()
        print("Hope you consider donating to my github")

    def show_popup(self):
        popup = QMessageBox()
        popup.setWindowTitle("About app")
        popup.setText("Pytranslator was created by Yassine Kharrat")
        popup.setIcon(QMessageBox.Information)
        x = popup.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())