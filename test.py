from flask import Flask, request, abort
import requests
import re
import random
import configparser
import urllib.request
import urllib.parse
import re


from bs4 import BeautifulSoup
from imgurpython import ImgurClient

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi('Ec/+yv3KijdZ3V7lj1IGSFclSCEn5Avq2Ctq8ZySwLaHQH43+kBBEsmMU0ggzdoGvDSn+gxXUg/LadYn4DLRK4vbY6wzz0JwTHEnN1fJvwhjhCG0GdE6C/3I9X+YbW3RP1nc0MSLNSaWufQrn/ttawdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d86151d60f372e05f0fd289ddd3bff68')

client_id = "9824999341e0ca8"
client_secret = "0fa7e0f509b09a78a1c88e435b0ed0ff0c0a0cc1"
access_token = "2606dc43c96cddd87b3871a62982b768f03baaa0"
refresh_token = "49cafcc77f21770efe63dc60b681364633191571"

client = ImgurClient(client_id, client_secret, access_token, refresh_token)


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


@app.route('/index')
def index():
    data = "Deploying a Flask App To Heroku"
    return data

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "來張圖片":
        url = "https://i.imgur.com/pd9if76.png"
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        line_bot_api.reply_message(
            event.reply_token, image_message)
        return 0
    #if event.message.text == "微胖型女孩":
       # url = "https://i.imgur.com/fLd61II.png"
     #   image_message = ImageSendMessage(
      #      original_content_url=url,
       #     preview_image_url=url
        #)
        #line_bot_api.reply_message(
         #   event.reply_token, image_message)
        #return 0
    if event.message.text == "正妹":   
        url="https://i.imgur.com/Gi2dgAV.jpg"
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        line_bot_api.reply_message(
            event.reply_token, image_message)
        return 0
    if event.message.text == "抽正妹":
        images = client.get_album_images('bgZsu')
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        line_bot_api.reply_message(
            event.reply_token, image_message)
        return 0
    if event.message.text == "抽帥哥":
        images = client.get_album_images('HahMV')
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        line_bot_api.reply_message(
            event.reply_token, image_message)
        return 0

    if event.message.text == "抽帥狗":
        images = client.get_album_images('3VZcD')
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        line_bot_api.reply_message(
            event.reply_token, image_message)
        return 0
    if '點歌-' in event.message.text:
        a,b = event.message.text.split("-")
        query_string = urllib.parse.urlencode({"search_query" : b})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        print("http://www.youtube.com/watch?v=" + search_results[0])
        line_bot_api.reply_message(
          event.reply_token,
          TextSendMessage("http://www.youtube.com/watch?v=" + search_results[0]))
    if '吃什麼' in event.message.text:
        foo = ['粹義', '九尾', '主廚蓋飯', '鼎香酸辣粉','名廚','泰之雲','洪師傅','mos burger','火鍋','韓式料理']
        secure_random = random.SystemRandom()
        res = secure_random.choice(foo)
        line_bot_api.reply_message(
           event.reply_token,
           TextSendMessage(text=res))
   # else:
    #    line_bot_api.reply_message(
     #     event.reply_token,
      #    TextSendMessage(text=event.message.text))



if __name__ == "__main__":
    app.run()



