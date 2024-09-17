from datetime import datetime
import time

async def welcome_http():
    return {"status": 200, "message": "welcome to parish rest server", "server-time": datetime.now(), "server-timezone": time.tzname }

async def test_case():
    v = await levels_http();
    print (v)
    
if __name__ == "__main__":
    import asyncio
    
    asyncio.run(test_case())
