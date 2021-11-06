from flask import Flask , request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import urllib.request
import json

#表示目前執行模組
app = Flask(__name__) 
#輸入LINE的驗證
line_bot_api = LineBotApi('LINEAPI')
handler = WebhookHandler('LINESERECT')

@app.route("/")
def home():
    return "Hello Flask 2"

@app.route("/test")
def test():
    return "This is Test"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #line_bot_api.reply_message(event.reply_token,TextSendMessage('OK1'))
    #網頁抓取爬蟲資料
    #把發生地震的大小粗列出
    #line_bot_api.reply_message(event.reply_token,TextSendMessage('OK2'))
    if event.message.text=='有地震':
        src = 'get api form gov'
        with urllib.request.urlopen(src) as response:
            data = json.load(response)
        elist = data['records']['earthquake']
        for point in elist:
            plist = point['intensity']['shakingArea']
            qtime = point['earthquakeInfo']['originTime']
            qinfo = point['earthquakeInfo']['epiCenter']
            qcent = point['earthquakeInfo']['depth']
            qman = point['earthquakeInfo']['magnitude']
        inf = '發生時間: ' + str(qtime) + '\n震央: ' + str(qinfo['location']) + '\n深度: ' + str(qcent['value']) + ' 公里' + '\n芮氏規模: ' + str(qman['magnitudeValue']) +'\n'
        adict = {}
        areas = ''
        for area in plist:
            try:
                adict[area['areaIntensity']['value']]
            except:
                adict[area['areaIntensity']['value']] = area['areaName']
            if len(adict[area['areaIntensity']['value']]) < len(area['areaName']):
                adict[area['areaIntensity']['value']] = area['areaName']
        for mkey in adict:
            areas = areas  + '\n' + str(mkey)+ '級地震縣市: '+ '\n' + str(adict[mkey])
        allqinf = inf + areas
        line_bot_api.reply_message(event.reply_token,TextSendMessage(allqinf))
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage('請打"有地震"或是"看天氣"謝謝您~'))

if __name__ == "__main__":
    app.run() 
