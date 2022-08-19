#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

if __name__ == '__main__':
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    members = len(sys.argv)
    values = {}

    if members == 2:
        values['q'] = sys.argv[1]
    else:
        values['q'] = ""

    response = requests.post(url, data=values)

    try:
        json_response = response.json()
        id = json_response.get("id")
        name = json_response.get("name")
        longitud = len(json_response)
        if longitud != 0:
            print("[{}] {}".format(id, name))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
