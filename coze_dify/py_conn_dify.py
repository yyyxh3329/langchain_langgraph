import requests
import json


def run_dify_workflow():
    url = "https://api.dify.ai/v1/workflows/run"

    headers = {
        "Authorization": "Bearer app-1QistAJjErsh1XCwupLpROnB",  # 请替换为您的实际 API Key
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": {
            'feedback':'这个衣服掉色，质量好差'
        },
        "response_mode": "streaming",
        "user": "abc-123"
    }

    # 发送 POST 请求
    response = requests.post(url, headers=headers, json=payload, stream=True)

    # 处理流式响应
    if response.status_code == 200:
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                if decoded_line.startswith('data: '):
                    data = json.loads(decoded_line[6:])
                    print(data)
    else:
        print(f"请求失败，状态码：{response.status_code}")
        print(response.text)


# 调用函数
run_dify_workflow()

