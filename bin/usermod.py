from libdiscord.TP import DIS_TP
#for lib.libdiscord
import sys

def main(FIT:str, SR:str) -> int:
    
    t = DIS_TP(FIT)
    if ((SR == "") or (SR == None)):
        t.TEXT("NO TEXT ARG")
        return
    t.USER.ADD_TO_GROUP(SR)
    return


exit(main(sys.argv[1], sys.argv[2]))