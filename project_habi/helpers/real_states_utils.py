
from data.conn import ConnDataBase
from constants import constants
import logging


def split_query_parameters(data):
    '''
    Split the URL string that arrives into the query parameters.
    Return a dictionary with the sorted filters.
    '''
    filters = {}
    query_parameters = dict(query.split("=") for query in data.split("&"))
    if query_parameters.get('city'):
        wanted_city = query_parameters['city'].lower()
        filters["city"] = wanted_city
    if query_parameters.get('year'):
        wanted_year = query_parameters['year']
        filters["year"] = wanted_year
    if query_parameters.get('state'):
        wanted_state = query_parameters['state']
        filters["state"] = int(wanted_state)
    if filters:
        return filters
    return False


def execute_query_string(filters):
    """
    Validates the existence of filters sent by the client.
    Generates the query depending on the filters.
    Returns a list with the properties found
    or message that says "There are no results matching the filters".
    """
    filter_city = filters.get('city')
    filter_year = filters.get('year')
    filter_state = filters.get('state')
    print(
        f"This is filters parameters: {filter_city},"
        "{filter_year}, {filter_state}")
    query_database = ConnDataBase()
    # case when take filter city and filter year
    if filter_city and filter_year:
        filters_query = constants.FILTER_CITY_AND_YEAR_QUERY
        response_query = query_database.use_cursor(
            filters_query.format(filter_city, filter_year))
        if not response_query:
            return constants.NO_FOUND_MATCHING
        response_properties = get_properties(response_query)
        if not filter_state:
            return response_properties
        return filter_to_state(response_properties, filter_state)
    # case when take only filter city
    if filter_city:
        city_query = constants.FILTER_CITY_QUERY
        response_query = query_database.use_cursor(
            city_query.format(filter_city))
        if not response_query:
            return constants.NO_FOUND_MATCHING
        response_properties = get_properties(response_query)
        if not filter_state:
            return response_properties
        return filter_to_state(response_properties, filter_state)
    # case when take only filter year
    if filter_year:
        year_query = constants.FILTER_YEAR_QUERY
        response_query = query_database.use_cursor(
            year_query.format(filter_year))
        if not response_query:
            return constants.NO_FOUND_MATCHING
        response_properties = get_properties(response_query)
        if not filter_state:
            return response_properties
        return filter_to_state(response_properties, filter_state)


def get_properties_by_status_id(list_status_ids):
    '''
    Takes a status id list and check status greater that 3,
    if it is higher, ask for the property.
    return the list of properties that have correct status.
    '''
    query_database = ConnDataBase()
    list_response = []
    status_id_query = constants.STATUS_ID_QUERY
    for _ids in list_status_ids:
        logging.info(f'This is ids: {_ids}')
        status_id = query_database.use_cursor(
            status_id_query.format(_ids))
        logging.info(status_id)
        if status_id[0][0] >= 3:
            property_query = constants.PROPERTY_QUERY
            response_query = query_database.use_cursor(
                property_query.format(_ids)
            )
            response_property = formatter_query(response_query)
            list_response.append(response_property)
    return list_response


def get_properties(response_query):
    """
    Takes ids from the response_query and perform the query on the database.
    Returns properties formatted in a dictionary within a list.
    """
    list_status_id = [x[0] for x in response_query]
    logging.info(f'This is states id: {list_status_id}')
    properties_list = get_properties_by_status_id(list_status_id)
    return properties_list


def filter_to_state(response_properties, filter_state):
    """
    Filter the list of properties by status.
    Returns a list with values ​​found or an empty list.
    """
    return [x for x in response_properties if x.get('state') == filter_state]


def formatter_query(response_property):
    """"
    Takes a list of keys and list to values to formatter into a dictionary.
    Return dict like this:
    {
        'address': 'calle 23 #45-67',
        'description': 'Hermoso apartamento en el centro de la ciudad',
        'price': 120000000,
        'city': 'bogota',
        'state': 3
        }
    """
    dict_formatter = {}
    list_keys = constants.KEYS_TO_FORMATING_RESPONSE
    list_values = list(response_property[0])
    for i in range(len(list_keys)):
        dict_formatter[list_keys[i]] = list_values[i]
    return dict_formatter
