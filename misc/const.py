#!/usr/bin/env python3
# coding:utf-8
from configparser import ConfigParser


class Const:
    def __init__(self, name='settings.ini'):
        self.ok = True
        try:
            cfg = ConfigParser()
            cfg.read(name, encoding='utf8')
            self.prog_name = cfg.get("Main", "prog_name")

            self.srv_addr = cfg.get("Server", "srv_addr")
            self.srv_port = cfg.get("Server", "srv_port")

            self.splash = cfg.get('Settings', 'splash')
        except Exception:
            print(f'Ошибка чтения файла параметров: {Exception}')
            self.ok = False


const = Const()
