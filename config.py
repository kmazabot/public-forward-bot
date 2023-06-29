import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "19495376"))
    API_HASH = os.environ.get("API_HASH", "62e8e48d4cc1dc6f120c0cf5961ba8ab")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5745691407:AAFGPFmCV0cR-DDT61v4exfkRmeuLOWayrw")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5023341854")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://xoxan12:Mzbeans1@cluster0.zedsq9s.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "AQBdWU8w5rTJr-ufwydGrr8NjvW1n3YQ7tXGXXblrpKZyiLgENkrlMd00wGEuJhOS8Ec1hG-9kvwJYI1LQLah1HAf6baqwetILJ6UGDai8iiSpO9So3Hmvf4lgPN9zClWSJbk1RcMdSiQN2OZK-OoJEiDr7TYQo-6NMECPOaEPRzqVtzq5F0hWysmVQSSuMHk1Y5OJSUtcfT0x5UnmFWQ-FQLCqYO66jkeBGB4XPQRUDpmWv4EzS0dPUQkRQEsc3BzAk3I2ZiqjDHBeWaw9Gey05_IXECNTf7q3FBG43fcShMr2Q7G8tcRSqLtNkRRizvQ2Mz2bBnZJmk-pYWP117LN8AAAAAStqHR4A")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001980696426"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "kmazafilmlinks_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
