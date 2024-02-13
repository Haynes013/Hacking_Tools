import requests
import sys


def loop():
    for word in sys.stdin:
        res = requests.get(url=f"http://10.0.2.4/{word}")
        if res.status_code == 404:
            loop()
        else:
            data = res.json()
            print(data)
            print(res.status_code)
            print(word)


loop()