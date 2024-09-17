from typing import Any, Dict, AnyStr, List, Union

class Arbitary():
    JSONObject = Dict[AnyStr, Any]
    JSONArray = List[Any]
    JSONStructure = Union[JSONArray, JSONObject]