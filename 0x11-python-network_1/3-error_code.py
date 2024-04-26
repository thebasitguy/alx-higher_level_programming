#!/usr/bin/python3
"""This script takes in a URL,sends a request to
the URL and displays the body of the response."""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    url = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(url) as response:
            url_res = response.read()
            print(url_res.decode('utf-8'))

    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
