import requests


def get_access_token():
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


print(get_access_token())
