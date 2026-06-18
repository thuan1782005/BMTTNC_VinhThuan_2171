from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 426)

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 110, 70, 20))

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 30, 200, 30))

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)

        self.label_2.setFont(font)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 190, 80, 20))

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 110, 80, 20))

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 190, 80, 20))

        # Plain Text
        self.txt_plain_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_plain_text.setGeometry(
            QtCore.QRect(140, 110, 261, 71)
        )

        # Information
        self.txt_information = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_information.setGeometry(
            QtCore.QRect(510, 110, 241, 71)
        )

        # Cipher Text
        self.txt_cipher_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_cipher_text.setGeometry(
            QtCore.QRect(140, 200, 261, 71)
        )

        # Signature
        self.txt_signature = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_signature.setGeometry(
            QtCore.QRect(510, 200, 241, 71)
        )

        # Buttons
        self.pushButton = QtWidgets.QPushButton(
            "Generate Keys",
            self.centralwidget
        )
        self.pushButton.setGeometry(
            QtCore.QRect(480, 30, 100, 25)
        )

        self.pushButton_2 = QtWidgets.QPushButton(
            "Encrypt",
            self.centralwidget
        )
        self.pushButton_2.setGeometry(
            QtCore.QRect(150, 290, 75, 25)
        )

        self.pushButton_3 = QtWidgets.QPushButton(
            "Decrypt",
            self.centralwidget
        )
        self.pushButton_3.setGeometry(
            QtCore.QRect(310, 290, 75, 25)
        )

        self.pushButton_4 = QtWidgets.QPushButton(
            "Sign",
            self.centralwidget
        )
        self.pushButton_4.setGeometry(
            QtCore.QRect(520, 290, 75, 25)
        )

        self.pushButton_5 = QtWidgets.QPushButton(
            "Verify",
            self.centralwidget
        )
        self.pushButton_5.setGeometry(
            QtCore.QRect(670, 290, 75, 25)
        )

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(
            _translate("MainWindow", "RSA Cipher")
        )

        self.label.setText(
            _translate("MainWindow", "Plain Text:")
        )

        self.label_2.setText(
            _translate("MainWindow", "RSA CIPHER")
        )

        self.label_3.setText(
            _translate("MainWindow", "CipherText:")
        )

        self.label_4.setText(
            _translate("MainWindow", "Information:")
        )

        self.label_5.setText(
            _translate("MainWindow", "Signature:")
        )