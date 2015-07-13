from slackclient import slackclient
import os

token = os.environ['SLACK_TOKEN']
sc = SlackClient(token)


if sc.rtm_connect():
  while True:
      print sc.rtm_read()
      time.sleep(1)
else: 
  print "Connection failed, invalid token?"

'''
check message to see if it references deepdreamer
if it does make sure two links are attached
run deep dreaming on the photos
save result to azure
post azure link in slack
'''