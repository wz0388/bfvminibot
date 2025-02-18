from flask import Flask, request
import requests
import logging
CQHTTP_URL = 'http://127.0.0.1:8003'
TVbotcx = {}
def handle_message(event):
    data = request.json
    user_id = event['user_id']
    message_id = event['message_id']
    group_id = data['group_id']
    message = data.get('message')
    #print(f"获取到的消息: {message}")
    if message.strip().startswith("/pl"):
        target_user_id = int(message.split()[1])
        TVbotcx[user_id]['status'] == 'waiting_for_TVbot'
        TVbotcx[user_id]['message_id'] == message_id
        TVbotcx[user_id]['group_id'] == group_id
        send_group_message(935114950, f"[CQ:at,qq=3889013937] /playerlist {target_user_id}")
    
    elif 'CQ:image' in message and user_id == 3889013937:
        name_start = message.find('file=') + 5
        name_end = message.find(',', name_start)
        file_temp_name = message[name_start:name_end]
        #logging.debug(f"提取到的文件名: {file_temp_name}")
        # 获取图片的URL
        image_path = get_image_info(file_temp_name)
        send_group_message(282850241, f"[CQ:image,file=file:///{image_path}]")

def send_group_message(group_id, message):
    url = f"{CQHTTP_URL}/send_group_msg"
    data = {
        'group_id': group_id,
        'message': message
    }
    response = requests.post(url, json=data)


def get_image_info(filename):
    url = f"{CQHTTP_URL}/get_image"
    data = {'file': filename}
    response = requests.post(url, json=data)
    data23 = response.json()
    file_store = data23['data']['file']
    #print(f"获取图片本地地址: {file_store}")
    return file_store


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