import discord
import os
import random
import time
import array
from discord.ext import commands
import sys

token = 'NjkyNDI4ODgwNzIzNzA1ODk2.XnuZFQ.WTJA0n194u9qWgVpC0xnxw33bSg'


client = discord.Client()
GUILD = "MorgzLordz"

gamevariable = 0

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
    theauthorofmessage = (message.author)
    if message.author == client.user:
        return
    if message.content == "Deactivate Bots" and messageauthor == "Sue_Perb#7867":
        sys.exit()
    messageauthor = str(message.author)
    if message.content == "GDB exit" and messageauthor == "Sue_Perb#7867":
        await message.channel.send("Goodbye")
        sys.exit()
    if "gdb info" in message.content.lower():
        embed = discord.Embed(title="Help Sheet",type = "rich",description="The help sheet for Global Domination Bot",color=0x1abc9c)
        embed.add_field(name="GDB Info", value="Triggers this help sheet", inline=False)
        embed.add_field(name="start game", value="Starts a Global Domination game", inline=False)
        embed.add_field(name="yes", value="comfirms action (whilst in game)", inline=False)
        embed.add_field(name="no", value="cancels action (whilst in game)", inline=False)
        await message.channel.send(embed=embed)
    if "start game" in message.content.lower():
        clock = 5
        while clock > 0:
            await message.channel.send(f"Commencing in {clock}")
            clock = clock - 1
            time.sleep(1)
        await message.channel.send("Type yes to continue")
    if "yes" in message.content.lower():
        await message.channel.send("Commencing Start Setup")
        await message.channel.send(file=discord.File('C:\\Users\\david\Pictures\\David_Photos\BabyYoda.jfif'))
            #gamevariable = 1
    #if gamevariable == 1 and "yes" in message.content.lower():
        #await message.channel.send("goodbye")
    #if gamevariable == 1 and "no" in message.content.lower():
        #await message.channel.send("goodbye")
    

client.run(token)
    
