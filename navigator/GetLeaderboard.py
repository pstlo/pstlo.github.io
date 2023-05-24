import os,sys,json,base64,certifi
from cryptography.fernet import Fernet
from pymongo.mongo_client import MongoClient

database = MongoClient((Fernet(base64.b64decode(os.getenv('DBKEY'))).decrypt(os.getenv('DBTOKEN'))).decode(),tlsCAFile=certifi.where())
collection = database["navigator"]["leaderboard"]

leaders = list(collection.find().sort('longestRun', -1).limit(20))
database.close()
leaderBoard = []
for leaderIndex in range(len(leaders)-1):
    leader = leaders[leaderIndex]
    leaderBoard.append( {'name':leader['name'], 'time':leader['longestRun'], 'score':leader['highScore']} )

with open ("Leaders.json","w") as file: file.write(json.dumps(leaderBoard))
print os.listdir(os.getcwd())
