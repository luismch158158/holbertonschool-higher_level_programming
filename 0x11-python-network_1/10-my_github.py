#!/usr/bin/python3
"""Python script that takes your GitHub
credentials (username and password)
and uses the GitHub API to display your id"""

if __name__ == '__main__':
    import requests
    from requests.auth import HTTPBasicAuth
    import sys
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'

    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    print(response.json().get('id'))
