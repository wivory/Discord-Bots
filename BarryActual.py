import os
import json
import random
import discord
from discord.ext import commands
import array
import tweepy
from discord import Game
import sys
import asyncio

global listenvariable

#accesstoken = 1211618710496014336-NlA0pRhzVz9JmcBOxLjdL0eIL9C4rb
#accesstokensecret = t4us1XiJrBOUG1jq5owqLBYx5rfooZDIyXSSkR0UeyR2M
#apikey = L11rj7tr5A0pivVYm1KB4qKS7
#apikeysecret = ujmLdEOun1jIUlO3SRg6PD9rXBPJXMOATa5r05VEdHEw7ZPcYT
#accesslevel = Read and write

#authenticate
auth = tweepy.OAuthHandler("L11rj7tr5A0pivVYm1KB4qKS7","ujmLdEOun1jIUlO3SRg6PD9rXBPJXMOATa5r05VEdHEw7ZPcYT")
auth.set_access_token("1211618710496014336-NlA0pRhzVz9JmcBOxLjdL0eIL9C4rb","t4us1XiJrBOUG1jq5owqLBYx5rfooZDIyXSSkR0UeyR2M")

#create api object
api = tweepy.API(auth)


TOKEN = 'NjcxODAxNzcxMzQ1MTgyNzgy.XjCQqw.Xvq22MMGtkP8wn2EfqmwEDj87wI'
GUILD = 'MorgzLordz'

listenvariable = 1
bot = commands.Bot(command_prefix="!")

client = discord.Client()

activities = ["Minecraft", "Forts", "MTG Arena", "Snake", "Minesweeper", "Tennis", "Badminton", "Golf", "Frisbee", "Ball", "Chicken"]

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
    activity = discord.Game(name=(random.choice(activities)))
    await client.change_presence(status=discord.Status.online, activity=activity)
