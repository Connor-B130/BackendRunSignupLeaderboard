import urllib.request, json
from collections import namedtuple

baseURL = "https://runsignup.com/Rest/"

#def customRaceDecoder(racesDict):
    #return namedtuple('X', racesDict.keys())(*racesDict.values())

def resolve_races(*_):
    try:
        with open('dummy.json', "r",encoding='utf-8') as json_data:
            d = json.load(json_data)
        response = urllib.request.urlopen(baseURL + 'races?format=json')
        data = response.read()
        #print(data)
        dict = json.loads(data)
        #dict = dict.items()
        #print(dict)
        #print(dict["races"])
        payload = {
            "success": True,
            "result": dict["races"]
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
