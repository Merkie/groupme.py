import requests
import string
import random
import json

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

class groupme:

    def __init__(self, user, pss):
        self.u = user
        self.p = pss

    def randomString(self, stringLength):
        letters = string.ascii_lowercase + "1234567890"
        return ''.join(random.choice(letters) for i in range(stringLength))

    def login(self):
        headers = {
            'Host': 'v2.groupme.com',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'User-Agent': 'GroupMe-iOS/5.35.0.28 (iPhone; iOS 13.1; en_US)',
            'Accept-Language': 'en-US;q=1, es-MX;q=0.9, ja-JP;q=0.8',
        }

        data = '{"grant_type":"password","password":"'+self.p+'","app_version":"5.35.0.28","username":"'+self.u+'","app_id":"GroupMe-iOS-5.35.0.28-13.1-en_US","device_id":"3F6ACBC2-639E-429D-AE0F-68DFD95EA0D8"}'

        response = requests.post('https://v2.groupme.com/access_tokens', headers=headers, data=data, verify=False)

        return response.content

    def sendMessageToGroup(self, message, group, act):
        headers = {
            'Host': 'api.groupme.com',
            'X-Access-Token': act,
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'User-Agent': 'GroupMe-iOS/5.35.0.28 (iPhone; iOS 13.1; en_US)',
            'Accept-Language': 'en-US;q=1, es-MX;q=0.9, ja-JP;q=0.8',
        }

        data = '{"message":{"source_guid":"'+self.randomString(25)+'","attachments":[],"text":"'+message+'"}}'

        response = requests.post('https://api.groupme.com/v3/groups/'+str(group)+'/messages', headers=headers, data=data, verify=False)

        return response.content

    def getMessagesFromGroup(self, group, count, act):
        import requests

        c = count

        if(count > 100):
            c = 100

        headers = {
            'Host': 'api.groupme.com',
            'X-Access-Token': str(act),
            'Accept': '*/*',
            'User-Agent': 'GroupMe-iOS/5.35.1.5 (iPhone; iOS 13.1; en_US)',
            'Accept-Language': 'en-US;q=1, es-MX;q=0.9, ja-JP;q=0.8',
        }

        params = (
            ('acceptFiles', 'true'),
            ('app_id', 'GroupMe-iOS-5.35.1.5-13.1-en_US'),
            ('limit', str(count)),
        )

        response = requests.get('https://api.groupme.com/v3/groups/'+str(group)+'/messages', headers=headers, params=params, verify=False)

        return(response.content)

    def likeMessage(self, id, group, act):
        headers = {
            'Host': 'api.groupme.com',
            'X-Access-Token': str(act),
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'User-Agent': 'GroupMe-iOS/5.35.1.5 (iPhone; iOS 13.1; en_US)',
            'Accept-Language': 'en-US;q=1, es-MX;q=0.9, ja-JP;q=0.8',
        }

        data = '{"app_id":"GroupMe-iOS-5.35.1.5-13.1-en_US"}'

        response = requests.post('https://api.groupme.com/v3/messages/'+str(group)+'/'+str(id)+'/like', headers=headers, data=data, verify=False)

    def getUsers(self, group, act):
        headers = {
            'Host': 'api.groupme.com',
            'X-Access-Token': str(act),
            'Accept': '*/*',
            'User-Agent': 'GroupMe-iOS/5.35.1.5 (iPhone; iOS 13.1; en_US)',
            'Accept-Language': 'en-US;q=1, es-MX;q=0.9, ja-JP;q=0.8',
        }

        params = (
            ('app_id', 'GroupMe-iOS-5.35.1.5-13.1-en_US'),
        )

        response = requests.get('https://api.groupme.com/v3/groups/'+str(group), headers=headers, params=params, verify=False)

        return response.content
