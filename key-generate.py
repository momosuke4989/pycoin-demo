#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from pycoin.key import Key
from pycoin.key.BIP32Node import BIP32Node
from PyQt5.QtWidgets import (QLabel, QLineEdit, QGridLayout, QWidget, 
                             QApplication, QPushButton, QDesktopWidget, 
                             QTextEdit)
def KeyGenerater(s):
    key = BIP32Node.from_master_secret(s.encode("utf8"))
    return key.wif(), key.address()

class MainWindow(QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.inputLine = QLineEdit()

        self.privateKey = QTextEdit()
        self.privateKey.setReadOnly(True)

        self.publicKey = QTextEdit()
        self.publicKey.setReadOnly(True)

        generateBtn = QPushButton('Generate', self)
        generateBtn.clicked.connect(self.showKeys)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(QLabel('Input'), 1, 0)
        grid.addWidget(self.inputLine, 1, 1)

        grid.addWidget(generateBtn, 1, 2)

        grid.addWidget(QLabel('Private Key'), 2, 0)
        grid.addWidget(self.privateKey, 2, 1, 1, 2)

        grid.addWidget(QLabel('Public Key'), 3, 0)
        grid.addWidget(self.publicKey, 3, 1, 1, 2)

        self.setLayout(grid)

        self.resize(350, 150)
        self.center()
        self.setWindowTitle('Key generate demo')
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showKeys(self):

        text = self.inputLine.text()
        private, public = KeyGenerater(text)
        self.privateKey.setText(private)
        self.publicKey.setText(public)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

