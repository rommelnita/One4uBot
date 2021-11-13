# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.

import asyncio
from asyncio import wait, sleep

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.events import register
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
import sys
import traceback
import time
import random
import re

api_id = 8432622  # API ID
api_hash = '1911d40c63e90803fc62d64f1678b9a3'  #API HASH
phone = '+6282246498229'  #NUMBER WITH COUNTRY CODE
timer = 120 #TIME TO WAIT BEFORE NEXT SENDING
msgtosend = "Metpagi" # MESSAGE TO SEND
client = TelegramClient(phone, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))
chats = []
last_date = None
chunk_size = 10
groups=[]
result = client(GetDialogsRequest(
                offset_date=last_date,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=chunk_size,
                hash = 0
            ))
chats.extend(result.chats)
for chat in chats:
    try:
        groups.append(chat)
    except:
        continue
while True:    
    for group in groups:
        try:
            username1 = group.username
            print(username1)    
            client.send_message(username1, msgtosend)
            time.sleep(1)
        except:
            continue 
    print("Send Complete!!, Waiting for " + str(timer) + " seconds")
    time.sleep(timer)
