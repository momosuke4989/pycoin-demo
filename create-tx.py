#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from pycoin.tx import Tx
from pycoin.services import spendables_for_address
from pycoin.services.blockchain_info import BlockchainInfoProvider, send_tx
from pycoin.tx.tx_utils import create_signed_tx
from PyQt5.QtWidgets import (QLabel, QLineEdit, QGridLayout, QWidget, 
                             QApplication, QPushButton, QDesktopWidget, 
                             QTextEdit)

class MainWindow(QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        #送金元アドレス
        address = "Enter BTC address"
        #送金先アドレス
        destination = "Enter BTC address"

        self.fromaddress = QLineEdit()
        self.fromaddress.setText(address)
        #self.fromaddress.setReadOnly(True)

        self.sendto = QLineEdit()
        self.sendto.setText(destination)
        #self.sendto.setReadOnly(True)

        self.transaction = QTextEdit()
        self.transaction.setReadOnly(True)

        sndTxBtn = QPushButton('send Tx', self)
        sndTxBtn.clicked.connect(self.createTx)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(QLabel('From'), 1,0)
        grid.addWidget(self.fromaddress, 1,1)

        grid.addWidget(QLabel('Send to'), 2,0)
        grid.addWidget(self.sendto, 2,1)

        grid.addWidget(QLabel('Transaction'), 3,0)
        grid.addWidget(self.transaction, 3, 1, 1, 2)

        grid.addWidget(sndTxBtn, 4, 1)

        self.setLayout(grid)

        self.resize(320, 180)
        self.center()
        self.setWindowTitle('Create transaction demo')
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def createTx(self):

        address = self.fromaddress.text()
        destination = self.sendto.text()
        #あらかじめ送信元アドレスに対応する秘密鍵を入力しておく
        wif = ""
        sndtx = BlockchainInfoProvider('BTC')

        spendables = spendables_for_address(address, "BTC")
        tx = create_signed_tx(spendables, payables=[destination], wifs=[wif])
        sndtx.broadcast_tx(tx)
        self.transaction.setText(tx.as_hex())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

