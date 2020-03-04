import os
import sys
import gspread

import re
from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser, WebhookHandler
from linebot.exceptions import InvalidSignatureError,LineBotApiError 
from linebot.models import *
from utils import send_text_message
from oauth2client.service_account import ServiceAccountCredentials
import datetime
load_dotenv()

app = Flask(__name__)


adding = False


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
print("line secret  ")
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)
handler = WebhookHandler(channel_secret)

# 監聽所有來自 /callback 的 Post Request
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
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global adding 
    print(event)
    user_id = event.source.user_id
    text=event.message.text
    language = isword(text)
    
    
    if adding   :
        
        if(language=="english"):
            reply_text = "新增單字為英文"
            adding = False
        elif(language=="chinese") :
            reply_text = "新增單字為中文"
            adding = False
        else :
            reply_text = "新增單字為亂碼"
    else :
        if (text=="小幫手"):
            
            buttons_template = ButtonsTemplate(
                title='我是小幫手', text='想要幹嘛呢，要查詢單字請直接輸入文字', actions=[
                    PostbackAction(label='每日五字', data='5word'),
                    PostbackAction(label='新增單字', data='addvoc')
                    
                ])
            template_message = TemplateSendMessage(
                alt_text='請用手機看此訊息！', template=buttons_template)
            line_bot_api.reply_message(event.reply_token,  template_message)
            print("小幫手")
        
            return
            #測試輸入是否為中文
        elif language == "chinese":
            reply_text = "是中文"
            #測試輸入是否為英文
        elif language == "english":
            reply_text = "是英文"
        else:
            reply_text = "亂碼，請重新輸入"
    message = TextSendMessage(reply_text)
    line_bot_api.reply_message(event.reply_token, message)
    
#處裡postback的event
@handler.add(PostbackEvent)
def handle_post_message(event):
    global adding
    print("postback")
    print("event =", event)
    times=5
    user_id = event.source.user_id
    action = text=str(str(event.postback.data))
    try:
    #回傳五個單字
        if action == "5word" :
            for i in range(times):
                line_bot_api.push_message(user_id, 
                    TextSendMessage(text=str(i)))
            return
    #新增單字
        elif action == "addvoc":
            print("addvoc")
            testing = False
            adding = True
            text="你要新增哪個單字呢"
            
        else :
            return
        message = TextSendMessage(text)
        line_bot_api.reply_message(event.reply_token, message)
    except LineBotApiError as e:
        # error handle
        raise e
    
def isword(word) :
    
    if is_all_chinese(word) :
        return "chinese"
    elif  word.encode( 'UTF-8' ).isalpha() :
        return "english"
    else :
        return "error"

def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
