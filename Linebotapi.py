import json
import requests

Channel_access_token = 'MEHHmo0chIX8ldVTNcHXeVw5XSjhlFY7jWcOCGf/w0aaWk3qfCKG3uGAfEBrFKNPp2vwgnxbni2tvWMr+hzRD7BMEx2fPlpHq5ouPfR6BDtltkcyuvkkh8ledsXWO6VTMhWD4X7nmuk4YDLF0PLGJwdB04t89/1O/w1cDnyilFU='

def ReplyMessageTest(Reply_token,Message):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  Authorization = 'Bearer {}'.format(Channel_access_token)
  headers = {
      'Content-Type': 'application/json; charset=UTF-8',
      'Authorization': Authorization
  }
  data = {
        "replyToken": Reply_token,
        "messages": [
                      {
                          "type":"text",
                          "text":Message
                      },
                    ]
        }
  data = json.dumps(data)  ## dump dict >> Json Object
  r = requests.post(LINE_API, headers=headers, data=data)



def PushMessage(userid,msg):
  LINE_API = 'https://api.line.me/v2/bot/message/push'
  Authorization = 'Bearer {}'.format(Channel_access_token)
  headers = {
      'Content-Type': 'application/json; charset=UTF-8',
      'Authorization': Authorization
  }

  Message = {
    "to": userid,
    "messages": [
        {
          "type": "text",
          "text": msg
        }
    ]
  }

  data = Message
  data = json.dumps(data)  ## dump dict >> Json Object
  r = requests.post(LINE_API, headers=headers, data=data)


def ReplyMessage(Reply_token,Message):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  Authorization = 'Bearer {}'.format(Channel_access_token)
  headers = {
      'Content-Type': 'application/json; charset=UTF-8',
      'Authorization': Authorization
  }
  data = {
        "replyToken": Reply_token,
        "messages": [
                      {
                          "type":"text",
                          "text":Message
                      },
                    ]
        }
  data = json.dumps(data)  ## dump dict >> Json Object
  r = requests.post(LINE_API, headers=headers, data=data)




def QuickReplyyMessage(Reply_token):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  Authorization = 'Bearer {}'.format(Channel_access_token)
  headers = {
      'Content-Type': 'application/json; charset=UTF-8',
      'Authorization': Authorization
  }
  data = {
          "replyToken": Reply_token,
          "messages": [
            {
            "type": "text",
            "text": "ปุ่มตอบกลับแบบรวดเร็ว",
            "quickReply": {
              "items": [
                        {
                          "type": "action",
                          "action": {
                                    "type":"message",
                                    "label":"ข้อความ1",
                                    "text":"TEXT1"
                                    }
                        },
                        {
                          "type": "action",
                          "action": {
                                    "type":"message",
                                    "label":"ข้อความ2",
                                    "text":"TEXT2"
                                    }
                        }
                      ]
                }
            }
          ]
        }
  data = json.dumps(data)  ## dump dict >> Json Object
  r = requests.post(LINE_API, headers=headers, data=data)


def ReplyMessageFlex(Reply_token, TextMessage):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'

  Authorization = 'Bearer {}'.format(Channel_access_token)
  headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
  }

  data = {
        "replyToken": Reply_token,
        "messages": [{
            "type": "flex",
            "altText": "this is a flex message",
            "contents": {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": TextMessage
                        }
                    ]
                }
            }
        }],
    }
  data = json.dumps(data)  ## dump dict >> Json Object
  r = requests.post(LINE_API, headers=headers, data=data)
  return 200



def ReplyMessageBubble(Reply_token):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'

  Authorization = 'Bearer {}'.format(Channel_access_token)
  headers = {
              'Content-Type': 'application/json; charset=UTF-8',
              'Authorization': Authorization
          }

  data = {
        "replyToken": Reply_token,
        "messages": [
            {
                "type": "flex",
                "altText": "Flex Message",
                "contents": {
                    "type": "bubble",
                    "direction": "ltr",
                    "footer": {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "OK",
                                    "text": "ok"
                                }
                            }
                        ]
                    }
                }
            }
        ]
    }

  data = json.dumps(data)  ## dump dict >> Json Object
  r = requests.post(LINE_API, headers=headers, data=data)


def ReplyMessageCarousel(Reply_token):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'

  Authorization = 'Bearer {}'.format(Channel_access_token)
  headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
  }
  data = {
        "replyToken": Reply_token,
        "messages": [{
            "type": "flex",
            "altText": "Flex Message",
            "contents": {
                "type": "carousel",
                "contents": [
                    {
                        "type": "bubble",
                        "direction": "ltr",
                        "footer": {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "message",
                                        "label": "OK 1",
                                        "text": "OK1"
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "type": "bubble",
                        "direction": "ltr",
                        "footer": {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "message",
                                        "label": "OK 2",
                                        "text": "OK2"
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "type": "bubble",
                        "direction": "ltr",
                        "footer": {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "message",
                                        "label": "OK 3",
                                        "text": "OK3"
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }],
    }

  data = json.dumps(data)  ## dump dict >> Json Object
  r = requests.post(LINE_API, headers=headers, data=data)






def CreateRichmenu():
  LINE_API = 'https://api.line.me/v2/bot/richmenu'

  Authorization = 'Bearer {}'.format(Channel_access_token)
  headers = {
              'Content-Type': 'application/json; charset=UTF-8',
              'Authorization': Authorization
            }

  data = {
        "size": {
            "width": 2500,
            "height": 1686
        },
        "selected": False,
        "name": "LINE Developers Info",
        "chatBarText": "Tap to open",
        "areas": [
            {
                "bounds": {
                    "x": 34,
                    "y": 24,
                    "width": 169,
                    "height": 193
                },
                "action": {
                    "type": "uri",
                    "uri": "https://developers.line.biz/en/news/"
                }
            },
            {
                "bounds": {
                    "x": 229,
                    "y": 24,
                    "width": 207,
                    "height": 193
                },
                "action": {
                    "type": "uri",
                    "uri": "https://www.line-community.me/"
                }
            },
            {
                "bounds": {
                    "x": 461,
                    "y": 24,
                    "width": 173,
                    "height": 193
                },
                "action": {
                    "type": "flex",
                    "altText": "LINE Developers Site More Options",
                    "contents": {
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "url": "devSiteImageUrl",
                            "size": "full",
                            "margin": "none",
                            "gravity": "top",
                            "aspectRatio": "1200:630"
                        }
                    }
                }
            }
        ]
  }

  data = json.dumps(data)  ## dump dict >> Json Object
  r = requests.post(LINE_API, headers=headers, data=data)




def UploadRichmenu(richmenu_id):
  LINE_API = 'https://api-data.line.me/v2/bot/richmenu/{}/content'.format(richmenu_id)

  Authorization = 'Bearer {}'.format(Channel_access_token)
  headers = {
              'Content-Type': 'image/jpeg',
              'Authorization': Authorization
            }

  data = {}
  data = json.dumps(data)  ## dump dict >> Json Object
  r = requests.post(LINE_API, headers=headers, data=data)

