import json

import requests


def get_access_token():
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=UsguVpG6UcsP4fyk15uDnFvf&client_secret=mPuKsTRrsvyWJcvzzBsXrkjXqY7UoJLv"

    payload = ""
    returndata = requests.post(url, headers=headers, data=payload)
    returndata = returndata.json()
    access_token = returndata.get("access_token")
    print(access_token)
    return access_token


def post_baiduchat(String, access_token):
    # access_token = get_access_token()
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + access_token
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    payload = json.dumps({
        "messages": [{"role": "user", "content": String}]
    })
    returndata = requests.post(url, headers=headers, data=payload)

    returnjson = returndata.json()
    baiduchat = returnjson.get("result")
    return baiduchat


if __name__ == '__main__':
    get_access_token = get_access_token()
    text = post_baiduchat("你好么", get_access_token)
    print(text)
