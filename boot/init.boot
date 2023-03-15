#!/usr/bin/env python3
import json
import bot
import disnake
from disnake.ext import commands
import _ex
import os
import sys

RED = "\033[0;31m"
NO_COL = "\033[0m"
YELLOW = "\033[0;33m"

CNF = os.path.abspath("jsons/tok.json")
with open(CNF) as buff:
    j = json.load(buff)
gid = int(j["GID"])

#bot:discord.client.Client = discord.client.Client(intents=discord.Intents.all())
dbot:bot.Bot = bot.Bot(gid)

@dbot.event
async def on_ready():
        print(f"{YELLOW}DISTERM IS BOOTED\n\tBOT NAME IS {RED}\"{dbot.user.name}\"{NO_COL}")

def BOOT():
    if (os.path.exists(os.path.abspath("jsons/tok.json")) == False):
        print(f"\n{RED}BOT ERR{NO_COL}\n    {YELLOW}NO \"./jsons/tok.json\"\n\t\tUSE \"gconf\" TO MAKE THE JSON{NO_COL}")
        sys.exit(999)
    
    p = os.path.abspath("jsons/tok.json")
    with open(p, "r") as buff:
        t = json.load(buff)
        tTOK = t["ton"]
        fGID = t["GID"]
        if (((tTOK == "") or (tTOK == None) or (tTOK == "token")) or (fGID == 0)):
            #cf = os.path.abspath("gconf")
            #os.system(cf)
            sys.exit(88)
        dbot.run(tTOK)

@dbot.slash_command()
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