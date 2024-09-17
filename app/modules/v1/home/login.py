from modules.common.mysql.driver import RiMysqlDriver
from modules.common.model.arbitary import Arbitary
from datetime import datetime

import time
import json

async def login_http(data:Arbitary.JSONStructure):
    dbdriver = RiMysqlDriver()
    
    # Create a cursor object
    dbconn = dbdriver.get_connection()
    mycursor  = dbconn.cursor()
        
    # Define the SQL query for inserting data
    sql = "select userid, email, password from user";
        
    # Execute the SQL query
    mycursor.execute(sql)
    
    # Fetch all rows and convert to a list of dictionaries
    rows = mycursor.fetchall()
    result = []
    
    for row in rows:
        d={}
        for i, col in enumerate(mycursor.description):
            d[col[0]] = row[i]
            result.append(d)
    # close 
    dbdriver.close();
    
    # convert the list of dictionaries to json
    return {"status": 200, "message": "", "server-time": datetime.now(), "server-timezone": time.tzname, "payload": result }

async def test_case():
    v = await login_http();
    print (v)
    
if __name__ == "__main__":
    import asyncio
    
    asyncio.run(test_case())
