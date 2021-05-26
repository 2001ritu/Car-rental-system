import math
import json


f = open('vehicle-database.json')
data=json.load(f)
f.close

carlocations=[]
for i in data['points']:
    carlocations.append(i)

def FetchCabs(a,b):
    carlocations.sort(key=lambda x: math.sqrt((float(x['x']) - a) ** 2 + (float(x['y']) - b) ** 2))

    output = []
    for j in range(0,5):
        output.append(carlocations[j]);

    for i in output:
        print(i)

x=float(input())
y=float(input())


FetchCabs(x,y)
