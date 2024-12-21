#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from json import (
    dumps as json_encode,
    loads as json_decode
)
from re import (
    search as regex_search,
    DOTALL as REGEX_DOTALL
)
from random import (
    choice as random_choice,
    choices as random_choices
)
from concurrent.futures import ThreadPoolExecutor
from uuid import uuid4
from websocket import create_connection
from requests import post
from ssl import CERT_NONE
from gzip import decompress
import pyfiglet
import sys
import time
import os


class TelegramBot:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id= chat_id

    def __REQUEST__(self, method, data):
        try:
            response = post(
                url="https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",
                data={
                    "UrlBox": f"https://api.telegram.org/bot{self.bot_token}/{method}",
                    "ContentTypeBox": "application/json",
                    "ContentDataBox": json_encode(data),
                    "HeadersBox": "",
                    "RefererBox": "",
                    "AgentList": "Custom...",
                    "AgentBox": "Telegram Bot SDK",
                    "VersionsList": "HTTP/1.1",
                    "MethodList": "POST"
                }
            )
            if response.status_code == 200:
                response = response.text
                response = ((json_decode((regex_search(r"<pre[^>]*>(.*?)</pre>", response, REGEX_DOTALL)[1].strip()))))
                return response["result"]
        except Exception:
            pass
        return False

    def SendMessage(self, chat_id, text):
        return self.__REQUEST__("sendMessage", {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "markdown"
        })
    

class SafeUmAccountMaker:
    Ab = '\033[1;92m'
    aB = '\033[1;91m'
    AB = '\033[1;96m'
    aBbs = '\033[1;93m'
    AbBs = '\033[1;95m'
    A_bSa = '\033[1;31m'
    a_bSa = '\033[1;32m'
    faB_s = '\033[2;32m'
    a_aB_s = '\033[2;39m'
    Ba_bS = '\033[2;36m'
    Ya_Bs = '\033[1;34m'
    S_aBs = '\033[1;33m'

    def __init__(self, telegram_bot):
        self.failed = 0
        self.success = 0
        self.retry = 0
        self.accounts = []
        self.uuid = (str(uuid4()))
        self.executor = (ThreadPoolExecutor(max_workers=1000))
        self.telegram_bot = telegram_bot
        self.__Display_Header__()

    def __Display_Header__(self):
        ab = pyfiglet.figlet_format("DedSec\nSafeUm")
        print(self.a_bSa + ab)
        self.__Print_Info__()

    def __Print_Info__(self):
        info = (
            f"\033[1;36mSafeUm Account Maker \n"
            f"\033[1;31m Programmed by >> \033[1;33m@ZELROTH\n"
            f"\033[1;34m Telegram Channel >> \033[1;32m@DedSec_Network\n"
            f"\033[1;37m Github >> \033[1;33mgithub.com/xelroth/\n"  
        )
        self.__To__(info)

    def __To__(self, message):
        for char in message + "\n":
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(500.0 / 8000)

    def __Work__(self):
        username = (random_choice(('qwertyuioplkjhgfdsazxcvbnm')) + ''.join((random_choices((list(('qwertyuioplkjhgfdsazxcvbnm1234567890'))), k=13))))
        try:
            con = create_connection(
                "wss://195.13.182.217/Auth",
                header={
                    "app": "com.safeum.android",
                    "host": None,
                    "remoteIp": "195.13.182.217",
                    "remotePort": str(8080),
                    "sessionId": "b6cbb22d-06ca-41ff-8fda-c0ddeb148195",
                    "time": "2023-04-30 12:13:32",
                    "url": "wss://51.79.208.190/Auth"
                },
                sslopt={"cert_reqs": CERT_NONE}
            )
            con.send(json_encode((self.__Create_Registration_Payload__(username))))
            gzip_response = (decompress((con.recv())).decode('utf-8'))
            self.__Handle_Response__(gzip_response, username)
        except Exception:
            self.retry += 1

    def __Create_Registration_Payload__(self, username):
        return {
            "action": "Register",
            "subaction": "Desktop",
            "locale": "en_IN",
            "gmt": "+05",
            "password": {
                "m1x": "1a07f431a68b4fb69a5c96349137476cca613f019b1016e63a27e022ef09805c",
                "m1y": "ba83a1300f777ada673afb9bc4d507da3000ea2fabaaa35a6616a0af666a4bb7",
                "m2": "43c58959c91b494e05a47cad7bca5b5f52e5204d393e06829c34884fa807954b",
                "iv": "140c409aba2f6c7050518a826e6f2810",
                "message": "5080dc99f8e226891ee1f4b52a480e1d0278ff1c211e5107a5de2ceb6a646d407084bd88f05438f6f671e2574239abbe68b401980a9336947e0b47c5e56bbcf05ad345cd46958d090bdd9110fdd33b08"
            },
            "magicword": {
                "m1x": "e90328d307cc09e8efb4bc307b93711c30ddc8dd2c81a4375a8c6f56cc491b6c",
                "m1y": "c10d0ea9f845ede4e3bddabd688b5a5df39e0542a9f7e3d3e634a0c947eb7cef",
                "m2": "0743248643a4ce7fe349e117aadc8bf6b98361410d9ee87b4a8b7519ddf421d5",
                "iv": "186e765c4b10803fc9a6a9d6ae08549b",
                "message": "76f4c2466364ccf3bd38882471fc30c3"
            },
            "magicwordhint": "0000",
            "login": str(username),
            "devicename": "Xiaomi 220733SPH",
            "softwareversion": "1.1.0.1548",
            "nickname": "jsjkkm822mmsm",
            "os": "AND",
            "deviceuid": "3933b21c103ad7a8",
            "devicepushuid": "*fC4qytGbRgCLyGKiZRfh5n:APA91bFXieRxcxPxIyxknU-MNLUyrao13YgiKV_tthXzXVLToRz8-t6LkU2Zol8cW7jhcfQp10h0n0VyZw4vOY04HWS5fIXGX-ic_1ijzt3RGbKUBCEkqAg",
            "osversion": "and_12.0.0",
            "id": "1492923070"
        }

    def __Handle_Response__(self, response, username):
        if ('"status":"Success"') in response:
            self.success += 1
            self.accounts.append((username))
            self.__Save_Account__(username)
            print(f"Account Created: {username}")
            telegram_bot.SendMessage((chat_id), (f"🎉 Account Created: {username}🎉\n"))
        else:
            self.failed += 1

    def __Save_Account__(self, username):
        with open(f"{self.uuid}_hits.txt", 'a') as f:
            f.write(username + "\n")

    def __Start_Work__(self):
        while True:
            self.executor.submit(self.__Work__)
            self.__Display_Status__()
            (os.system(("cls"))) if "nt" in (os.name) else (os.system(("clear")))

    def __Display_Status__(self):
        print(('\n\n\n'
        + ' ' * 25 + 'Session ID : ' + ((self.uuid)) + '\n\n\n' +
        + ' ' * 25 + 'Success : ' + (str(((self.success)))) + '\n\n\n' +
              ' ' * 25 + 'Failed : ' + (str(((self.failed)))) + '\n\n\n' +
              ' ' * 25 + 'ReTry : ' + (str(((self.retry))))
        ))
        if (self.success) > 1:
            print("Account Generated>>\n", (("\n".join((self.accounts)))))

if __name__ == "__main__":
    bot_token = ''
    chat_id = ''
    telegram_bot = (TelegramBot((bot_token), (chat_id)))
    account_maker = (SafeUmAccountMaker(telegram_bot))
    account_maker.__Start_Work__()
