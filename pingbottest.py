from flask import Flask, request
import requests

CQHTTP_URL = "http://127.0.0.1:8003"

def handle_message(event):
    data = request.json
    print(f"message原生data: {data}")
    user_id = event['user_id']
    message_id = event['message_id']
    group_id = data['group_id']
    message = data.get('message')
    print(f"获取到的消息: {message}")

app = Flask(__name__)
# 定义接收事件的路由
@app.route('/callback/', methods=['POST'])
def callback():
    #logging.debug(f"Received request: {request.json}")
    event = request.json
    if event['post_type'] == 'message':
        handle_message(event)
    return 'OK'

# 启动 Flask 应用
if __name__ == '__main__':
    app.run(port=8016)