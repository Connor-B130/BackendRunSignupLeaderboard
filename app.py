from api import app
from apscheduler.schedulers.background import BackgroundScheduler
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType, gql
from ariadne.explorer import ExplorerGraphiQL
from flask import request, jsonify
from api.schema import resolve_races, resolve_AdvancedRaces, resolve_race
from queries import races_query
import json

explorer_html = ExplorerGraphiQL().html(None)

query = ObjectType("Query")

query.set_field("response", resolve_races)
query.set_field("advancedResponse", resolve_AdvancedRaces)
query.set_field("race_response", resolve_race)

type_defs = load_schema_from_path("schema.graphql")
type_defs = gql(type_defs)
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
)

def update_local():
     
    # #file_path = "races.json"

    # with open(file_path, "w") as file:
    #         json.dump(data, file, indent=4)

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