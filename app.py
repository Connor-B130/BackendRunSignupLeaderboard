from api import app
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType, gql
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.schema import resolve_races
import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

#PLAYGROUND_HTML = ExplorerPlayground(title="Cool API").html(None)

query = ObjectType("Query")

query.set_field("Races", resolve_races)

type_defs = load_schema_from_path("schema.graphql")
type_defs = gql(type_defs)
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code