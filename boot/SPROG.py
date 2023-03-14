import disnake
import json
from disnake.ext import commands
import os

SPROG:list[str] = [ "exit", "user_conf" ]

async def conf(ind:disnake.ApplicationCommandInteraction):
    ind.response.send_message("WIP")
    pass

async def SPP(ind:disnake.ApplicationCommandInteraction, arg:list[str]):
    print(f"{arg}\n{SPROG}")
    if (arg[0] == SPROG[0]):
        if (ind.user.guild_permissions.administrator == False):
            return
        try:
            if(not arg[1].isdigit()):
                exit(0)
            else:
                exit(int(arg[1]))
        except:
            exit(0)
    elif (arg[0] == SPROG[1]):
        conf(ind)