#!/usr/bin/env python3
# coding:utf-8
from PyQt5.QtWidgets import QWidget

from Forms.users_Form import Ui_Form
from api.api import net_api


class UsersForm(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def showEvent(self, a0) -> None:
        data = {'table': 'CompForm'}
        print(net_api.post_sec('/api/info/dict_by_name', data))
        return super().showEvent(a0)
