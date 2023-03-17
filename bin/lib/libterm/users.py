import os
import sys
import json
DIR = os.path.abspath(".") 

class user:
    U:dict
    def __init__(self, UID:int):
        if(os.path.exists(f"{DIR}/var/user/{UID}.json") == False):
            raise FileExistsError(f"./var/user/{UID}.json dos NOT Exists")
        self.U = json.load(f"{DIR}/var/user/{UID}.json")

    def GET_UID() -> int:
        pass

    def GET_NAME() -> str:
        pass