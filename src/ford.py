# -*- coding: utf-8 -*-
"""
author: Andrei Bastos
organization: Labic/Ufes
data: 19/01/2018
"""

query = {
    "source": "twitter",
    "type": "flashback",
    "flashback_data": "tweets",
    "arguments": {        
        "terms": "dilma",
        "max_days": 5,
        "max_number": 10,
        "since_id": "15155345_56595951",
        "max_id": "-1",
        "language": "pt",
        "geocodes": {
            "lat": -20.351,
            "long": -40.175,
            "radius": 100
        },
        "filters": {
            "is_reverse": True,
            "terms": [
                {
                    "status.text": "não"
                },
                {
                    "status.user.screen_name": "andreibastos"
                }
            ]}
    }
}

class Collect():
    pid = 0
    priority = 0
    source = ""
    type = ""
    arguments = {}

    def __init__(self,query):
        self.source = query.get("source") or self.source
        self.type = query.get("type")
        self.arguments = query.get("arguments")
        self.flashback_data = query.get("flashback_data")
        
    def twitter(self, arguments):
        self.source = "twitter"
        pass

    def facebook(self, arguments):
        self.source = "facebook"
        pass
    
    def restart(self):
        pass

    def kill():
        pass

