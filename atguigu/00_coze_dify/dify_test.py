import requests

DIFY_API_KEY = "app-XL6aWPFbtpjBa8WWFkUWQI42"
DIFY_URL = "https://api.dify.ai/v1/workflows/run"
headers = {
    "Authorization": f"Bearer {DIFY_API_KEY}",
    "Content-Type": "application/json"
}
payload = {
    "inputs": {
        "feedback":"客服态度恶劣"
    },
    "response_mode": "blocking",
    "user": "abc-123"
}

def run_dify_workflow_block():
    resp = requests.post(DIFY_URL, json=payload, headers=headers)
    resp.raise_for_status()
    result = resp.json()
    print("完整返回结果：", result)

if __name__ == "__main__":
    run_dify_workflow_block()