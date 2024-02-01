import urllib.request, json

baseURL = "https://runsignup.com/Rest/"

def resolve_races(*_):
    try:
        response = urllib.request.urlopen(baseURL + 'races?format=json')
        data = response.read()
        #print(data)
        dict = json.loads(data)
        #dict = dict.items()
        #print(dict)
        #print(dict["races"])
        payload = {
            "success": True,
            "result": dict['races']
        }

        file_path = "races.json"

        with open(file_path, "w") as file:
            json.dump(dict['races'], file, indent=4)

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

#this resolve will accept a name parameter
#if a parameter is sent through this function will run, and if the fields are blank
#then the resolve_races function will run.
def resolve_AdvancedRaces(*_):
    try:
        response = urllib.request.urlopen(baseURL + 'races?format=json&name=ConnorBennett')
        data = response.read()
        dict = json.loads(data)
        payload = {
            "success": True,
            "result": dict['races']
        }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload
