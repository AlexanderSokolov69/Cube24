#!/usr/bin/env python3
# coding:utf-8
from PyQt5.QtWidgets import QMainWindow

from Forms.main_Form import Ui_MainWindow
from misc.const import const


class FormMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(const.prog_name)