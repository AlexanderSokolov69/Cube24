#!/usr/bin/env python3
# coding:utf-8
from datetime import datetime

from PyQt5.QtCore import QObject


class LogWriter(QObject):
    def __init__(self, fname='errorlog.txt'):
        super(LogWriter, self).__init__()
        self.fname = fname

    def to_log(self, message):
        timestamp = datetime.now()
        with open(self.fname, 'a', encoding='utf8') as f:
            f.write(f"""{timestamp} ==> {message}\n<===\n""")
