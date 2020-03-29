import discord
import random
import time
import os
from discord.ext import commands

token = "NjkyNjg2ODAyODI5NDQzMTAy.XnyJLg.5JpPQxJ1bR-b4M30s8ktqesAjLQ"
GUILD = "MorgzLordz"

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
    if "hello baby yoda" in message.content.lower():
        await message.channel.send(content="It's a pleasure to meet you.", tts=True)


client.run(token)
