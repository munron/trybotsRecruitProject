import pprint
import requests
import time
import sys

def main():
    response = requests.get(
        'http://munro.local:1337',
        params={'dc':'2'})
    try:
        pprint.pprint(response.json())
    except:
        sys.stderr.write("send 2\n")

main()
