#!/usr/bin/env python3
import json
import bot
import disnake
from disnake.ext import commands
import _ex
import os
import bot
import sys

RED = "\033[0;31m"
NO_COL = "\033[0m"
YELLOW = "\033[0;33m"

CNF = os.path.abspath("jsons/tok.json")
with open(CNF) as buff:
    j = json.load(buff)
gid = int(j["GID"])

#bot:discord.client.Client = discord.client.Client(intents=discord.Intents.all())
bot.dbot = bot.Bot(gid) 

@bot.dbot.event
async def on_ready():
        print(f"{YELLOW}DISTERM IS BOOTED\n\tBOT NAME IS {RED}\"{bot.dbot.user.name}\"{NO_COL}")

@bot.dbot.event
async def on_member_join(m:disnake.member.Member):
    DIR = os.path.abspath(".")
    US = {
        "name": m.name,
        "nk_name": m.nick,
        "id": m.id,
        "PWD": "/",
        "groups": [
            "CPWD"
        ],
        "OP": False
    }
    os.system(f"touch {DIR}/var/user/{m.id}.user")
    with open("{DIR}/var/user/{m.id}.user", "w") as buff:
        json.dump(US, buff, indent=4)

@bot.dbot.event
async def on_member_remove(m:disnake.member.Member):
    DIR = os.path.abspath(".")
    os.remove(f"{DIR}/var/user/{m.id}.user")

@bot.dbot.event
async def on_member_update(before:disnake.member.Member, after:disnake.member.Member):
    DIR = os.path.abspath(".")
    d:dict
    with open(f"{DIR}/var/user/{after.id}.user", "r") as buff:
        d = json.load(buff)
    d["name"] = after.name
    d["nk_name"] = after.nick
    with open(f"{DIR}/var/user/{after.id}.user", "w") as buff:
        json.dump(d, buff, indent=4)


def BOOT():
    if (os.path.exists(os.path.abspath("jsons/tok.json")) == False):
        print(f"\n{RED}BOT ERR{NO_COL}\n    {YELLOW}NO \"./jsons/tok.json\"\n\t\tUSE \"gconf\" TO MAKE THE JSON{NO_COL}")
        exit(999)
    
    p = os.path.abspath("jsons/tok.json")
    with open(p, "r") as buff:
        t = json.load(buff)
        tTOK = t["ton"]
        fGID = t["GID"]
        if (((tTOK == "") or (tTOK == None) or (tTOK == "token")) or (fGID == 0)):
            #cf = os.path.abspath("gconf")
            #os.system(cf)
            exit(88)
        bot.dbot.run(tTOK)

@bot.dbot.slash_command()
async def cmd(inter:disnake.ApplicationCommandInteraction, ex: str):
   await _ex.EX(inter, ex)
    #if (not i == 0):
    #    await inter.response.send_message(f"EX ERR \'{i}\'")
    #pass

#@bot.on_message()
#async def on_message(msg:discord.Message):
#    #if (msg.content.find("<@ID>") > 0):
#    pass

BOOT()