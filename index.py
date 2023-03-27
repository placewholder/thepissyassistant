import discord
import logging
import os
import random
import datetime
import asyncio
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="p!", intents=discord.Intents.all())

statuses = []
list = open(os.path.dirname(__file__)+"/config/internal/statuses.list", "r")
listy = list.read()
for line in listy.splitlines():
    statuses.append(line)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(f'Made by placewholder')
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name=random.choice(statuses)))
    await asyncio.sleep(4)
    print(discord.activity.Game)
    print(f'Ignore what got sent above, its supposed to print the status but it cant for some reason')
    #10xx - command success
    #xx - command code for 10xx
    #Ax - code for non-commands, displayed as 10Ax
    #Bx - code for embeds, displayed as 10Bx <--- SCRAPPED

@client.event
async def on_message(message):
    #A0
    if message.author == client.user:
        return
        print(f'10A0') #<-- that right there. It doesn't work anyways but I left it in just in case.
                        #yes I'm talking to you, code reader, who else I'd be talking to?
    
    #00
    if message.content.startswith('p!help'):
        await message.channel.send('/ MAIN \ \np!help - this help text\np!ping - can the bot respond or not (yes)\np!credits - the people who made the bot\np!blank - sends a blank message')
        print(f'1000')
    
    #01
    if message.content.startswith('p!ping'):
        #await message.channel.send('🏓 Pong!')  <-- useless, again. the bot gives a reaction instead.
        await message.add_reaction('🏓')
        print(f'1001')
    
    #02
    if message.content.startswith('p!credits'):
        await message.channel.send('Placewholder - made the 2.0 bot (this one)\nJellybean (Misko2356) - emotional support, help, ideas, made the original bot\nThis server - emotional support, ideas\nMade with discord.py, hosted on placewholders pc')
        print(f'1002')
    
    ## But now, a quick interruption from the Ax section! ##
    #A1
    #if message.content.startswith('p!'):
    #    await message.channel.send('Want to know my commands? Do "p!help" (without quotation marks)!')
    #    print(f'10A1')
    #A1 was scrapped.
    
    #A2 -- Spyware :trolley:
    if message.content.startswith('piss'):
        print(f'10A2')
        print(f'placewholder are you really committing China on a simple server?')
    ## Back to xx! ##
    
    #03
    if message.content.startswith('p!blank'):
        await message.delete()
        await message.channel.send('‎ ')
    
    ## Now an interruption from Ax! (again) ##
    
    #A3
    if "nigger" in message.content:
        print(f'Racism detected in server!')
        print(f'10A3')
    
    ## End of Ax ##
    
    #btw from now on the code will be more fancy I'm lazy to organize the previous bits of code

#@bot.command()    failed kick command
#@commands.has_permissions(kick_members=True)
#async def kick(ctx, member:discord.Member, *, reason=None):
#    if reason == None:
#        reason="No reason provided"                                        ##To whoever is reading the code,
#    await ctx.guild.kick(member)                                           ##please help with the kick command
#    await message.channel.send('the command is wip rn')                    ##Love, placewholder <3
#    await ctx.send(f"User {member.mention} has been kicked for {reason}")  
