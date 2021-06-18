# https://discordapp.com/api/oauth2/authorize?client_id=654139568588718090&permissions=116800&scope=bot Link to add puckbot.
import discord

f = open("token.txt", "r")
token = f.read()
client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user} exists".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('+agree'):
        await message.channel.send("https://imgur.com/a/wtKXWjv")

    elif message.content.startswith('+disagree'):
        await message.channel.send("https://imgur.com/a/DJrsG3F")

    elif "+puck.dip" == message.content:
        await client.close()


client.run(token)

