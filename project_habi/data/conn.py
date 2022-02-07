
import logging
import pymysql
from dotenv import load_dotenv
import os


class ConnDataBase:
    """
    Take data of enviroment and connect with database
    return a class connection.
    """
    def __init__(self):
        load_dotenv("project_habi/settings/.env")
        self.connection = pymysql.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            db=os.getenv("DB_NAME"),
        )
        self.cursor = self.connection.cursor()
        print('Stablish connection sussesfull')

    def use_cursor(self, query):
        """
        Take a query and try execute in database
        Returns the registers found or False
        """
        try:
            self.cursor.execute(query)
            response_query = self.cursor.fetchall()
            if response_query:
                return response_query
            return False
        except Exception as e:
            logging.exception(e)
