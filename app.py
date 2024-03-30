from api import app
from apscheduler.schedulers.background import BackgroundScheduler
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType, gql
from ariadne.explorer import ExplorerGraphiQL
from flask import request, jsonify
from api.schema import resolve_races, resolve_AdvancedRaces, \
    resolve_race, resolve_event_results, resolve_team_results, \
    resolve_team_ids_and_names, resolve_update_results, \
    resolve_frontend_call, resolve_update_teams
#from queries import races_query
import json

explorer_html = ExplorerGraphiQL().html(None)

query = ObjectType("Query")

watchlist = {}
watchlist_teams = {}

query.set_field("response", resolve_races)
query.set_field("advancedResponse", resolve_AdvancedRaces)
query.set_field("race_response", resolve_race)
query.set_field("individual_results", resolve_event_results)
query.set_field("team_results_sets", resolve_team_results)
query.set_field("team_scores", resolve_team_ids_and_names)
query.set_field("frontend_call", resolve_frontend_call)

type_defs = load_schema_from_path("schema.graphql")
type_defs = gql(type_defs)
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
)

def update_local():
     
    payload = {}
    for race in watchlist:
        for event in watchlist[race]:
            payload.update(resolve_update_results(race, event))

    file_path = "individual_results.json"

    with open(file_path, "w") as json_file:
        json.dump(payload, json_file, indent=4)

    print(watchlist)
        
    # payload_team = {}
    # team_file_path = "team_results.json"

    # for race in watchlist_teams:
    #     for teams in watchlist_teams[race]:
    #         payload_team.update(resolve_update_teams(race, teams))

    # with open(team_file_path, "w") as json_file:
    #     json.dump(payload_team, json_file, indent=4)

scheduler = BackgroundScheduler()
scheduler.add_job(update_local, 'interval', seconds = 30)

scheduler.start()

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return explorer_html, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug,
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code

@app.route("/disconnect", methods=["POST"])
def disconnection(disconnect_list):
    watchlist[disconnect_list["race_id"]][disconnect_list["event_id"]] -= 1

    if watchlist[disconnect_list["race_id"]][disconnect_list["event_id"]] <= 0:
        del watchlist[disconnect_list["race_id"]][disconnect_list["event_id"]]

    #I am going to recieve a dictionary with the race id and event id and I will decrement 
    #the global dictionary entry by one (That corresponds to those ids) after that I will 
    #check the global dictionarys counter to se if it is zero. if it is I will take that 
    #of the dictionary.