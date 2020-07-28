import discord
from discord.ext import commands
from time import sleep
import os
import random
from random import randint, choice, choices

client = commands.Bot( command_prefix = '-', self_bot = True)

@client.event
async def on_redy():
    print( 'Bot connected')



client.run("NzA2MTM4NjQwODQxMTc5MjE4.b5kCLO82SGnA1Jxcl1mvq_4WDWg", bot = False)
