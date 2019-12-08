# Groupme.py 💬

groupme.py is a little Python3.x library used for creating bots and other things within the Groupme app. Simply download groupme.py and import it into your Python file to start making your awesome project!

## Documentation

Initialization:

    from groupme import groupme as gm
    import json
    
    g = gm("email", "password") #Designed for normal accounts, not bot accounts
	loginresponse = g.login() #logs into groupme, save response
	accesstoken = json.loads(loginresponse)['response']['access_token'] #IMPORTANT

Sending a message to a group:

    groupid = 00000000
    g.sendMessageToGroup("message", groupid, accesstoken)

Getting messages from a group:

    #limit is the amount of messages you'll get starting from most recent, highest you can go is 100.
    messages = json.loads(g.getMessagesFromGroup(groupid, limit, accesstoken))['response']['messages']

Like a message:

    g.likeMessage(messages[x]['id'], groupid, accesstoken)

Get users of a group:

    g.getUsers(groupid, accesstoken))['response']['members']

Feel free to play around with the returns and the JSON structures. This API is very new, so expect updates in the future that'll make this more polished.

## Example bot

    from groupme import groupme as gm
    import time
    import json

	groupid = 00000000
	g = gm("email", "pass")

	loginresponse = g.login()
	accesstoken = json.loads(loginresponse)['response']['access_token']

	lastid = None
	prefix = "!"

	while True:
		time.sleep(1)
		messages = json.loads(g.getMessagesFromGroup(groupid, 100, accesstoken))['messages']
		
		try:
			#if this messages has not been registered before, and it begins with our set prefix...
			if(messages[0]['id'] != lastid and messages[0]['text'][0] == prefix):
				
				#command hello world
				if(messages[0]['text'] == prefix+"hello"):
					g.likeMessage(messages[0]['id'], groupid, accesstoken)
					g.sendMessageToGroup("world!", groupid, accesstoken)
				#when you say "!hello" bot likes message and says "world!"

		except Exception as e:
			print(e)

		lastid = messages[0]['id']

