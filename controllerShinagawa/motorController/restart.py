import pprint
import requests
import time
import sys

def main():
    response = requests.get(
        'http://munro.local:1337',
        params={'dc':'3'})
    try:
        pprint.pprint(response.json())
    except:
        sys.stderr.write("real gold\n")

main()
