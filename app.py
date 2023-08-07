#載入linebot登入資訊
from line_bot_api import *
from events.basic import *
from events.oil import *
app = Flask(__name__)

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
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id #使用者ID

    message_text = str(event.message.text).lower()

    if message_text == '@使用說明':
        about_us_event(event)
        Usage(event)




#————————————————————————————————油價查詢————————————————————————————————————


    if event.message.text =='@油價查詢':
        content = oil_price()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = content))
        


#————————————————————————————————股票————————————————————————————————————

    if event.message.text == '@股價查詢':
        line_bot_api.push_message(uid,TextSendMessage('請輸入#股價代號....'))

#————————————————————————————————查詢————————————————————————————————————



    if event.message.text =='@查詢':
        buttons_template = TemplateSendMessage(
            alt_text='小幫手template',
            template = ButtonsTemplate(
            title = '選擇服務',
            text = '請選擇',
            thumbnail_image_url='https://i.imgur.com/DTX0I3q.jpg',
            actions = [
                MessageTemplateAction(
                        label = '油價查詢',
                        text = '油價查詢'
                ),
                MessageTemplateAction(
                    label = '匯率查詢',
                    text = '匯率查詢'
                ),
                MessageTemplateAction(
                    label = '股價查詢',
                    text = '股價查詢'
                )
            
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token,buttons_template)

    

#————————————————————————————————封鎖提醒————————————————————————————————————
#封鎖後解除封鎖後顯示的訊息

@handler.add(FollowEvent)
def handle_follow(event):
    welcome_msg = """阿是在封鎖三小，不必封鎖又解除餒，滾"""

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text = welcome_msg)
    )
@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print(event)


if __name__ == "__main__":
    app.run()