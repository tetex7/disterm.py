import json
from libdiscord.TP import DIS_TP
#for lib.libdiscord
from typing import Final
import sys
import os
from enum import Enum

class cFAM_TYPE(Enum):
    SIB = "sibling"
    SPO = "spouse"
    KID = "child"
DIR = os.path.abspath(".")

def main(FIT:str, FAM_TYPE:str, WCALL:str, TO:str) -> int:
    t = DIS_TP(FIT)
    if (enumerate(cFAM_TYPE) == FAM_TYPE):
        RE:dict = {
            "TO": int(TO.replace("<@", "").replace(">", "")),
            "FROM": t.UID(),
            "TYPE": FAM_TYPE
        }
        d = TO.replace("<@", "").replace(">", "")
        os.system(f"touch {DIR}/var/temp/{d}.json")
        with open(f"{DIR}/var/temp/{d}.json", "w") as buff:
                json.dump(RE, buff, indent=4)
        t.ENBED(TEXT=f"From {t.USER_NAME()}", TEXT="type \"re_fam --accept\" or\ntype \"re_fam --no\"")
    else:
        t.UOM()
        t.TTS()
        t.TEXT("BAD FAM ARG")
    return


main(sys.argv[1], sys.argv[2], sys.argv[2], sys.argv[2])