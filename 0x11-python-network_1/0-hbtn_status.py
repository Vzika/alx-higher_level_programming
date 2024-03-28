#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request as request
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        if response:
            content = response.read()
            print('Body response:')
            print(f"\t- type: {type(content)}")
            print(f"\t- content: {content}")
            print(f"\t- utf8 content: {content.decode('utf-8')}")
