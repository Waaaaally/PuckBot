# https://discordapp.com/api/oauth2/authorize?client_id=654139568588718090&permissions=116800&scope=bot Link to add puckbot.
import random

import discord
import math

f = open("token.txt", "r")
token = f.read()
client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user} exists".format(client))
#on message, receive message -> string -> print in console.

@client.event
async def on_message(message):

    gamernumber = random.randint(1, 50)

    if message.author == client.user:
        return

    elif message.content.startswith('+pucknod'):
        await message.channel.send("https://imgur.com/a/wtKXWjv")

    elif "<:pucknod:801259360395329567>" in str(message.content) and gamernumber == 42: #funny haha 2% puckspam +pucknod
        for i in range(10):
            await message.channel.send("https://imgur.com/a/wtKXWjv")

    elif message.content.startswith('+disagree'):
        await message.channel.send("https://imgur.com/a/DJrsG3F")

    elif message.content.startswith('+clown'):
        if gamernumber%2 == 0:
            await message.channel.send("https://imgur.com/a/aI8GMPn")
        else:
            await message.channel.send("https://imgur.com/a/MEDtGgs")

    elif "+puck.dip" == message.content:
        await client.close()

client.run(token)

