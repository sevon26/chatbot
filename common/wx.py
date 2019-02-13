from wxpy import *
from flask import g
import json, datetime
from common.lang import Lang
from langdetect import detect
import asyncio
import os,time
import cv2
import numpy as np
bot = Bot()
my_friend = bot.friends().search('李婧媛')[0]
#my_friend = bot.friends().search('David')[0]
#my_friend.send('Start Test')


loop = asyncio.get_event_loop()

@bot.register(my_friend,msg_types=TEXT)
def auto_reply(msg):
    loop.run_until_complete(send_msg(msg))

async def send_msg(msg):
        tr_text = msg.text
        langtype = detect(msg.text)
        print(langtype)
        input_text = Lang.translate(msg.text, 'zh-cn')
        print(input_text)
        text_tmp = Lang.getModelReply(input_text)
        print(text_tmp+'模型输出')
        if langtype == 'zh-cn' or langtype ==  'ko':
            output_text = Lang.translate(text_tmp, 'else')
            print(output_text,'中文输出')
        else :
            output_text = text_tmp
            print('其他语言输出')
        msg.reply(output_text)
        
@bot.register(my_friend,msg_types=PICTURE)
def face_msg(msg):
    print(msg.file_name)
#    random_int = np.random.random_integers(0,10)
    random_int = np.random.random_integers(0,10)
    name = str(random_int)
    filename = 'test'+name+'.jpg'
    print(filename)
    msg.reply_image(filename)
    
    
@bot.register(my_friend,msg_types=RECORDING)
def voice_msg(msg):
    msg.reply('不懂你在说什么，好好交流好吗？')
    
@bot.register(my_friend,msg_types=MAP)
def voice_msg(msg):
    msg.reply('不懂你在说什么，好好交流好吗？')
    

    

#    image = msg.get_file(save_path=None)
#    cv2.imshow(image)
#    cv2.imread(msg.file_name)
#    cv2.imwrite('111111.jpg',msg.file_name)
##    print(type(msg.chat))
##    msg.get_file(save_path='/Users/david/Downloads/seq2seq-chatbot/common')
#    msg.reply_image('test3.jpg')

#    image_name = msg.file_name
#    friend = msg.chat
#    print (msg.chat)
#    print ('接收图片')
#    # face(image_name)
#    msg.get_file('' + msg.file_name)
#    count = face(image_name)
#    if count==0:
#        msg.reply(u'未检测到人脸')
#    else:
#        msg.reply_image("face_detected_1.jpg")
#        msg.reply(u"检测到%d张人脸"%count)
#    os.remove(image_name)
#    os.remove("face_detected_1.jpg")
# 
#embed()

    
#    tr_text = msg.text
#    langtype = detect(msg.text)
#    print(langtype)
#    if langtype == 'zh-cn' or 'ko' :
#        print(msg.text)
#        tmp_text = Lang.translate(tr_text, 'zh-cn')
#        print(tmp_text+'1')
#        De_text = Lang.getModelReply(tmp_text)
#        print(tmp_text+'2')
#        text_out = Lang.translate(De_text, 'else')
#        print(text_out)
#    if langtype == 'en':
#        print(msg.text)
#        print('En mode')
#        text_out = Lang.getModelReply(tr_text)
#        print(text_out)
#    msg.reply(text_out)
