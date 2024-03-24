from api import app
from apscheduler.schedulers.background import BackgroundScheduler
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType, gql
from ariadne.explorer import ExplorerGraphiQL
from flask import request, jsonify
from api.schema import resolve_races, resolve_AdvancedRaces, resolve_race, resolve_event_results, resolve_team_results, resolve_team_ids_and_names
#from queries import races_query
import json

explorer_html = ExplorerGraphiQL().html(None)

query = ObjectType("Query")

watchlist = {}

query.set_field("response", resolve_races)
query.set_field("advancedResponse", resolve_AdvancedRaces)
query.set_field("race_response", resolve_race)
query.set_field("individual_results", resolve_event_results)
query.set_field("team_results_sets", resolve_team_results)
query.set_field("team_scores", resolve_team_ids_and_names)

type_defs = load_schema_from_path("schema.graphql")
type_defs = gql(type_defs)
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
)

def update_local():
     
    #for race in watchlist:
    #    for event in race:
    #        resolve_event_results(race, event)

    # #file_path = "races.json"

    # with open(file_path, "w") as file:
    #         json.dump(data, file, indent=4)
    print(watchlist)

    print("Running every 30 seconds")

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