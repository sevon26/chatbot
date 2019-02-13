from wxpy import *
from flask import g
import json, datetime
from common.lang import Lang
from langdetect import detect
import asyncio

bot = Bot(cache_path="logoo.pkl")
my_friend = bot.friends().search('李婧媛')[0]
my_friend.send('start test')

loop = asyncio.get_event_loop()

@bot.register(my_friend,msg_types=TEXT)
def auto_reply(msg):
    loop.run_until_complete(send_msg(msg))

async def send_msg(msg):
    langtype = detect(msg.text)
    tr_text = Lang.translate(msg.text, langtype)
    text = Lang.getModelReply(tr_text)
    text = Lang.translate(text, langtype)
    msg.reply(text)


    '''
    text = msg.text
    detect_result = detect(text)
    print(text,detect_result)
    if detect_result == 'en':
        text_en = Lang.getModelReply(msg.text)
        msg.reply(text_en)
    elif detect_result == 'zh-cn':
        tr_text = Lang.translate(text, 'zh-CHS', 'EN')
        text_ch = Lang.getModelReply(tr_text)
        text_ch = Lang.translate(text, 'EN', 'zh-CHS')
        msg.reply(text_ch)
        '''

