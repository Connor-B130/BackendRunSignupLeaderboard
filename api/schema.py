from ariadne import QueryType
import urllib.request, json

baseURL = "https://runsignup.com/Rest/"

def resolve_races(*_):
    try:
        response = urllib.request.urlopen(baseURL + 'races?format=json')
        data = response.read()
        dict = [json.loads(data)]
        payload = {
            "success": True,
            "races": dict
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
