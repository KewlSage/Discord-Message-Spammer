# Name: discord message spam
# Description: allows you to send messages with token to channel ids
# Author: Not Kewl Sage from Hypesquad, i did edit this a lot though.
# Warning: THIS IS SELF BOTTING, I AM NOT RESPONSIBLE FOR ANY ISSUES YOU MAY COME IN TO DUE TO THIS FACT. USE AT YOUR OWN RISK.

import requests
import sys

class Bonk:

    def __init__(self, token, channel, message):
        self.token = token
        self.channel_id = channel
        self.message = message
        self.headers = {'Authorization': token}


    def _generate_message(self, m1):
        return m1


    def execute(self):
        return requests.post(f'https://discordapp.com/api/v6/channels/{self.channel_id}/messages', headers=self.headers, json={'content': self._generate_message(self.message)})

    
def main():
    if len(sys.argv) < 3:
        print(f'Usage: py {sys.argv[0]} <TOKEN> <CHANNEL ID> "MESSAGE"')
        sys.exit()

    token = sys.argv[1]
    channel_id = sys.argv[2]
    message = sys.argv[3]

    epicness = Bonk(token, channel_id, message)

    epicness.execute()


if __name__ == '__main__':
    main()
