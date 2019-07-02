import json
import sys
import requests
import pymongo
from bson import json_util

uri = "mongodb://urlget:uHNWUz4jcGKMnlYCkb6aTNO9rtpEfdTyam4EWoSZ5vsiBmha3PZcqiZ14cb6i35AEEXPgceUAlUWwonKOJoUgw==@urlget.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
myclient = pymongo.MongoClient(uri)
mydb = myclient["stats"]
mycol = mydb["bf"]
print(myclient.list_database_names())

names = ["Skarmaggio", "Shawarmaaaaaa", "Christoballh", "EpleFyrsten"]

for name in names:
    r = requests.get(
        "https://api.battlefieldtracker.com/api/v1/bfv/profile/origin/" + name + ""
    )
    stats_JSON = r.json()

    # stats_string = json.dumps(stats_JSON, indent=2)

    x = mycol.insert_one(stats_JSON)
    print(x.inserted_id)
    # print(stats_string)
