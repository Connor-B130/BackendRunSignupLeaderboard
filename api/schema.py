from ariadne import QueryType
import urllib.request, json

baseURL = "https://runsignup.com/Rest/"

query = QueryType()

@query.field("Races")
def resolve_races(*_):
    response = urllib.request.urlopen(baseURL + 'races?format=json')
    data = response.read()
    dict = json.loads(data)
    #print(dict["races"])
    #print(type(dict))
    print(data)
    return dict["races"]
