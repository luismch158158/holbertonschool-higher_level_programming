#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""

if __name__ == '__main__':
    import requests

    url = "https://intranet.hbtn.io/status"
    req = requests.get(url)
    req_text = req.text

    print('Body response:')
    print('\t type: {}'.format(type(req_text)))
    print('\t content: {}'.format(req_text))
