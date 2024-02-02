import urllib.request, json

baseURL = "https://runsignup.com/Rest/"

def resolve_races(_, info):
    variables = info.variable_values

    try:
        response = urllib.request.urlopen(baseURL + 'races?format=json&name=' + variables["name"] + "&city=" + variables["city"])
        data = response.read()
        #print(data)
        dict = json.loads(data)
        #dict = dict.items()
        #print(dict)
        #print(dict["races"])
        payload = {
            "success": True,
            "result": dict
        }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

#this resolve will accept a name parameter
#if a parameter is sent through this function will run, and if the fields are blank
#then the resolve_races function will run.
def resolve_AdvancedRaces(_, info):
    variables = info.variable_values
    try:
        advancedResponse = urllib.request.urlopen(baseURL + 'races?format=json&name=' + variables["name"] + '&state=' + variables["state"] + '&city=' + variables["city"] + "&country_code=" + variables["country_code"])
        data = advancedResponse.read()
        dict = json.loads(data)
        payload = {
            "success": True,
            "result": dict
        }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload
