#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
 https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)"""


if __name__ == '__main__':
    import requests
    import sys

    repository = sys.argv[1]
    owner = sys.argv[2]
    counter = 0

    url_1 = "https://api.github.com/repos/" + owner
    url_2 = "/" + repository + "/commits"
    url = url_1 + url_2

    response = requests.get(url)

    json_commits = response.json()
    # print(json_commits)
    for members in json_commits:
        counter += 1
        sha = members.get("sha")
        author = members.get("commit").get("author").get("name")
        print("{}: {}".format(sha, author))

        if counter == 10:
            break
