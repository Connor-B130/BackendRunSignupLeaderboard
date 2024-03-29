import urllib.request, json
from urllib.parse import urlencode
import base64

baseURL = "https://runsignup.com/Rest/"

def resolve_races(_, info):
    variables = info.variable_values

    try:
        response = urllib.request.urlopen(baseURL + 'races?format=json&name=' + variables["name"] + "&results_per_page=1000")
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
        advancedResponse = urllib.request.urlopen(baseURL + 'races?format=json&' + urlencode(variables) + "&results_per_page=1000")
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
        #team_dict = json.loads(team_data)
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
    from app import watchlist
    
    variables = info.variable_values
    try:
        results_response =  urllib.request.urlopen(baseURL + "race/" + variables["race_id"] + "/results/get-results?format=json&event_id=" + variables["event_id"] + "&results_per_page=2500")
        
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
        
    race_id = variables["race_id"]
    event_id = variables["event_id"]
    
    # Check if race_id exists in watchlist
    if race_id in watchlist:
        race_results = watchlist[race_id]
        # Check if event_id exists in race_results
        if event_id in race_results:
            watchlist[race_id][event_id] += 1
        else:
            # temp = {
            #     ("" + race_id): {
            #          ("" + event_id): 1
            #     }
            # }
            # watchlist.update(temp)
            watchlist[race_id][event_id] = 1
    else:
        temp = {
                ("" + variables["race_id"]): {
                     ("" + variables["event_id"]): 1
                }
            }
        watchlist.update(temp)

    return payload

def resolve_team_results(_, info):
    variables = info.variable_values
    try:
        results_response =  urllib.request.urlopen(baseURL + "v2/team-results/team-result-set.json?" + urlencode(variables))
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

def resolve_team_ids_and_names(_,info):
    from app import watchlist_teams
    variables = info.variable_values

    try:
        results_response =  urllib.request.urlopen(baseURL + "v2/team-results/team-result-set-results.json?" + urlencode(variables))
        names_response = urllib.request.urlopen(baseURL + "v2/team-results/result-teams.json?" + urlencode(variables))

        data = results_response.read()
        name_data = names_response.read()

        dict = json.loads(data)
        names_dict = json.loads(name_data)

        ids = dict["results"]
        names = names_dict["teams"]

        headers = dict["columns"] + names_dict["columns"]
        matching_list = []

        for i in ids:
            for x in names:
                if (i[0] == x[0]):
                    combined_list = i + x
                    new_dict = {headers: combined_list for headers, combined_list in zip(headers, combined_list)}
                    matching_list.append(new_dict)

        #print(matching_list)
        payload = {
            "success": True,
            "result": matching_list
        }
        #print(payload)
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    race_id = variables["race_id"]
    team_result_set_id = variables["team_result_set_id"]
    
    # Check if race_id exists in watchlist
    if race_id in watchlist_teams:
        race_results = watchlist_teams[race_id]
        # Check if event_id exists in race_results
        if team_result_set_id in race_results:
            watchlist_teams[race_id][team_result_set_id] += 1
        else:
            temp = {
                ("" + variables["race_id"]): {
                     ("" + variables["team_result_set_id"]): 1
                }
            }
            watchlist_teams.update(temp)
    else:
        temp = {
                ("" + variables["race_id"]): {
                     ("" + variables["team_result_set_id"]): 1
                }
            }
        watchlist_teams.update(temp)

    return payload

def resolve_update_results(race, event):
    try:
        results_response =  urllib.request.urlopen(baseURL + "race/" + race + "/results/get-results?format=json&event_id=" + event + "&results_per_page=2500")
        
        data = results_response.read()
        dict = json.loads(data)

        payload = { 
            ""+ race + event: dict
        }
    except Exception as error:
        print(error)
    
    return payload

def resolve_update_teams(race, team_set):
    variables = {"race_id": race, "team_result_set_id": team_set}
    try:
        results_response =  urllib.request.urlopen(baseURL + "v2/team-results/team-result-set-results.json?" + urlencode(variables))
        names_response = urllib.request.urlopen(baseURL + "v2/team-results/result-teams.json?" + urlencode(variables))

        data = results_response.read()
        name_data = names_response.read()

        dict = json.loads(data)
        names_dict = json.loads(name_data)

        ids = dict["results"]
        names = names_dict["teams"]

        headers = dict["columns"] + names_dict["columns"]
        matching_list = []

        for i in ids:
            for x in names:
                if (i[0] == x[0]):
                    combined_list = i + x
                    new_dict = {headers: combined_list for headers, combined_list in zip(headers, combined_list)}
                    matching_list.append(new_dict)

        #print(matching_list)
        payload = {
            "success": True,
            "result": matching_list
        }
        #print(payload)
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
    #race id and team result id

def resolve_frontend_call(_, info):
    variables = info.variable_values
    try:
        with open('individual_results.json', 'r') as results:
            data = json.load(results)
            race_event = variables['race_id'] + variables['event_id']
            dict = data.get(race_event)
            
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