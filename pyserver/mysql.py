import pymysql
import pymysql.cursors
from loguru import logger


# import sys


class SQLDriver:
    def __init__(self, sql_user, sql_user_password, sql_host, sql_port, sql_db):
        logger.add("logs/sql.log", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}", rotation="10MB")
        try:
            self.connector = mariadb.connect(user=sql_user,
                                             password=sql_user_password,
                                             host=sql_host,
                                             port=sql_port,
                                             database=sql_db
                                             )
            self.cursor = self.connector.cursor()
            logger.info("Connection to DB is READY")
        except Exception as ex:
            logger.debug("FAIL connecting to DB", ex)
            # sys.exit(1)

    def retrieve_data(self, query, data):
        try:
            self.cursor.execute(query, data)
        except mariadb.Error as e:
            logger.error(f"Error: {e}")

    def add_date(self, query, data):
        try:
            self.cursor.execute(query, data)
        except mariadb.Error as e:
            logger.error(f"Error: {e}")

    def disconnect(self):
        self.connector.close()
        logger.info("Connection to DB is CLOSED")
