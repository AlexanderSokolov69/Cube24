#!/usr/bin/env python3
# coding:utf-8
from PyQt5.QtWidgets import QWidget

from Forms.test import Ui_Form


class TestForm(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
