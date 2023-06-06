#!/usr/bin/python3
"""
Queries for the first 10 hot posts listed
for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    Queries for the first 10 hot posts listed
    Args:
        subreddit: string
    if subreddit is invalid prints None
    """
    sub_check_url = "https://www.reddit.com/api/search_reddit_names.json"
    top_ten_url = "https://www.reddit.com/r/{}.json".format(subreddit)

    sub_check = requests.get(
        sub_check_url,
        headers={"User-Agent": "Safari 12.1"},
        params={"exact": True, "query": subreddit},
    )
    if "error" in sub_check.json().keys():
        print(None)
    else:
        data = requests.get(top_ten_url, headers={"User-Agent": "Safari 12.1"})
        children = data.json().get("data").get("children")
        printrange = 10
        if len(children) < 10:
            printrange = len(children)

        for i in range(printrange):
            print(children[i].get("data").get("title"))


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument")
    else:
        top_ten(sys.argv[1])
