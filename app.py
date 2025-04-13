from flask import Flask, request
# 载入 json 标准函式库，处理回传的资料格式
import json
import os
from dotenv import load_dotenv
# 载入 LINE Message API 相关函式库
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageMessage, FileMessage

# 加载环境变量
load_dotenv()

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)  # 取得收到的讯息内容
    try:
        json_data = json.loads(body)  # json 格式化讯息内容
        
        # 从环境变量获取凭证
        access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
        secret = os.getenv('LINE_CHANNEL_SECRET')
        
        line_bot_api = LineBotApi(access_token)  # 确认 token 是否正确
        handler = WebhookHandler(secret)  # 确认 secret 是否正确
        signature = request.headers['X-Line-Signature']  # 加入回传的 headers
        handler.handle(body, signature)  # 绑定讯息回传的相关资讯
        
        # 获取事件类型
        event_type = json_data['events'][0]['type']
        
        # 如果不是讯息事件，则跳过
        if event_type != 'message':
            return 'OK'
        
        # 获取回传讯息的 Token 和讯息类型
        tk = json_data['events'][0]['replyToken']
        type = json_data['events'][0]['message']['type']
        
        # 获取发送者信息
        source_type = json_data['events'][0]['source']['type']
        source_info = ""
        
        if source_type == 'user':
            user_id = json_data['events'][0]['source']['userId']
            source_info = f"用户ID: {user_id}"
        elif source_type == 'group':
            group_id = json_data['events'][0]['source']['groupId']
            if 'userId' in json_data['events'][0]['source']:
                user_id = json_data['events'][0]['source']['userId']
                source_info = f"群组ID: {group_id}, 用户ID: {user_id}"
            else:
                source_info = f"群组ID: {group_id}, 用户ID: 未知"
        elif source_type == 'room':
            room_id = json_data['events'][0]['source']['roomId']
            if 'userId' in json_data['events'][0]['source']:
                user_id = json_data['events'][0]['source']['userId']
                source_info = f"聊天室ID: {room_id}, 用户ID: {user_id}"
            else:
                source_info = f"聊天室ID: {room_id}, 用户ID: 未知"
        
        # 根据讯息类型处理
        if type == 'text':
            msg = json_data['events'][0]['message']['text']  # 取得 LINE 收到的文字讯息
            print(f"收到文字讯息: {msg}")
            print(f"讯息来源: {source_type} - {source_info}")
            reply = f"我收到了你的文字: {msg}\n来源: {source_type}\n{source_info}"
            
        elif type == 'image':
            print(f"收到图片")
            print(f"讯息来源: {source_type} - {source_info}")
            reply = f"我收到了你的图片\n来源: {source_type}\n{source_info}"
            
        elif type == 'file':
            # 获取文件名称(如果有)
            file_name = json_data['events'][0]['message'].get('fileName', '未知文件')
            print(f"收到文件: {file_name}")
            print(f"讯息来源: {source_type} - {source_info}")
            reply = f"我收到了你的文件: {file_name}\n来源: {source_type}\n{source_info}"
            
        else:
            reply = f"我收到了一个{type}类型的讯息\n来源: {source_type}\n{source_info}"
            print(f"收到{type}类型讯息")
            print(f"讯息来源: {source_type} - {source_info}")
        
        # 回传讯息
        line_bot_api.reply_message(tk, TextSendMessage(reply))
        
    except Exception as e:
        print(f"发生错误: {str(e)}")
        print(f"原始请求体: {body}")  # 如果发生错误，印出收到的内容
        
    return 'OK'  # 验证 Webhook 使用，不能省略

@app.route("/", methods=['GET'])
def index():
    return "LINE Webhook 服务正在运行!"

if __name__ == "__main__":
    app.run(debug=True, port=5000)