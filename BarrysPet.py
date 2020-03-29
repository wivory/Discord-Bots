import discord
import os
import random
import time
import sys
from discord.ext import commands
import json
from discord import Game

token = 'NjkyNzg5NzQ0OTgzMjEyMDg1.XnzpDg.TlX8t01az5JKdVDHL_3PpweBfhI'
GUILD = 'MorgzLordz'

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    messageauthor = str(message.author)
    if message.author == client.user:
        return
    if message.content == "Deactivate Bots" and messageauthor == "Sue_Perb#7867":
        sys.exit()
    if message.content == "Deactivate Barry's Pet" and messageauthor == "Sue_Perb#7867":
        sys.exit()
    if "ping" in message.content.lower() and messageauthor == "Barry#1301":
        activity = discord.Game(name="ping pong with Barry")
        await client.change_presence(status=discord.Status.online, activity=activity)
        await message.channel.send("pong")

client.run(token)
    
    
