import disnake
import json
from disnake.ext import commands
import os
import SPROG

DIR = os.path.abspath(".")

def arg_sep(s:str) -> list[str]:
    out:list[str] = list()
    print(len(s))
    print(out)
    temp:str = str()
    temp_intn:int = 0

    for i in range(0, len(s)):
        if (s[i] == ' '):
            continue
        elif ((s[i] == '"') or (s[i] == '\'')):
            temp = temp + s[i]
            for dd in range(i, len(s)):
                if ((s[dd] == '"') or (s[dd] == '\'')):
                    temp = temp + s[dd]
                    out.append(temp)
                    break
        elif (s[i] == '-'):
            temp = temp + s[i]
            for yy in range(i, len(s)):
                temp = temp + s[yy]
                if (s == ' '):
                    out.append(temp)
                    break
        else:
            temp = temp + s[i]
            if (s[i] == s[len(s)]):
                out.append(temp)
        temp = ""
    return out

async def intrp(tr:str, inn:disnake.ApplicationCommandInteraction) -> int:
    sd:None
    with open(f"{tr}") as buff:
        sd = json.load(buff)
    
    for i in sd["DATA"]:
        try:
            await inn.response.send_message(i["RAW_TEXT"])
        except KeyError:
            pass
        try:
            t:str = i["EMBED"][0]["TITLE"]
            tc:str = i["EMBED"][1]["TEXT"]
            ft:str = i["EMBED"][2]["FOOER"]
            cL:int = i["EMBED"][3]["CL"]
            d = disnake.embeds.Embed(title=t, description=tc, color=cL)
            await inn.response.send_message(embed=d)
        except KeyError:
            pass
    return 0


def PRJ(JJ:str, inr:disnake.ApplicationCommandInteraction):
    r:None
    with open(JJ,"r") as buff:
        r = json.load(buff)
    r["DATA"][0]["UID"] = inr.user.id
    r["DATA"][1]["USER"] = inr.user.name
    r["DATA"][2]["NK_NAME"] = inr.user.nick
    with open(JJ, "w") as buff:
            json.dump(r, buff)




async def EX(inr:disnake.ApplicationCommandInteraction, ex: str) -> int:
    o:int = 0
    if ((ex == None) or (ex == "")):
         o = 88
    print(ex)
    sep = ex.split(' ') #arg_sep(ex)

    if (os.path.exists(f"{DIR}/bin/{sep[0]}.prog") == False):
        await SPROG.SPP(inr,sep)
        o = 78
    
    ss = ""
    os.system(f"cp {DIR}/jsons/RAW_TP.json {DIR}/var/temp/{sep[0]}.json")
    PRJ(f"{DIR}/var/temp/{sep[0]}.json", inr)
    for i in range(1, len(sep)):
        ss = ss + sep[i]
    oi:int = os.system(f"python3 {DIR}/bin/{sep[0]}.prog {DIR}/var/temp/{sep[0]}.json {ss}")
        
    if (not (oi == 0)):
        o = oi
    await intrp(f"{DIR}/var/temp/{sep[0]}.json", inr)
    os.system(f"rm {DIR}/var/temp/{sep[0]}.json")
    if (not o == 0):
        await inr.response.send_message(f"EX ERR \'{o}\'")

    