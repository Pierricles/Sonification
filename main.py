import requests
import json

class Point:
    latitude=0
    longitude=0
    def __init__(self,latitude=0, longitude=0):
        self.latitude = latitude
        self.longitude = longitude

r = requests.get("https://www.mapquestapi.com/directions/v2/alternateroutes?key=uMb0YEdtislXWuR2w0rt1hk11NQXjA4p&from=Lille%2C+FR&to=Villeneuve+d'Ascq%2C+FR&outFormat=json&ambiguities=check&routeType=fastest&maxRoutes=10&timeOverage=25&doReverseGeocode=false&enhancedNarrative=false&avoidTimedConditions=false&unit=M")
data = r.json()
json.dumps(data, indent = 4, sort_keys=True)

p = (data["route"]["alternateRoutes"][0]["route"]["shape"]["shapePoints"])
nodeTable=[]
while len(p) != 0:
    point = Point()
    point.latitude = p.pop()
    point.longitude = p.pop()
    nodeTable.append(point)
print(nodeTable[0].latitude)
print(nodeTable[0].longitude)