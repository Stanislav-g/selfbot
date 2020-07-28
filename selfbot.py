import discord
from discord.ext import commands
from time import sleep
import os
import random
from random import randint, choice, choices
import asyncio

client = commands.Bot( command_prefix = '*', self_bot = True)

@client.event
async def on_redy():
    print( 'Bot connected')

  
@client.command()
async def start( ctx ):
    await ctx.channel.purge( limit = 1 )
    while True:
        await ctx.send(f"!d bump")
        await asyncio.sleep(7200)
        await ctx.send(f"!d bump")
        await asyncio.sleep(7200)
        await ctx.send(f"!d bump")
        await asyncio.sleep(7200)
        await ctx.send(f"!d bump")
        await asyncio.sleep(7200)
        await ctx.send(f"!d bump")
        await asyncio.sleep(7200)
        await ctx.send(f"!d bump")
        await asyncio.sleep(7200)
        await ctx.send(f"!d bump")
        await asyncio.sleep(7200)
        await ctx.send(f"!d bump")
        await asyncio.sleep(7200)
        await ctx.send(f"!d bump")
        await asyncio.sleep(7200)
    

    
@client.command()
async def priv( ctx ):
    while True:
        a = random.choice(['эй','привет','алло','девять чи десять?','ку','аваава','как дела?','упс','ДЕВЯТЬ???','ало','алооо','здарова'])
        await ctx.send(a)
        await asyncio.sleep(20)
        

#coin
@client.command()
async def coin(ctx):
    await ctx.channel.purge(limit = 1)
    coins = [ 'орел', 'решка' ]
    coins_r = random.choice( coins )
    coin_win = 'орел'
    if coins_r == coin_win:
        emb = discord.Embed(description= f''':tada: { ctx.message.author.name }, выиграл! \nТебе повезло у тебя: ``{ coins_r }``''', color = 0x0c0c0c)
        await ctx.send(embed = emb)
    if coins_r != coin_win:
        emb = discord.Embed(description= f''':thumbsdown:  { ctx.message.author.name }, проиграл!\n Тебе не повезло у тебя: ``{ coins_r }``''', color = 0x0c0c0c)
        await ctx.send(embed = emb)

    
token= os.environ.get('BOT_TOKEN')
client.run( token, bot = False )
