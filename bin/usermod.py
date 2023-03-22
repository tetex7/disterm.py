from libdiscord.TP import DIS_TP
from libdiscord.users import user
#for lib.libdiscord
import sys

if (sys.argv[2] == "--help"):
    t = DIS_TP(sys.argv[1])
    t.ENBED(TITLE="TODO", TEXT="TODO")


def dmain(FIT:str, ID:int, g:str):
    t = DIS_TP(FIT)
    u = user(ID)
    if ((g == "") or (g == None)):
        t.TEXT("NO TEXT ARG")
        return
    u.ADD_TO_GROUP(g)
    t.TEXT("GROUP ADDED")
    return

def main(FIT:str, SR:str) -> int:
    
    t = DIS_TP(FIT)
    if ((SR == "") or (SR == None)):
        t.TEXT("NO TEXT ARG")
        return
    t.USER.ADD_TO_GROUP(SR)
    t.TEXT("GROUP ADDED")
    return


try:
    dmain(sys.argv[1], int(sys.argv[2]), sys.argv[3])
except:
    main(sys.argv[1], sys.argv[2])