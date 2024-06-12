#!/usr/bin/env python3
# coding:utf-8
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5.Qt import Qt

from Forms.main_window import FormMain
from misc.const import const
from misc.functions import except_hook
from misc.logwriter import LogWriter, flog

if __name__ == "__main__":
    if not const.ok:
        sys.exit(13)

    app = QApplication(sys.argv)
    spl = QSplashScreen(QPixmap(const.splash))
    spl.setWindowFlag(Qt.WindowStaysOnTopHint)
    spl.show()

    sys.excepthook = except_hook
    flog.to_log('Старт программы')
    main_win = FormMain()
    spl.finish(main_win)
    main_win.show()
#    main_win.login_user()
    sys.exit(app.exec())
