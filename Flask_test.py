'''
This Project make by Sarawut nacwijit

Messaging API
https://developers.line.biz/en/services/messaging-api/
https://developers.line.biz/en/docs/messaging-api/overview/#what-you-can-do
https://manager.line.biz/

Ngrok
https://ngrok.com/download
'''

from flask import Flask, send_file, render_template, request
from flask_cors import CORS
from pathlib import Path
import Linebotapi as bot


# Create the application instance
app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')
app.url_map.strict_slashes = False
cors = CORS(app, resources={r"*": {"origins": "*"}})

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = str(Path(__file__).parent)

# Create a URL route in our application for "/"
@app.route('/')
def hello():
    return "<h1> Hello World. </h1>" ,200

# return Json
@app.route('/test', methods=['GET'])
def test():
    return {"reply":"test"} ,200

# return file in local
@app.route('/getimage', methods=['GET'])
def get_image():
    filename = BASE_DIR + "/templates/test.png"
    return send_file(filename) ,200


@app.route('/gethtml', methods=['GET'])
def get_html():
    filename = "/templates/test.html"
    return send_file("templates/test.html") ,200


@app.route('/API', methods=['GET', 'POST'])
def parse_request():
    header = request.headers
    print(header)
    data = request.json
    print(data)
    return {"test":True} ,200


@app.route('/user/<username>')
def profile(username):
    return "username's {}.".format(username) ,200



@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    if request.method == 'POST':
        payload = request.json
        print("----------")
        print(payload)
        print("----------")

        if payload['events'] == []:
            print("Verify Webhook.")
        else:
            Reply_token = payload['events'][0]['replyToken']
            type_message = payload['events'][0]['message']['type']
            messageID = payload['events'][0]['message']['id']
            userID = payload['events'][0]['source']['userId']

            print("[Reply_token] ", Reply_token)
            print("[type_message] ", type_message)
            print("[messageID] ", messageID)
            print("[ userID ] ", userID)

            if type_message == 'text':
                message = payload['events'][0]['message']['text']
                if "test" == message:
                    bot.ReplyMessage(Reply_token,"test")
                elif "ทดสอบ" == message:
                    bot.ReplyMessage(Reply_token,"ทดสอบ")
                elif "msg0" == message:
                    bot.ReplyMessage(Reply_token,"TEXT REPLY")
                elif "msg1" == message:
                    bot.PushMessage(userID,"TEXT PUSH")
                elif "msg2" == message:
                    bot.QuickReplyyMessage(Reply_token)
                elif "msg3" == message:
                    bot.ReplyMessageFlex(Reply_token,"TEXT")
                elif "msg4" == message:
                    bot.ReplyMessageBubble(Reply_token)
                elif "msg5" == message:
                    bot.ReplyMessageCarousel(Reply_token)
                elif "msg6" == message:
                    bot.ReplyMessageRichmenu(Reply_token)
                else:
                    bot.ReplyMessage(Reply_token,'Bot ยังไม่สามารถตอบกลับได้ในขณะนี้ ขอบคุณที่เข้ามาคุยกันน่ะครับ')

            if type_message == 'image':
                msg = 'ยังไม่สามารถรับรู้รูปภาพได้ในขณะนี้'
                bot.ReplyMessage(Reply_token, msg)

            if type_message == 'video':
                msg = 'ยังไม่สามารถรับรู้วีดีโอได้ในขณะนี้'
                bot.ReplyMessage(Reply_token, msg)

            if type_message == 'audio':
                msg = 'ยังไม่สามารถรับรู้เสียงได้ในขณะนี้'
                bot.ReplyMessage(Reply_token, msg)

            if type_message == 'file':
                msg = 'ยังไม่สามารถรับรู้ไฟล์ได้ในขณะนี้'
                bot.ReplyMessage(Reply_token, msg)

            if type_message == 'location':
                msg = 'ยังไม่สามารถรับรู้สถานที่ได้ในขณะนี้'
                bot.ReplyMessage(Reply_token, msg)
        return {"msg":"This Webhook."}, 200

    elif request.method == 'GET':
        return 'this is method GET!!!', 200
    else:
        abort(400)


if __name__ == '__main__':
    # app.run(port=8000)     #localhost:8000/
    app.run(debug=True)     #localhost:5000/

