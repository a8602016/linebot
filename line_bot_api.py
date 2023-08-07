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