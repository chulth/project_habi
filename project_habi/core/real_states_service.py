
import http.server
from urllib.parse import urlparse
import json
from helpers import real_states_utils


class RealStatesHandler(http.server.BaseHTTPRequestHandler):
    """
    Handles the GET requests that arrive to the service.
    Returns a json object with the query.
    """

    def do_GET(self):
        data = urlparse(self.path).query
        dict_filters = real_states_utils.split_query_parameters(data)
        if not dict_filters:
            self.send_response(200)
            self.send_header('Content-type', 'text/json')
            self.end_headers()
            query_response = {"msg": "Please add query parameters"}
            self.wfile.write(json.dumps(query_response).encode())
        query_response = real_states_utils.execute_query_string(dict_filters)
        print(query_response)
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        self.wfile.write(json.dumps(query_response).encode())
