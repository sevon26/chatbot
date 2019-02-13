from flask import g, jsonify
from application import app
from main import train

import hashlib, random, requests, json


class Lang():
    def __init__(self):
        pass

    @staticmethod
    def translate(text, langtype):
        appKey = '64843ce75da929d6'  # app.config['appKey']
        secretKey = 'Cop2kHaHeEd8kGmYdJSbyiaDAK9ebR0l'  # '#app.config['secretKey']
        q = text
        if langtype == 'en':
            fromLang = 'EN'
            toLang = 'EN'
        elif langtype =='zh-cn':
            fromLang = 'zh-CHS'
            toLang = 'EN'
        elif langtype == 'else':
            fromLang = 'EN'
            toLang = 'zh-CHS'

        fromLang = fromLang # 'zh-CHS'
        toLang = toLang
        salt = random.randint(1, 65536)

        sign2 = appKey + q + str(salt) + secretKey
        sign = hashlib.md5(sign2.encode(encoding='UTF-8')).hexdigest()
        myUrl = 'http://openapi.youdao.com/api' + '?appKey=' + appKey + '&q=' + q + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
            salt) + '&sign=' + sign

        r = requests.get(myUrl)

        data = json.loads(r.text)
        ts = str(data['translation'][0])
        return ts

    @staticmethod
    def getModelReply(text):
        data = train('twitter', 32, 50, 0.001, True, text)
        return data
        
    @staticmethod
    def getModelReply_Cornell(text):
        data = train('cornell', 32, 50, 0.001, True, text)
        return data



