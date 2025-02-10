import json

import requests


class linguistic:
    def __init__(self):
        # self.access_token = self.get_access_token()
        pass

    def get_access_token(self):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        API_KEY = "UsguVpG6UcsP4fyk15uDnFvf"
        API_SECRET = "mPuKsTRrsvyWJcvzzBsXrkjXqY7UoJLv"
        url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={API_KEY}&client_secret={API_SECRET}"

        payload = ""
        returndata = requests.post(url, headers=headers, data=payload)
        returndata = returndata.json()
        access_token = returndata.get("access_token")
        # print(access_token)
        return access_token

    def call_ernie_speed_api(self, text, access_token):
        url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + access_token

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        data = {
            "messages": [
                {
                    "role": "user",
                    "content": text
                }
            ]
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            result = response.json()
            baiduchat = result.get("result")
            return baiduchat
            # return result["result"]["response"]
        else:
            print("请求失败")
            return None


if __name__ == "__main__":
    linguistic = linguistic()
    access_token = linguistic.get_access_token()
    text = linguistic.call_ernie_speed_api("你好", access_token)
    print(text)
