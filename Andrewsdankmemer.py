import discord
import tweepy

idtoken = '690532991654559754'
secrettoken = 'z61kcIt_m9mf_Q53seRBWAfhHy8TEMXo'
token = 'NjkwNTMyOTkxNjU0NTU5NzU0.XnS0mQ.RfOWQlG_CHSS2WNEjI-EawBuAxg'


auth = tweepy.OAuthHandler("")
auth.set_access_token("")

api = tweepy.API(auth)

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} Is ready to SpamMemes')

@client.event
async def on_message():
    if "meme" in message.content.lower:
        for tweet in api.search(q="dank memes", lang="en", rpp=10, count=3):
            await message.channel.send("{tweet.text}")

client.run(token)
    
