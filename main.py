# https://discordapp.com/api/oauth2/authorize?client_id=654139568588718090&permissions=116800&scope=bot Link to add puckbot.
import random
import discord
from discord.ext import commands
from discord import Emoji

f = open("token.txt", "r")
token = f.read()
intents = discord.Intents.default()
intents.members = True
intents.presences = True
client= discord.Client(intents=intents)
prefix = "puck"

#topQueue = []
#jgQueue = []
#midQueue = []
#botQueue = []
#supQueue = []

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

    elif prefix+'draft' in message_content:
        await draft(message)

    elif (prefix + "dip") == message_content:
        await client.close()

async def draft(message):
    amongus = discord.Embed(title = 'Roles', description = 'Draft Roles')
    amongus.set_image(url = 'https://cdn.discordapp.com/attachments/505828208982097921/918226847882412072/unknown.png')
    amongus.add_field(name = 'Top: ', value = 'None', inline = False)
    amongus.add_field(name = 'Jungle: ', value = 'None', inline = False)
    amongus.add_field(name = 'Mid: ', value = 'None', inline = False)
    amongus.add_field(name = 'Bot: ', value = 'None', inline = False)
    amongus.add_field(name = 'Sup: ', value = 'None', inline = False)
    amongus.add_field(name = 'Fill', value = 'None', inline = False)

    draft = await message.channel.send('Draft message', embed = amongus)
    await draft.add_reaction('⬆')
    await draft.add_reaction('🌳')
    await draft.add_reaction('↗')
    await draft.add_reaction('⬇')
    await draft.add_reaction('<:fence:862522273022214156>')
    await draft.add_reaction('⬜')
    await draft.add_reaction('🚫')
    #Todo Have a reaction to end the thing, Resolve Role fistfighting, Tyler1 Issue (Multi Role Gods[not fill]),
    #Todo send inprogress instead of constant new ones, role queue system when stuff gets dequeued?
    #Todo  pucknorms sticker later, Discordpy yet to add sticker sending. I think
@client.event
async def on_reaction_add(reaction, user):
    # "queue" is jsut w/ arrays and we only show the fist value everytime and rmeove it when someone dequeues so it then shows the next in line one. how do make array that doesnt reset?
    # downside, when ppl want to swap around they have to go thorugh the whole queue? non issue? discuss. OTherwise have to do other stuff
    reactionMessage = reaction.message
    emoji = reaction.emoji
    if('Draft message' in reactionMessage.content and user.id != client.user.id):
        if(emoji == '⬆'):
            reactionMessage.embeds[0].set_field_at(0, name ='Top: ', value = user.name, inline = False)
            await reactionMessage.edit(embed = reactionMessage.embeds[0])
        elif(emoji == '🌳'):
            reactionMessage.embeds[0].set_field_at(1, name ='Jungle: ', value = user.name, inline = False)
            await reactionMessage.edit(embed = reactionMessage.embeds[0])
        elif(emoji == '↗'):
            reactionMessage.embeds[0].set_field_at(2, name ='Mid: ', value = user.name, inline = False)
            await reactionMessage.edit(embed = reactionMessage.embeds[0])
        elif(emoji == '⬇'):
            reactionMessage.embeds[0].set_field_at(3, name ='Bot: ', value = user.name, inline = False)
            await reactionMessage.edit(embed = reactionMessage.embeds[0])
        elif(isinstance(emoji, Emoji) and emoji.name == 'fence'): #todo doesn't work w/ custom emotes?
            reactionMessage.embeds[0].set_field_at(4, name ='Sup: ', value = user.name, inline = False)
            await reactionMessage.edit(embed = reactionMessage.embeds[0])
        elif(emoji == '⬜'):
            fillQueue = reactionMessage.embeds[0].fields[5].value
            if(fillQueue == 'None'):
                reactionMessage.embeds[0].set_field_at(5, name ='Fill: ', value = user.name, inline = False)
            else:
                reactionMessage.embeds[0].set_field_at(5, name ='Fill: ', value =fillQueue + " " + user.name, inline = False)
            await reactionMessage.edit(embed = reactionMessage.embeds[0])
        elif(emoji == '🚫'):
            blankEmbed = discord.Embed(description = 'No more drafters')
            await reactionMessage.edit(embed = blankEmbed)

@client.event
async def on_reaction_remove(reaction, user):
    reactionMessage = reaction.message
    emoji = reaction.emoji
    if ('Draft message' in reactionMessage.content and user.id != client.user.id):
        if (emoji == '⬆'):
            reactionMessage.embeds[0].set_field_at(0, name='Top: ', value = 'None', inline=False)
            await reactionMessage.edit(embed=reactionMessage.embeds[0])
        elif (emoji == '🌳'):
            reactionMessage.embeds[0].set_field_at(1, name='Jungle: ', value = 'None', inline=False)
            await reactionMessage.edit(embed=reactionMessage.embeds[0])
        elif (emoji == '↗'):
            reactionMessage.embeds[0].set_field_at(2, name='Mid: ', value ='None', inline=False)
            await reactionMessage.edit(embed=reactionMessage.embeds[0])
        elif (emoji == '⬇'):
            reactionMessage.embeds[0].set_field_at(3, name='Bot: ', value ='None', inline=False)
            await reactionMessage.edit(embed=reactionMessage.embeds[0])
        elif (isinstance(emoji, Emoji) and emoji.name == 'fence'):  # todo doesn't work w/ custom emotes?
            reactionMessage.embeds[0].set_field_at(4, name='Sup: ', value ='None', inline=False)
            await reactionMessage.edit(embed=reactionMessage.embeds[0])
        elif (emoji == '⬜'):
            fillQueue = reactionMessage.embeds[0].fields[5].value.split(" ")
            fillQueue.remove(user.name)
            newQueue = " ".join(fillQueue)

            if(len(newQueue) == 0):
                reactionMessage.embeds[0].set_field_at(5, name='Fill: ', value ='None', inline=False)
            else:
                reactionMessage.embeds[0].set_field_at(5, name='Fill: ', value = newQueue, inline=False)

            await reactionMessage.edit(embed=reactionMessage.embeds[0])

client.run(token)
