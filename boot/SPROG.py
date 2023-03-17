import disnake
import json
from disnake.ext import commands
import os
import sys

SPROG:list[str] = [ "exit", "user_conf" ]

async def conf(ind:disnake.ApplicationCommandInteraction):
    ind.response.send_message("WIP")
    pass

async def SPP(ind:disnake.ApplicationCommandInteraction, arg:list[str]) -> bool:
    print(f"{arg}\n{SPROG}")
    if (arg[0] == SPROG[0]):
        await ind.response.send_message("GOOD BYE")
        ind.bot.close()
        sys.exit(0)
        return 1
    elif (arg[0] == SPROG[1]):
        conf(ind)
        return 1
    return 0