import disnake
import json
import random
from disnake.ext import commands
import disnake.types.embed
import bot
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

def arr(s:str) -> list[str]:
    out:list[str] = list()
    ff = str()
    for v in s:
        if (v == " "):
            out.append(ff)
            ff = str()
        if not (v == " "):
            ff = ff + v
            
        if (v == s[s.__len__() - 1]):
            break
    return out


async def intrp(tr:str, inn:disnake.ApplicationCommandInteraction) -> int:
    sd:None
    with open(f"{tr}") as buff:
        sd = json.load(buff)
    print(sd["DATA"])
    print(type(sd))
    s:list[str] = list()
    e:list[disnake.embeds.Embed] = list()
    for i in sd["DATA"]:
        try:
            s.append(i["RAW_TEXT"])
            #await inn.response.send_message(i["RAW_TEXT"])
        except KeyError:
            pass
        try:
            t:str = i["EMBED"][0]["TITLE"]
            tc:str = i["EMBED"][1]["TEXT"]
            ft:str = i["EMBED"][2]["FOOER"]
            cL:int = i["EMBED"][3]["CL"]
            d = disnake.embeds.Embed(title=t, description=tc, color=cL)
            d.set_footer(text=ft)
            #await inn.response.send_message(embed=d)
            e.append(d)
        except KeyError:
            pass
    ss:str = str()
    for v in s:
        ss = ss + v
    try:
        await inn.response.send_message(embeds=e,content=ss)
    except:
        return 0
    return 0


def PRJ(JJ:str, inr:disnake.ApplicationCommandInteraction):
    r:dict
    with open(JJ,"r") as buff:
        r = json.load(buff)
    r["DATA"][0]["UID"] = inr.user.id
    r["DATA"][1]["USER"] = inr.user.name
    r["DATA"][2]["NK_NAME"] = inr.user.nick
    r["DATA"][3]["GNAME"] = inr.guild.name
    r["DATA"][4]["USER_MENTI"] = inr.user.mention # str = <@inr.user.id>
    with open(JJ, "w") as buff:
            json.dump(r, buff)




async def EX(inr:disnake.ApplicationCommandInteraction, ex: str) -> int:
    o:int = 0
    with open(f"{DIR}/jsons/ban.json") as buff:
        bb:dict = json.load(buff)
        for v in bb["IDS"]:
            if (inr.user.id == v):
                await inr.response.send_message(f"NO {bot.dbot.get_user(v).name}", tts=True, ephemeral=1)
                return 44
    if ((ex == None) or (ex == "")):
         o = 88
    print(ex)
    er = ex + '\\'
    sep = ex.replace(" ", ", ").split(",")

    if (os.path.exists(f"{DIR}/bin/{sep[0]}.prog") == False):
        v = await SPROG.SPP(inr,sep)
        if (v == 0):
            await inr.response.send_message(f"NO PROG {sep[0]}.prog")
            return 0
        o = 78
    rng = random.randint(15, 999)
    js = f"{DIR}/var/temp/{sep[0]}{rng}.json"
    print(js)
    ss = ""
    os.system(f"cp {DIR}/jsons/RAW_TP.json {js}")
    PRJ(js, inr)
    for i in range(1, len(sep)):
        ss = ss + sep[i]

    print(ss)
    oi:int = os.system(f"python3 {DIR}/bin/{sep[0]}.prog {js} {ss}")

    if (not (oi == 0)):
        o = oi
    await intrp(js, inr)
    print(js)
    os.system(f"rm {js}")
    if (not o == 0):
        #await inr.response.send_message(f"EX ERR \'{o}\'")
        pass

    