
import http.server
from data.conn import ConnDataBase
from urllib.parse import urlparse
from constants import constants
import json


class RealStatesHandler(http.server.BaseHTTPRequestHandler):
    """
    Handles the GET requests that arrive to the service.
    Returns a json object with the query.
    """

    def do_GET(self):
        data = urlparse(self.path).query
        dict_filters = self.split_query_parameters(data)
        if not dict_filters:
            self.send_response(200)
            self.send_header('Content-type', 'text/json')
            self.end_headers()
            query_response = {"msg": "Please add query parameters"}
            self.wfile.write(json.dumps(query_response).encode())
        query_response = self.create_query_string(dict_filters)
        print(query_response)
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        self.wfile.write(json.dumps(query_response).encode())

    def split_query_parameters(self, data):
        '''
        Split the URL string that arrives in the query parameters.
        Return a dictionary with the sorted filters
        '''
        filters = {}
        query_parameters = dict(query.split("=") for query in data.split("&"))
        if query_parameters.get('city'):
            wanted_city = query_parameters['city'].lower()
            filters["city"] = wanted_city
        if query_parameters.get('year'):
            wanted_year = query_parameters['year']
            filters["year"] = wanted_year
        # if query_parameters.get('state'):
        #     wanted_state = query_parameters['state'].lower()
        #     dict_parameters["state"] = wanted_state
        if filters:
            return filters
        return False

    def create_query_string(self, filters):
        """
        Validate the filters sent by the client.
        Returns the query string to make the sql query
        """
        
        filter_city = filters.get('city')
        filter_year = filters.get('year')
        query_database = ConnDataBase()
        if filter_city and filter_year:
            filters_query = constants.FILTER_CITY_AND_YEAR_QUERY
            response = query_database.use_cursor(
                filters_query.format(filter_city, filter_year))
            states_to_id = [x[0] for x in response]
            print(f'This is states id: {states_to_id}')
            filter_state = self.check_state_to_property(states_to_id)
            return filter_state
        if filter_city:
            city_query = constants.FILTER_CITY_QUERY
            response = query_database.use_cursor(
                city_query.format(filter_city))
            states_to_id = [x[0] for x in response]
            print(f'This is states id: {states_to_id}')
            filter_state = self.check_state_to_property(states_to_id)
            return filter_state
        if filter_year:
            year_query = constants.FILTER_YEAR_QUERY
            response = query_database.use_cursor(
                year_query.format(filter_year))
            states_to_id = [x[0] for x in response]
            print(f'This is states id: {states_to_id}')
            filter_state = self.check_state_to_property(states_to_id)
            return filter_state
        
    def check_state_to_property(self, states_to_ids):
        query_database = ConnDataBase()
        response_query = []
        status_id_query = constants.STATUS_ID_QUERY
        for _ids in states_to_ids:
            print(f'This is ids: {_ids}')
            status_id = query_database.use_cursor(
                status_id_query.format(_ids))
            print(status_id)
            if status_id[0][0] >= 3:
                property_query = constants.PROPERTY_QUERY
                response_property = query_database.use_cursor(
                    property_query.format(_ids)
                )
                response_query.append(response_property)
        return response_query
