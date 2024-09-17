import json
import os
import pymysql

from modules.common.logger.logger import Logger
from dotenv import load_dotenv

load_dotenv(verbose=True)

class RiMysqlDriver:
    p = Logger(__name__, "INFO")
        
    def __init__(self):
        # Establish a connection to the MySQL database
        self.conn = pymysql.connect(
                host=os.environ["MYSQL_HOST"],
                user=os.environ["MYSQL_USER"],
                password=os.environ["MYSQL_PASSWORD"],
                db=os.environ["MYSQL_DATABASE"],
                charset='utf8mb4')

    def get_connection(self):
        return self.conn
    
    def close(self):
        self.conn.close()
