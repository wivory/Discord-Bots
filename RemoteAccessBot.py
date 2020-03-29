import os
import random

import discord
from dotenv import load_dotenv
from discord.ext import commands
import array


load_dotenv()
TOKEN = 'Njc5MDQzMjU3NTIyNDU0NTMz.XkrnCw.LkMEnwuShqmGoAaa9d--mM1YaFg'
GUILD = 'MorgzLordz'

bot = commands.Bot(command_prefix="!")

client = discord.Client()

how_are_you_today = [
    "I'm great thanks.",
    "I'm actually slightly sad.",
    "Brilliant. How are you?",
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
    if message.author == client.user:
        return
    if "change spam variable to" in message.content.lower():
        morgz1 = message.content.lower()
        spam1 = open("spam.txt", "w+")
        if spam1.mode == "w+":
            spamvariablefile = spam1.readlines()
            spam1.write(morgz1)
            await message.channel.send("Consider it done.")
        
@bot.command(name="roll dice")
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides +1)))
        for _ in range(number_of_dice)
        ]
    await ctx.send(", ".join(dice))

async def on_error(event, *args, **kwargs):
    with open("err.log", "a+") as f:
        if event == "on_message":
            f.write(f"Unhandled message: {args[0]}\n")
        else:
            raise
        





        
        
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Welcome {member.name} to MorgzLordz. (this is an automated message from Barry The Discord Bot)"
        )

client.run(TOKEN)
bot.run(token)
