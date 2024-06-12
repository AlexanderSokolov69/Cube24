#!/usr/bin/env python3
# coding:utf-8
import typing

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QMainWindow, QMdiSubWindow, QWidget, QMdiArea

from Forms.login_window import FormLoginWindow
from Forms.main_Form import Ui_MainWindow
from Forms.test import Ui_Form
from Forms.test_window import TestForm
from misc.const import const


class FormMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(const.prog_name)
        self.mdiArea.setAttribute(Qt.WA_DeleteOnClose, True)
        self.mdiArea.subWindowActivated.connect(self.mdi_activated)
        self.mdiArea.destroyed.connect(self.signal)
        self.win = FormLoginWindow()

        self.test_wind = TestForm()
        self.test_wind.setObjectName('TEST')

        self.test_wind2 = TestForm()
        self.test_wind2.setObjectName('TEST2')

        self.action_dict.triggered.connect(lambda x: self.mdi_append_window(self.test_wind))
        self.action.triggered.connect(lambda x: self.mdi_append_window(self.test_wind2))

    def login_user(self):
        if not self.win.user:
            self.win.show()

    def event(self, event: typing.Optional[QtCore.QEvent]) -> bool:
        if event.type() == QEvent.WindowActivate:
            if not self.win.user:
                # print('User пустой')
                self.win.show()
                # print('Окно login активно!')
            else:
                print(self.win.user)
                self.login.setText(self.win.user.get('login', 'login'))
                self.user_name.setText(self.win.user.get('name', 'UserName'))
                self.current_year.setValue(self.win.current_year)
        return super().event(event)

    def mdi_append_window(self, win_obj: QWidget):
        spw = self.mdiArea.subWindowList()
        for obj in spw:
            if obj.widget().objectName() == win_obj.objectName():
                self.mdiArea.cascadeSubWindows()
                obj.widget().showMaximized()
                break
        else:
            wind_mdi = QMdiSubWindow()
            wind_mdi.setWidget(win_obj)
            self.mdiArea.addSubWindow(wind_mdi)
            win_obj.showMaximized()

    def mdi_activated(self, wind):
        print('!!!', wind)

    def signal(self):
        print('destroy')