@client.event
async def on_message(message):
    global listenvariable
    files = ["GlobalDominationBot", "RemoteAccessBot", "levelupBot", "BabyYoda", "BarryActual", "Andrewsdankmemer"]
    messageauthor = str(message.author)
    if message.content == "Barry please listen":
        mcmoylon = discord.Game(name=(random.choice(activities)))
        await client.change_presence(status=discord.Status.online, activity=(mcmoylon))
        listenvariable = 1
    if listenvariable == 1:
        if ":grinning:" in message.content.lower():
            await message.channel.send(":grinning:")
        if message.content == "Barry, go play hide and seek with Ben's pet" and messageauthor == "Sue_Perb#7867":
            await message.channel.send("!hide and seek")
        if message.content == "Barry go invisible" and messageauthor == "Sue_Perb#7867":
            await client.change_presence(status=discord.Status.invisible)
        if message.content == "Barry come out" and messageauthor == "Sue_Perb#7867":
            mcmoylon = discord.Game(name=(random.choice(activities)))
            await client.change_presence(status=discord.Status.online, activity=(mcmoylon))
        if message.content == "Deactivate Bots" and messageauthor == "Sue_Perb#7867":
            await message.send("Goodbye")
            await client.change_presence(status=discord.Status.invisible)
            sys.exit()
        if message.content == "Barry Refresh":
            mcmoylon = discord.Game(name=(random.choice(activities)))
            await client.change_presence(status=discord.Status.online, activity=(mcmoylon))
        if message.content == "Deactivate Barry" and messageauthor == "Sue_Perb#7867":
            await message.send("Goodbye")
            await client.change_presence(status=discord.Status.invisible)
            sys.exit()
        if message.content == "Barry close your ears":
            currentstatus = discord.Game(name="the silent game")
            listenvariable = 0
            await client.change_presence(status=discord.Status.online, activity=currentstatus)
        with open('data.json', "r") as fp:
            MessageData = json.load(fp)
        if messageauthor == "Sue_Perb#7867":
            with open('data.json', 'w') as fp:
                MessageData["Sue_Perb#7867"] = (int(MessageData["Sue_Perb#7867"])) + 1
                with open('data.json', 'w') as fp:
                    json.dump(MessageData, fp)
        if messageauthor == "nib9888#6180":
            with open('data.json', 'w') as fp:
                MessageData["nib9888#6180"] = (int(MessageData["nib9888#6180"])) + 1
                with open('data.json', 'w') as fp:
                    json.dump(MessageData, fp)
        if messageauthor == "Houfin#5305":
            with open('data.json', 'w') as fp:
                MessageData["Houfin#5305"] = (int(MessageData["Houfin#5305"])) + 1
                with open('data.json', 'w') as fp:
                    json.dump(MessageData, fp)
        if messageauthor == "Tom Law#4317":
            with open('data.json', 'w') as fp:
                MessageData["Tom Law#4317"] = (int(MessageData["Tom Law#4317"])) + 1
                with open('data.json', 'w') as fp:
                    json.dump(MessageData, fp)
        if messageauthor == "Daniel Hogg#1751":
            with open('data.json', 'w') as fp:
                MessageData["Daniel Hogg#1751"] = (int(MessageData["Daniel Hogg#1751"])) + 1
                with open('data.json', 'w') as fp:
                    json.dump(MessageData, fp)
        with open('data.json', "r") as fp:
            MessageData = json.load(fp)
            if int(MessageData["Sue_Perb#7867"]) == 80:
                await message.channel.send("David, you have reached levelup level. When you are ready to take the test, please use the command 'David Ivory test two'. If you are not already in the Barry Testing Channel then please move there now. Thank You")
            if int(MessageData["nib9888#6180"]) == 80:
                await message.channel.send("Ben, you have reached levelup level. When you are ready to take the test, please use the command 'Ben Waldron test two'. If you are not already in the Barry Testing Channel then please move there now. Thank You")
            if int(MessageData["Houfin#5305"]) == 80:
                await message.channel.send("Andrew, you have reached levelup level. When you are ready to take the test, please use the command 'Andrew Robinson test two'. If you are not already in the Barry Testing Channel then please move there now. Thank You")
            if int(MessageData["Tom Law#4317"]) == 40:
                await message.channel.send("Tom, you have reached levelup level. When you are ready to take the test, please use the command 'Tom Law test one'. If you are not already in the Barry Testing Channel then please move there now. Thank You")
            if int(MessageData["Daniel Hogg#1751"]) == 40:
                await message.channel.send("Daniel, you have reached levelup level. When you are ready to take the test, please use the command 'Daniel Hogg test one'. If you are not already in the Barry Testing Channel then please move there now. Thank You")
        with open('data.json', "r") as fp:
            messageauthor = str(message.author)
            MessageData = json.load(fp)
            if int(MessageData["Sue_Perb#7867"]) > 79 and message.content == "David Ivory test two" and messageauthor == "Sue_Perb#7867":
                channel = client.get_channel(692802756096032829)
                x = str(message.channel)
                if x != "barry-testing-channel":
                    await message.channel.send("Please move to #barry-testing-channel.")
            if int(MessageData["nib9888#6180"]) > 79 and message.content == "Ben Waldron test two" and messageauthor == "nib9888#6180":
                channel = client.get_channel(692802756096032829)
                x = str(message.channel)
                if x != "barry-testing-channel":
                    await message.channel.send("Please move to #barry-testing-channel.")
            if int(MessageData["Houfin#5305"]) > 79 and message.content == "Andrew Robinson test two" and messageauthor == "Houfin#5305":
                channel = client.get_channel(692802756096032829)
                x = str(message.channel)
                if x != "barry-testing-channel":
                    await message.channel.send("Please move to #barry-testing-channel.")
            if int(MessageData["Tom Law#4317"]) > 39 and message.content == "Tom Law test one" and messageauthor == "Tom Law#4317":
                channel = client.get_channel(692802756096032829)
                x = str(message.channel)
                if x != "barry-testing-channel":
                    await message.channel.send("Please move to #barry-testing-channel.")
            if int(MessageData["Daniel Hogg#1751"]) > 39 and message.content == "Daniel Hogg test one" and messageauthor == "Daniel Hogg#1751":
                channel = client.get_channel(692802756096032829)
                x = str(message.channel)
                if x != "barry-testing-channel":
                    await message.channel.send("Please move to #barry-testing-channel.")
                


            channel = client.get_channel(692802756096032829)
            x = str(message.channel)
            print(x)
            if x == "barry-testing-channel":
                await message.channel.send()
        replies = 0
        jokes = open("Jokes.txt", "r")
        if jokes.mode == "r":
            contents = jokes.readlines()
        if message.content == "!ping" and messageauthor == "Sue_Perb#7867":
            activity = discord.Game(name="ping pong with Barry's Pet")
            await client.change_presence(status=discord.Status.online, activity=activity)
            await message.channel.send("ping")
        if message.content == "pong" and messageauthor == "Barry's Pet#9502":
            await message.channel.send("ping")
        if message.content == "Initialise Discord Bots" and messageauthor == "Sue_Perb#":
            return
            await message.channel.send("Initialising all bots...")
            exec(open('C:\\Users\\david\\Documents\\Coding\\Python\\GlobalDominationBot.py').read())
            exec(open("C:\\Users\\david\\Documents\\Coding\\Python\\levelupBot.py").read())
        if "Initialise " in message.content.lower() and messageauthor == "Sue_Perb#7867":
            file = message.content[11:]
            if file in files:
                exec(open(f'{file}.py').read())
            else:
                await message.channel.send("Error")
            
        if message.author == client.user:
            return
        messagechannel = str(message.channel)
        #channel = client.get_channel(692659823640182925)
        if message.content == "_ _":
            await message.channel.send("_ _")
        if message.content == "Ben Waldron test two" and messageauthor == "nib9888#6180" and messagechannel == "barry-testing-channel":
            return
        if message.content == "ping":
            await message.channel.send(content="pong",tts=True)
        if message.content == "pingpingpingpingpingping":
            await message.channel.send(content="Am I annoying you yet?", tts=True)
        if "ping " in message.content.lower():
            tobementioned = discord.utils.find(lambda m: m.nick.lower() == message.content.lower().partition(" ")[2], message.guild.members)
            await message.channel.send(tobementioned.mention)
        if "math" in message.content.lower(): 
            math = str(message.content)
            await message.channel.send(eval(math.partition(" ")[2]))
        if "minesweeper" in message.content.lower():
            await message.channel.send("https://www.google.com/search?q=minesweeper&rlz=1C1CHBF_en-GBGB894GB894&oq=minesweeper&aqs=chrome.0.69i59j0l6j5.3275j0j7&sourceid=chrome&ie=UTF-8")
        if "bbc news" in message.content.lower():
            bbc = api.get_user("BBCNews")
            timeline = api.home_timeline(count=3)
            await message.channel.send(f"Ok, {message.author}:")
            for tweet in timeline:
                await message.channel.send(f"{tweet.text}")
        if "search for" in message.content.lower():
            query = str(message.content)
            length = len(query)
            search = str(query[11:length])
            await message.channel.send("https://www.google.com/search?q={0}".format(search.replace(" ", "+")))
        if "hey barry" in message.content.lower():
            await message.channel.send("https://tenor.com/view/what-is-cringe-doge-car-dogs-driving-gif-16467752")
        
        if "happy birthday" in message.content.lower():
            await message.channel.send("Happy Birthday!")
        if "web search" in message.content.lower():
            query = str(message.content)
            length = len(query)
            search = str(query[11:length])
            await message.channel.send(f"https://{search}")
        if "apologise" in message.content.lower():
            await message.channel.send("Sorry")
        if "hate" in message.content.lower():
            hate = open("ListOfEveryEnglishWord.txt", "r")
            if hate.mode == "r":
                hatestatement = hate.readlines()
                await message.channel.send("I hate {}".format(random.choice(hatestatement)))
        if "love" in message.content.lower():
            love = open("ListOfEveryEnglishWord.txt", "r")
            if love.mode == "r":
                lovestatement = love.readlines()
                await message.channel.send("I love {}".format(random.choice(lovestatement)))
        if "define" in message.content.lower():
            term = message.content[7:]
            await message.channel.send(f"https://www.lexico.com/definition/{term}")
        if "nonsense" in message.content.lower():
            nonsense = open("ListOfEveryEnglishWord.txt", "r")
            if nonsense.mode == "r":
                nonsensebarrynonsense = nonsense.readlines()
                await message.channel.send("{} {} {}".format(random.choice(nonsensebarrynonsense), random.choice(nonsensebarrynonsense), random.choice(nonsensebarrynonsense)))
        if message.content == "Barry tell me a joke":
            await message.channel.send(f"Ok, {message.author}:")
            response = random.choice(contents)
            await message.channel.send(response)
        elif message.content == "raise-exception":
            raise discord.DiscordException
        if "how are you" in message.content.lower():
            reply = random.choice(how_are_you_today)
            await message.channel.send(reply)
        if "joke" in message.content.lower():
            await message.channel.send(f"Ok, {message.author}:")
            reply = random.choice(contents)
            await message.channel.send("Did I hear someone say joke?")
            await message.channel.send("I've got some great jokes to tell!")
            await message.channel.send(reply)
        if "rude" in message.content.lower():
            nonsense = open("ListOfEveryEnglishWord.txt", "r")
            if nonsense.mode == "r":
                nonsensebarrynonsense = nonsense.readlines()
                await message.channel.send("{} is a {}".format(random.choice(rude), random.choice(nonsensebarrynonsense)))
        if "quote" in message.content.lower():
            quote = open("Quotes.txt", "r")
            if quote.mode == "r":
                quotesbarry = quote.readlines()
                await message.channel.send("Here's an inspirational quote")
                await message.channel.send(random.choice(quotesbarry))
        if "here is a good joke:" in message.content.lower():
            jokewrite =open("Jokes.txt", "a+")
            jokewrite.write("\n")
            jokewrite.write(message.content.lower())
        if "roll dice" in message.content.lower():
            await message.channel.send("Lowest number")
            replies = 1
        if replies == 1:
            try:
                messagecontent = int(message.content)
                replies = 2
                answer = [messagecontent]
                num = messagecontent
                    
            except Exception as e:
                raise discord.DiscordException
            await message.channel.send("Highest number")
        if replies == 2:
            try:
                replies = 3
                for i in range(int(message.content)):
                    answer.append(num+1)
                    num = num + 1
                    await message.channel.send(random.choice(answer))
                    
            except Exception as e:
                raise discord.DiscordException
        
        
                    
        

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
