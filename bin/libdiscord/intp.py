import json
import os
import sys
from typing import Final

class intp:
    FL:Final[str]

    def __UPDAT(self, DAT):
        with open(self.FIR, "w") as buff:
            json.dump(DAT, buff)

    def __init__(self, FILE:str) -> None:
        self.FL = FILE

    def START_AT_IND(self, i:int):
        D:Final[dict] = {"START_AT", i}
        df:dict
        with open(self.FL,"r") as buff:
            df = json.load(buff)
        dd:list = df["INTP_CALL"]
        dd.append(D)
        self.__UPDAT(df)

    def GO_TO(self, i:int):
        D:Final[dict] = {"GO_TO", i}
        df:dict
        with open(self.FL,"r") as buff:
            df = json.load(buff)
        dd:list = df["INTP_CALL"]
        dd.append(D)
        self.__UPDAT(df)

    def END_AT_IND(self, i:int):
        D:Final[dict] = {"END_AT": i}
        df:dict
        with open(self.FL,"r") as buff:
            df = json.load(buff)
        dd:list = df["INTP_CALL"]
        dd.append(D)
        self.__UPDAT(df)

    def NO_EMBEDS(self):
        D:Final[dict] = {"NO_EMBED": 1}
        df:dict
        with open(self.FL,"r") as buff:
            df = json.load(buff)
        dd:list = df["INTP_CALL"]
        dd.append(D)
        self.__UPDAT(df)

    def MGS_NUCK(self):
        D:Final[dict] = {"NUCK": 1}
        df:dict
        with open(self.FL,"r") as buff:
            df = json.load(buff)
        dd:list = df["INTP_CALL"]
        dd.append(D)
        self.__UPDAT(df)

    

