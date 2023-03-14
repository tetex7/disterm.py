from io import TextIOWrapper
import json


class DIS_TP:
    FIR:str
    def __UPDAT(self, DAT):
        with open(self.FIR, "w") as buff:
            json.dump(DAT, buff)

    def __init__(self, TF:str):
        self.FIR = TF


    def UID(self) -> str:
        with open(self.FIR, "r") as buff:
            day = json.load(buff)
            d:list = day["DATA"]
            return d[0]["UID"]

    def USER(self) -> str:
        with open(self.FIR, "r") as buff:
            day = json.load(buff)
            d:list = day["DATA"]
            return d[1]["USER"]

    def NK_NAME(self) -> str:
        with open(self.FIR, "r") as buff:
            day = json.load(buff)
            d:list = day["DATA"]
            return d[2]["NK_NAME"]


    def ENBED(self, TITLE:str, TEXT:str, CL:int = 0xFF0000, FOOTER:str = "DISTREM v1"):
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

