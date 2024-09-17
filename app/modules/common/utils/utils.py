import uuid

def get_uuid_id():
    return str(uuid.uuid4())

def walk_node(data_dict, key):
    lists = key.split(".")
    
    r = None
    for o in lists:
        r = data_dict.get(o)
        
        if r == None:
            return r
        
        data_dict = r
        
    return r