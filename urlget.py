import json
import sys
import requests
import pymongo

uri = "mongodb://urlget:uHNWUz4jcGKMnlYCkb6aTNO9rtpEfdTyam4EWoSZ5vsiBmha3PZcqiZ14cb6i35AEEXPgceUAlUWwonKOJoUgw==@urlget.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
client = pymongo.MongoClient(uri)
mydb = client["statTracker"]
print(client.list_database_names())

print("haaaaa")

names = ["Skarmaggio", "Shawarmaaaaaa", "Christoballh", "EpleFyrsten"]

for name in names:
    r = requests.get("https://api.battlefieldtracker.com/api/v1/bfv/profile/origin/" + name + "")
    stats_JSON = r.json()

    def showVals(label, node):
        if isinstance(node, float):
            print(f' {label}: {round(node, 2)}')
        else:
            print(f' {label}: {node}')

    stats_string = json.dumps(stats_JSON, indent=2)

    stats_lastupdated = stats_JSON['data']['stats']['lastUpdated']
    stats_scorePerMin = stats_JSON['data']['stats']['scorePerMinute']['value']
    stats_kd = stats_JSON['data']['stats']['kdRatio']['value']
    stats_kills = stats_JSON['data']['stats']['kills']['value']
    stats_deaths = stats_JSON['data']['stats']['deaths']['value']
    stats_accuracy = stats_JSON['data']['stats']['shotsAccuracy']['value']
    stats_killStreak = stats_JSON['data']['stats']['killStreak']['value']
    stats_longestHeadShot = stats_JSON['data']['stats']['longestHeadshot']['value']
    stats_killsPerMinute = stats_JSON['data']['stats']['killsPerMinute']['value']
    stats_wins = stats_JSON['data']['stats']['wins']['value']
    stats_losses = stats_JSON['data']['stats']['losses']['value']
    stats_wlPercentage = stats_JSON['data']['stats']['wlPercentage']['value']
    account_name = stats_JSON['data']['account']['playerNameNormalized']
    account_avatarURL = stats_JSON['data']['account']['avatarUrl']



    print(stats_string) 
    #print(round(stats_scorePerMin, 2))
    #print(account_name, stats_kd, stats_scorePerMin, stats_wlPercentage)
    #showVals('Name', account_name)
    #showVals('ScorePerMin', stats_scorePerMin)
    #showVals('KD', stats_kd)
    #showVals('Kills per min', stats_killsPerMinute)
    #showVals('Longest headshot', stats_longestHeadShot)
    #showVals('Win Loss %', stats_wlPercentage)
    #showVals('Longest killstreak', stats_killStreak)
    #showVals('Accuracy %', stats_accuracy)
    #showVals('Last updated', stats_lastupdated)

    print ("-------")
