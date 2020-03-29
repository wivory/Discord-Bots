import os
import random

import discord
from dotenv import load_dotenv
from discord.ext import commands
import array
import time

load_dotenv()
TOKEN = 'Njc5MDI1OTkwNTQ2MDk2MTI5.XkrY0g.NcrvCGQEN0GN-nEUEbxER7cIm8M'
GUILD = 'MorgzLordz'

bot = commands.Bot(command_prefix="!")

client = discord.Client()

how_are_you_today = [
    "I'm great thanks.",
    "I'm actually slightly sad.",
    "Brilliant. How are you?",
]

pleasantries = [
    "How are you feeling at the moment?",
    "Does the spam ever stop?",
    "Thanks for spamming me again and again.",
    "Spam is my life."
]
jokes = open("Jokes.txt", "r")
if jokes.mode == "r":
    contents = jokes.readlines()

rude = ["Barry", "David", "Andrew", "Ben"]

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
@bot.event
async def on_ready1():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user.name} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    messagecode = 0
    stop = 0
    if message.author == client.user:
        return
    if "stop the spam" in message.content.lower():
        stop = 0
        await messsage.channel.send("Very sorry. I will definitely stop now.")
        stop = 1
        return
    if "spam message" in message.content.lower():
        if stop == 0:
            time.sleep(0)
            messagecode += 1
            await message.channel.send("Thank you for the spam message. {}".format(random.choice(pleasantries), messagecode))
        

@bot.command(name="roll dice")
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides +1)))
        for _ in range(number_of_dice)
        ]
    await ctx.send(", ".join(dice))
                
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Welcome {member.name} to MorgzLordz. (this is an automated message from Barry The Discord Bot)"
        )

client.run(TOKEN)
bot.run(token)
