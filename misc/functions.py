#!/usr/bin/env python3
# coding:utf-8
import sys
import traceback as tb

from PyQt5.QtWidgets import QMessageBox

from misc.logwriter import flog


def except_hook(cls, exception, traceback):
    flog.to_log(f"""{exception} | \n{tb.format_tb(traceback)[0]}""")
    sys.__excepthook__(cls, exception, traceback)


def msg_window(title='Сообщение', text='Сообщение о событии!', count=1):
    box = QMessageBox()
    box.setWindowTitle(title)
    box.setText(text)
    box.setStandardButtons(QMessageBox.Ok)
    box.exec_()


