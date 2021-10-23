# https://discordapp.com/api/oauth2/authorize?client_id=654139568588718090&permissions=116800&scope=bot Link to add puckbot.
import random
import discord

f = open("token.txt", "r")
token = f.read()
client = discord.Client()
prefix = "puck"

@client.event
async def on_ready():
    print(f"{client.user} exists".format(client))

@client.event
async def on_message(message):
    
    gamernumber = random.randint(1, 50)

    message_content = message.content.lower()

    if message.author == client.user:
        return

    elif message_content.startswith(prefix + 'nod'):
        await message.channel.send("https://imgur.com/a/wtKXWjv")

    elif ("<:pucknod:801259360395329567>" or "pucknod" or "Pucknod") in str(message_content) and gamernumber == 42: #funny haha 2% puckspam +pucknod
        for i in range(10):
            await message.channel.send("https://imgur.com/a/wtKXWjv")

    elif message_content.startswith(prefix + 'disagree'):
        await message.channel.send("https://imgur.com/a/DJrsG3F")

    elif message_content.startswith(prefix + 'cringe'):
        await message.channel.send("https://imgur.com/a/m6WA6zo")

    elif message_content.startswith(prefix + 'clown'):
        if gamernumber%2 == 0:
            await message.channel.send("https://imgur.com/a/aI8GMPn")
        else:
            await message.channel.send("https://imgur.com/a/MEDtGgs")

    elif message_content.startswith(prefix + 'angry'):
        await message.channel.send("https://imgur.com/a/3PKgCmC")

    elif message_content.startswith(prefix + 'cock'):
        await message.channel.send("https://imgur.com/a/t57bTOK")

    elif message_content.startswith(prefix + 'based'):
        await message.channel.send("https://imgur.com/a/B7v3Vff")

    elif message_content.startswith(prefix + 'bruh'):
        await message.channel.send("https://imgur.com/a/FPG3JAT")

    elif message_content.startswith(prefix + 'happy'):
        await message.channel.send("https://imgur.com/a/HE30d03")

    elif (prefix + "dip") == message_content:
        await client.close()

client.run(token)

