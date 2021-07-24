import os 
class config(object):
   API_ID=int(os.environ.get("API_ID", 6)) 
   API_HASH=os.environ.get("API_HASH" "")
   BOT_TOKEN=os.environ.get("BOT_TOKEN", "")
