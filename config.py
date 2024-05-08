from os import getenv
from dotenv import load_dotenv

#Necessary Variables 
API_ID = int(getenv("API_ID", 22163856))
API_HASH = getenv("API_HASH", "5c7fd7dded5675ce397690fa84d9ed4c")
BOT_TOKEN = getenv("BOT_TOKEN") #Put your bot token here
CHANNEL = getenv("CHANNEL", "ZenBotX") #Your public channel username without @ for force subscription.
MONGO = getenv("MONGO") #Put mongo db url here
#Optional Variables
OWNER_ID = int(getenv("OWNER_ID", 6542673293)) #Go to @ThunderrXbot and type /id and put that value here. 
FSUB = bool(getenv("FSUB", False)) #Set this True if you want to enable force subscription from users else set to False.
