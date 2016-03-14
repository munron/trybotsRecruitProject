import pprint
import requests
import time
import sys

def main():
    response = requests.get(
        'http://adawarppi3.local:1337/',
        {"dc":"1"})
    try:
        pprint.pprint(response.json())
    except:
        sys.stderr.write("real gold\n")

if __name__=='__main__':
    while True:
        main()
        time.sleep(1)
        
        
