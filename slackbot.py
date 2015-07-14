from slackclient import SlackClient
import os
import time

BOT_ID = '<@U07G4CNSV>'


if sc.rtm_connect():
  while True:
      print sc.rtm_read()
      time.sleep(1)
else: 
  print "Connection failed, invalid token?"

def init_slack_connection():
  token = os.environ['SLACK_KEY']
  sc = SlackClient(token)

  if sc.rtm_connect():
    while True:
        updates = sc.rtm_read()
        bot_updates = [update for update in updates if BOT_ID in update['text']]
        for update in updates:
          if verify_message(update):

          else:
            sc.rtm_send_message(channel=update['channel'], message="<@" + update['user'] + ">: Yo syntax was wrong")


        time.sleep(1)
  else: 
    print "Connection failed, invalid token?"

def references_bot(updates, bot_id):


def main():
  init_slack_connection()

'''
check message to see if it references deepdreamer
if it does make sure two links are attached
grab user name
run deep dreaming on the photos
save result to azure
post azure link in slack
'''

# u<@U07G4CNSV>