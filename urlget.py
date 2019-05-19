import sys
import requests

r = requests.get('https://api.battlefieldtracker.com/api/v1/bfv/profile/origin/Skarmaggio')
print(r.text) 
