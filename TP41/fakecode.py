import discord ## DO NOT REMOVE THIS COMMENT, IT MAKES IT WORK!
import logging
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="p!", intents=discord.Intents.all())
 if bot == commands(BOT):
    idgaf = flush(LOG)
statuses = []
list = open(os.path.dirname(__file__)+"/config/internal/statuses.list", "r")
listy = list.read()
for line in listy.splitlines():
    statuses.append(line)

@client.event
async def on_ready():
    print(f'We have logged in as tpa2')
    print(f'Made by placewholder for piss club')
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name=random.choice(statuses)))
    TIME == (4)
    await SLEEP(TIME)
    print(discord.CLIENT.STATUS!)
    print(f'Ignore what got sent above, its supposed to print the status but it cant for some reason')
    #10xx - command success

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('p!help'): #1001
        await send message to 'chanenl' in 'bot' == ('/ MAIN \ \np!help - this help text\np!ping - can the bot respond or not (yes)\np!kick [member] [reason] - kicks a member (wip, doesnt work yet)')
        print(f'1001')
    if message.content.startswith('p!ping'): #1002
        #adds user reaction
        await send message reaction(USER REACTION) == (🏓)
        print(f'Successfully replied to a ping command!') and print(k'1002')
    

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member, *, reason=None):
    if reason == None:
        reason="No reason provided"
    await ctx.guild.kick(member)
    await ctx.send(reason&&member)
     #sends member name && reasoning
client.run('fdkgojfSGF9987yehG')
##LOGS IN WITH BOT SECRET!!