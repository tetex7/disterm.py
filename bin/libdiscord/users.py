import os
import sys
import json
from typing import Final

DIR:Final[str] = os.path.abspath(".") 

class user:
    U:dict
    UID:Final[int]
    PT:Final[str]

    class group_v:
        g:str
        ind:int

    def __UPDAT(self, DAT:dict):
        with open(self.PT, "w") as buff:
            json.dump(DAT, buff)

    def __init__(self, UID:int):
        if UID == -69:
            with open(f"{DIR}/var/user/ROOT.user") as buff:
                self.U = json.load(buff)
            self.UID = UID
            self.PT = f"{DIR}/var/user/ROOT.user"
            return

        if(os.path.exists(f"{DIR}/var/user/{UID}.user") == False):
            raise FileExistsError(f"./var/user/{UID}.user dos NOT Exists")
        with open(f"{DIR}/var/user/{UID}.user") as buff:
            self.U = json.load(buff)
        self.UID = UID
        self.PT = f"{DIR}/var/user/{UID}.user"

    def GET_UID(self) -> int:
        j:dict
        with open(self.PT) as buff:
            j = json.load(buff)
        if (j["id"] == self.UID):
            raise RuntimeError("id mismacth")
        return j["id"]

    def GET_NAME(self) -> str:
        j:dict
        with open(self.PT) as buff:
            j = json.load(buff)
        return j["name"]

    def GET_GROUPS(self) -> list[str]:
        j:dict
        with open(self.PT) as buff:
            j = json.load(buff)
        return list(j["groups"]).copy()

    def HAS_GROUP(self, s:str) -> bool:
        j:dict
        with open(self.PT) as buff:
            j = json.load(buff)
        for v in j["groups"]:
            if (s == v):
                return True
        return False
        
    def IS_TRUE_GROUP(self, g:str) -> bool:
        GROUP:Final[dict]
        with open(f"{DIR}/jsons/group.json") as buff:
            GROUP = json.load(buff)
        for v in GROUP["GROUPS"]:
            if (v == g):
                return True
        return False

    def GET_PWD(self) -> str:
        j:dict
        with open(self.PT) as buff:
            j = json.load(buff)
        return j["PWD"]

    def SET_PWD(self, s:str) -> int:
        if not (self.HAS_GROUP("CPWD")):
            return 88
        j:dict
        with open(self.PT) as buff:
            j = json.load(buff)
        j["PWD"] = s
        self.__UPDAT(j)
        return 0
        