from modules.common.mysql.driver import RiMysqlDriver
from datetime import datetime
from modules.common.model.arbitary import Arbitary
import time
import json
import requests
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

async def arbitary_http(data:Arbitary.JSONStructure):
    print('received:', data)
    
    print('received-userid:', data['userid'])
    dbdriver = RiMysqlDriver()
    dbconn = dbdriver.get_connection()
    mycursor  = dbconn.cursor()
    sql = "select userid, email, password from user where email ='"+data['userid']+"'";
    print('sql-statement:', sql )
    mycursor.execute(sql)
    rows = mycursor.fetchall()
    result = []
    
    for row in rows:
        d={}
        for i, col in enumerate(mycursor.description):
            d[col[0]] = row[i]
            result.append(d)
            
    dbdriver.close();    
		
    response =  {"status": 200, "risk": 0, "server-time": datetime.now(), "server-timezone": time.tzname, "payload": result}
        
    return response

async def test_case():
    v = await arbitary_http({"foo":"bar"});
    print (v)
    
if __name__ == "__main__":
    import asyncio
    
    asyncio.run(test_case())