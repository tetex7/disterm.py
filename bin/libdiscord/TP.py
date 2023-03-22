#from io import TextIOWrapper
import json
from typing import Final
from libdiscord.users import user
from libdiscord.intp import intp
import random

class DIS_TP:
    FIR:Final[str]
    USER:Final[user]
    INP:Final[intp]


    def __UPDAT(self, DAT):
        with open(self.FIR, "w") as buff:
            json.dump(DAT, buff)

    def __init__(self, TF:str):
        self.FIR = TF
        self.USER = user(self.UID())
        self.INP = intp(self.FIR)
        self.INP.START_AT_IND(5)


    def UID(self) -> int:
        with open(self.FIR, "r") as buff:
            day = json.load(buff)
            d:list = day["DATA"]
            return d[0]["UID"]
    

    def USER_MENTI(self) -> str:
        with open(self.FIR, "r") as buff:
            day = json.load(buff)
            d:list = day["DATA"]
            return d[4]["USER_MENTI"]
    

    def USER_NAME(self) -> str:
        with open(self.FIR, "r") as buff:
            day = json.load(buff)
            d:list = day["DATA"]
            return d[1]["USER"]

    def NK_NAME(self) -> str:
        with open(self.FIR, "r") as buff:
            day = json.load(buff)
            d:list = day["DATA"]
            return d[2]["NK_NAME"]

    def GNAME(self) -> str:
        with open(self.FIR, "r") as buff:
            day = json.load(buff)
            d:list = day["DATA"]
            return d[3]["GNAME"]
    
    def UOM(self):
        with open(self.FIR) as buff:
            day = json.load(buff)
            lL = day["DATA"]
            dat = {"UOM": 0}
            lL.append(dat)
            self.__UPDAT(day)

    def TTS(self):
        with open(self.FIR) as buff:
            day = json.load(buff)
            lL = day["DATA"]
            dat = {"TTS": 0}
            lL.append(dat)
            self.__UPDAT(day)


    def GEN_DM(self, id:int) -> None:
        if (self.User.HAS_GROUP("GODS")):
            DM = [{"TO": 0}]
            with open(self.FIR, "r") as buff:
                day:dict = json.load(buff)
                l:list = day["DATA"]
                l.append(DM)
        else:
            raise PermissionError("NOT disROOT")
#0xAF95F4
    def ENBED(self, TITLE:str, TEXT:str, CL:int = random.randint(0, 0xFFFFFF), FOOTER:str = "DIStrem"):
        with open(self.FIR) as buff:
            day = json.load(buff)
            lL = day["DATA"]
            dat = {"EMBED": [ {"TITLE": f"{TITLE}"}, {"TEXT": f"{TEXT}"}, {"FOOER": f"{FOOTER}"}, {"CL": CL} ]}
            lL.append(dat)
            self.__UPDAT(day)

    def TEXT(self, TEXT:str):
        with open(self.FIR) as buff:
            day = json.load(buff)
            lL = day["DATA"]
            dat = {"RAW_TEXT": f"{TEXT}"}
            lL.append(dat)
            self.__UPDAT(day)

    def DEF_TEXT(self, TEXT:str):
        with open(self.FIR) as buff:
            day = json.load(buff)
            lL = day["DATA"]
            dat = {"DEF_TEXT": f"{TEXT}"}
            lL.append(dat)
            self.__UPDAT(day)

    def EXIT(self):
        KILL:Final[dict] = {"KILL": "HO NO"}
        if (self.User.HAS_GROUP("GODS")):
            with open(self.FIR) as buff:
                day:dict = json.load(buff)
                lL:list = day["DATA"]
                lL.append(KILL)
                self.__UPDAT(day)
        else:
            raise PermissionError("NOT disROOT")

    def __str__(self) -> str:
        return self.USER()

    def __int__(self) -> int:
        return self.UID()

