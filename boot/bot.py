from typing import Optional

import disnake
from disnake.ext import commands

class Bot(commands.InteractionBot):
    gUILD:None

    def __init__(self, gid):
        self.gUILD = gid
        super().__init__()
    
dbot:Bot