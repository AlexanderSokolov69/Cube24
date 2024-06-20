#!/usr/bin/env python3
# coding:utf-8
import jwt
from requests import post

from misc.const import const
from misc.functions import msg_window
from misc.logwriter import flog


class NetApiConnect:
    def __init__(self):
        self.token = None
        self.decoded_token = None
        self.user = []
        self.current_year = 2024
        self.connect_string = f'http://{const.srv_addr}:{const.srv_port}'
        self.timeout = int(const.timeout_req)

    def post(self, path='', data={}):
        response = {}
        try:
            response = post(f'{self.connect_string}{path}',
                            json=data, timeout=self.timeout).json()
            token = response.get('token', None)
            if token is not None:
                self.token = token
        except Exception:
            msg_window(text='Соединение с сервером не удалось!')
            flog.to_log(f"Ошибка подключения к серверу: {Exception}")

        if self.token:
            self.decoded_token = self.decode_token()
            if self.decoded_token:
                self.user = self.decoded_token['user']
        else:
            msg_window(text=response.get('message', 'Неизвестная ошибка!'))
        return response

    def post_sec(self, path='', data={}):
        response = {}
        if self.token:
            headers = {'Authorization': 'Bearer ' + self.token}
            try:
                response = post(f'{self.connect_string}{path}',
                                headers=headers,
                                json=data,
                                timeout=self.timeout).json()
                token = response.get('token', None)
                if token is not None:
                    self.token = token
            except Exception:
                msg_window(text='Соединение с сервером не удалось!')
                flog.to_log(f"Ошибка подключения к серверу: {Exception}")
        else:
            return {'message': 'token is None'}
        return response

    def decode_token(self):
        token = None
        try:
            algorithm = jwt.get_unverified_header(self.token).get('alg')
            token = jwt.decode(self.token, key=const.jwt_key, algorithms=algorithm)
        except Exception:
            flog.to_log(f'token decode Error: {Exception}')
        return token


net_api = NetApiConnect()
