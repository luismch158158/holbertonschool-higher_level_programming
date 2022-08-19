#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed
URL with the email as a parameter, and displays the
body of the response (decoded in utf-8)"""

if __name__ == '__main__':
    import urllib.parse
    import urllib.request
    import sys

    email = sys.argv[2]
    url = sys.argv[1]
    values = {}
    values['email'] = email

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
    print(body.decode('utf-8'))
