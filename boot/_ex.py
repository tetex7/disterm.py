import disnake
import json
import random
from disnake.ext import commands
import disnake.types.embed
import bot
import os
import SPROG

DIR = os.path.abspath(".")

def arg_sep(args:str) -> list[str]:
    temp:str = str()
    print(len(args) - 1)
    #ebn = False
    out:list[str] = list()
    ind = range(0, len(args))
    i = 0
    while (not i > (len(args) - 1)):  #cursed C like for Loop

        if (args[i] == '"'):
            temp = temp + args[i]
            for id in range(i+1, len(args)):
                temp = temp + args[id] 
                if (args[id] == '"'):
                    if (args[id] == '"'):
                        out.append(temp)
                        temp = str()
                        i = id 
                        break
                    temp = temp + args[id]
                    out.append(temp)
                    i = id
                    temp = str()
                    break
                     
        else:
            if (args[i].isspace()):
                if not (temp == ""):
                    out.append(temp)
                temp = str()
                i = i + 1
                continue
            else:
                temp = temp + args[i]
        i = i + 1
            
    if not (temp == ""):
        out.append(temp)
    return out.copy()


async def intrp(tr:str, inn:disnake.ApplicationCommandInteraction) -> int:
    sd:dict
    with open(f"{tr}") as buff:
        sd = json.load(buff)
    print(sd["DATA"])
    print(sd["INTP_CALL"])
    ie:int = len(sd["DATA"])
    en:bool = 1
    n:bool = 0
    TTS = False
    ib:int = 0

    for v in sd["INTP_CALL"]:
        try:
            ib = v["START_AT"]
        except KeyError:
            pass

        try:
            ie = v["END_AT"]
        except KeyError:
            pass
        try:
            ie = v["NUCK"]
            n = True
        except KeyError:
            pass
        try:
            ie = v["NO_EMBED"]
            en = False
        except KeyError:
            pass

    s:list[str] = list()
    e:list[disnake.embeds.Embed] = list()
    evo:bool = False
    for i in range(ib, ie):
        df = sd["DATA"][i]
        try:
            s.append(df["RAW_TEXT"])
            #await inn.response.send_message(i["RAW_TEXT"])
        except KeyError:
            pass

        
        try:
            if (en == 1):
                t:str = df["EMBED"][0]["TITLE"]
                tc:str = df["EMBED"][1]["TEXT"]
                ft:str = df["EMBED"][2]["FOOER"]
                cL:int = df["EMBED"][3]["CL"]
                d = disnake.embeds.Embed(title=t, description=tc, color=cL)
                d.set_footer(text=ft)
            #await inn.response.send_message(embed=d)
                e.append(d)
            else:
                s.append("EMBED BLOCK:\n{{")
                t:str = df["EMBED"][0]["TITLE"]
                tc:str = df["EMBED"][1]["TEXT"]
                ft:str = df["EMBED"][2]["FOOER"]
                s.append(f"\t**{t}**\n")
                s.append(f"\t{tc}\n")
                s.append(f"\n\t{ft}\n}}\n")
        except KeyError:
            pass
        
        try:
            if df["EXIT"] == "HO NO":
                pass
            exit()
            #await inn.response.send_message(i["RAW_TEXT"])
        except KeyError:
            pass

        try:
            if df["UOM"] == 0:
                evo = True
            
            #await inn.response.send_message(i["RAW_TEXT"])
        except KeyError:
            pass

        try:
            if df["TTS"] == 0:
                TTS = True
            
            #await inn.response.send_message(i["RAW_TEXT"])
        except KeyError:
            pass
    ss:str = str()
    for v in s:
        ss = ss + v
    try:
        await inn.response.send_message(embeds=e,content=ss, ephemeral=evo, tts=TTS)
    except:
        return 0
    if (n == True):
        await inn.target.delete()
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
    try:
        o:int = 0
        with open(f"{DIR}/jsons/ban.json") as buff:
            bb:dict = json.load(buff)
            list(bb["IDS"]).append(187385331753025536)
            for v in bb["IDS"]:
                if (inr.user.id == v):
                    await inr.response.send_message(f"NO {bot.dbot.get_user(v).name}", tts=True, ephemeral=1)
                    return 44
        if ((ex == None) or (ex == "")):
            o = 88
        print(ex)
        er = ex + '\\'
        sep = arg_sep(ex)
        if (sep[0] == "sudo"):
            sep[0] = "doas"

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
    except Exception as ex:
        MSG = f"TRACEBACK:\n{ex}"
        d = disnake.Embed(title="BOT PANIC:", description=MSG, color=0xFF0000)
        d.set_footer("PANIC!!")
        inr.response.send_message(embed=d)
        return
        

    