import discord
from discord.ext import commands
from pathlib import Path
import asyncio

client = discord.Client()

token = "NzUwNDc0NDk1OTE0OTM0NDAy.X07D1g.owyiZTSa8aO2-GwSCLml8GeM2n4"

    
@client.event
async def on_ready():
    print ("Logged in as " + str(client.user))
    print("id= " + str(client.user.id))


@client.event
async def on_message(message):

    channel = message.channel
    content = message.content
    if message.author == client.user:
        return
        
    
    

client.run(token)