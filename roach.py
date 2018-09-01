import discord
from discord import Game
from discord.ext import commands

CLIENT_PREFIX = ("?", "!", ";;")
TOKEN = 'NDg1Mzg2MDA0Nzg2ODM5NTUy.Dmv2Fw.lhl0KIzKK_mgwHzUTph-RdFes-E'

client = commands.Bot(command_prefix=CLIENT_PREFIX)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with data"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await client.say(left + right)

@client.command()
async def badroach():
    """Bad Roach"""
    await client.say('oops')

@client.command()
async def info():
    """Roach's identity"""
    embed = discord.Embed(title="Roachy McRoachface", description="Most random creature of the 5 kingdoms", color=0x118ab2)
    embed.add_field(name="Author", value="MaXeraph")
    embed.add_field(name="Invite", value="lol nah")
    await client.say(embed=embed)

@client.command()
async def roach(content : str):
    """General enquiries"""
    operations = ['+', '-', '*', '//', 'add', 'minus','multiply', 'divide']
    for op in operations:
        if op in content:
            if op == operations[0] or op == 'add':
                num1 = int(content[:content.find(operations[0])])
                num2 = int(content[content.find(operations[0]) + 1:])
                await client.say(num1 + num2)
            elif op == operations[1] or op == 'minus':
                num1 = int(content[:content.find(operations[1])])
                num2 = int(content[content.find(operations[1]) + 1:])
                await client.say(num1 - num2)
            elif op == operations[2] or op == 'multiply':
                num1 = int(content[:content.find(operations[2])])
                num2 = int(content[content.find(operations[2]) + 1:])
                await client.say(num1 * num2)
            elif op == operations[3] or op == 'divide':
                num1 = int(content[:content.find(operations[2])])
                num2 = int(content[content.find(operations[2]) + 1:])
                await client.say(num1 // num2)

# @client.command()
# async def spotify():
#     if spot_token:
#         title, artist, device = get_data()
#         if device is None or title is None or artist is None:
#             await client.send_message(message.channel, 'Player not found')
#         else:
#             msg = 'Spotify is currently playing %s | %s on %s' % (title, artist, device)
#             await client.send_message(message.channel, msg)
#     else:
#         await client.send_message(message.channel, 'Spotify is not connected')

# @client.event
# async def on_message(message):
#     # we do not want the client to reply to itself
#     if message.author == client.user:
#         return
#
#     if message.content.startswith('!spawn'):
#         msg = 'Hello {0.author.mention}'.format(message)
#         await client.send_message(message.channel, msg)


client.run(TOKEN)
