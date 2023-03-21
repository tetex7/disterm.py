from typing import Final

import disnake
from disnake.ext import commands

class Bot(commands.InteractionBot):
    gUILD:Final[int]

    def __init__(self, gid):
        self.gUILD = gid
        super().__init__(intents=disnake.Intents.all())

    def GET_GUILD(self) -> disnake.Guild:
        return self.get_guild(self.gUILD)

    def GET_USERS(self) -> list[disnake.Member]:
        return self.GET_GUILD().members.copy()
    
dbot:Bot