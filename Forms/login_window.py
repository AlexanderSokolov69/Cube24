#!/usr/bin/env python3
# coding:utf-8
import jwt
from PyQt5.Qt import Qt
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QWidget, QDialog, QMainWindow
from requests import post

from Forms.login_Form import Ui_LoginDialog
from misc.const import const
from misc.functions import msg_window
from misc.logwriter import flog


class FormLoginWindow(QDialog, Ui_LoginDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Подключение к серверу')
        self.setWindowModality(Qt.ApplicationModal)
        # self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.login.setFocusPolicy(Qt.StrongFocus)
        self.user = None
        self.token = None
        self.decoded_token = None
        self.current_year = 2024
        self.button_ok.clicked.connect(self.try_login)

    def try_login(self):
        # print('login', self.login.text())
        # print('password', self.password.text())
        data = {'login': self.login.text().strip(), 'password': self.password.text().strip()}
        response = {}
        try:
            response = post('http://localhost:5050/api/login', json=data, timeout=5).json()
            self.token = response.get('token', None)
        except Exception:
            msg_window(text='Соединение с сервером не удалось!')
            flog.to_log(f"Ошибка подключения к серверу: {Exception}")
        #print(self.token)
        if self.token:
            self.decoded_token = self.decode_token()
            if self.decoded_token:
                self.user = self.decoded_token['user']
                self.close()
        else:
            msg_window(text=response.get('message', 'Неизвестная ошибка!'))

    def closeEvent(self, event: QCloseEvent):
        event.accept()

    def decode_token(self):
        token = None
        try:
            algorithm = jwt.get_unverified_header(self.token).get('alg')
            token = jwt.decode(self.token, key=const.jwt_key, algorithms=algorithm)
        except Exception:
            flog.to_log(f'token decode Error: {Exception}')
        return token
