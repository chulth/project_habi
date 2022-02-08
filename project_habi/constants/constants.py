FILTER_CITY_AND_YEAR_QUERY = (
                "SELECT * FROM property where city = '{0}' "
                "and year = {1};"
                        )
STATUS_ID_QUERY = (
            "SELECT MAX(status_id) FROM "
            " status_history where property_id = {0}"
        )
PROPERTY_QUERY = (
                    "SELECT property.address, property.description, "
                    "property.price, property.city, "
                    "MAX(status_history.status_id) FROM  "
                    "property, status_history where property.id={0} "
                    " and property_id={0};"
                    )
FILTER_CITY_QUERY = (
        "SELECT * FROM property where city = '{0}';"
        )
FILTER_YEAR_QUERY = (
                "SELECT * FROM property where year = {0};"
                )
NO_FOUND_MATCHING = {"msg": "There are no results matching the filters"}
KEYS_TO_FORMATING_RESPONSE = [
        "address", "description", "price", "city", "state"
        ]