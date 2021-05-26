import json

data = {
  "points": []
}

for i in range(0,1000):
    data['points'].append({"id":i,"x":i+6.765,"y":i+1.354})
	

with open('vehicle-database.json', 'w') as outfile:
    json.dump(data, outfile)
