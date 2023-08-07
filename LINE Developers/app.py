#載入LineBot所需要的套件
from flask import Flask,request,abort
from linebot import(LineBotApi,WebhookHandler,exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

app = Flask(__name__)

#必須放上自己的Channel Access Token
line_bot_api = LineBotApi('aE+7rF3FLH5GxkNamQ2qJTDFQx01Z41U7h6eIkwilfYWXe+wV7OhnCImFr3Yv8/sPr9O85t39mEpIrB0cUL3g9cAKjaWt3NPzJgBgfft+tvqv5Jp5l9NluEZorWbSbQ/mAzdr9/Y2ofFHaOmeK+/PAdB04t89/1O/w1cDnyilFU=')
#必須放上自己的Channel Secret
handler = WebhookHandler('fe27da6a009efaf74192b337b47e14eb')

#監聽所有來callback的 Post Request
@app.route("/callback",methods = ['POST'])
def callback():
    # get X-LineSignature header value
    Signature = request.headers['x-Line-Signature']

    # get request body as text
    body = request.get_data(as_text = True)
    app.logger.info('Request body:'+body)

    # handle webhook body
    try:
        handler.handle(body,Signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

#處理訊息
@handler.add(MessageEvent,message=TextMessage)
def handle_message(event):
    #文字訊息格式
    message = TextSendMessage(text = event.message.text)
    line_bot_api.reply_message(event.reply_token,message)

if __name__ == "__main__":
    app.run()