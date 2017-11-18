from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('Ec/+yv3KijdZ3V7lj1IGSFclSCEn5Avq2Ctq8ZySwLaHQH43+kBBEsmMU0ggzdoGvDSn+gxXUg/LadYn4DLRK4vbY6wzz0JwTHEnN1fJvwhjhCG0GdE6C/3I9X+YbW3RP1nc0MSLNSaWufQrn/ttawdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d86151d60f372e05f0fd289ddd3bff68')




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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))



if __name__ == "__main__":
    app.run()



