import sys
import requests
import json

r = requests.get('https://api.battlefieldtracker.com/api/v1/bfv/profile/origin/Skarmaggio')
stats_JSON = r.json()


stats_string = json.dumps(stats_JSON, indent=2)

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



#print(stats_string) 
print(round(stats_scorePerMin, 2))
print(account_name, stats_kd, stats_scorePerMin, stats_wlPercentage)