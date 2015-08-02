__author__ = 'abhatna4'

import facebook
import requests

token = 'CAAUqzPiHjnMBAOhrWdiF6W9OxmShJa8w6Ix3ZBAJbBdOstGTZBgW3m8Yr7EOhBbuqV1jpAG9FXX4mPGk3ErSi8A6DHnvJHRm7SOvGNMZBHDqGIQyvYbPuEuZACPjXVZAwOvaUiFn6HmS2QmofOoq7hb7aicrspffuHCZAHl99LqXHIUSByvfOTViZBcoZBh7ttMZD'

def main():
    friends = requests.get("https://graph.facebook.com/1267203966/friends", params={'access_token':token})
    print friends.json()

if __name__ == '__main__':
    main()