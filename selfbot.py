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

    
token= os.environ.get('BOT_TOKEN')
client.run( token, bot = False )
