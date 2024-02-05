import urllib.request, json

baseURL = "https://runsignup.com/Rest/"

def resolve_races(_, info):
    variables = info.variable_values

    try:
        response = urllib.request.urlopen(baseURL + 'races?format=json&name=' + variables["name"])
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
        advancedResponse = urllib.request.urlopen(baseURL + 'races?format=json&name=' + variables["name"] + '&state=' + variables["state"] + '&city=' + variables["city"] + "&country_code=" + variables["country_code"] + "$start_date=" + variables["start_date"])
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

def resolve_race(_, info):
    variables = info.variable_values
    try:
        race_response = urllib.request.urlopen(baseURL + "race/" + variables["race_id"] + "?format=json")
        data = race_response.read()
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

def resolve_event_results(_, info):
    variables = info.variable_values
    try:
        results_response =  urllib.request.urlopen(baseURL + "race/" + variables["race_id"] + "/results/get-results?format=json&event_id=" + variables["event_id"])
        data = results_response.read()
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