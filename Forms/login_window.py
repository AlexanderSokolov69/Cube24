#!/usr/bin/env python3
# coding:utf-8
from PyQt5 import QtWidgets

from Forms.login_Form import Ui_LoginDialog


class FormLoginWindow(QtWidgets, Ui_LoginDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Подключение к серверу')