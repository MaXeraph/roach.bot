import discord
import requests
from discord import Game
from discord.ext import commands
from key import discord_token

CLIENT_PREFIX = ("?", "!", ";;")
TOKEN = discord_token

client = commands.Bot(command_prefix=CLIENT_PREFIX)
client.remove_command('help')

#---------------------------------------
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with your data"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # we do not want the client to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!spawn'):
        msg = 'Hello {0.author.mention}'.format(message)
        msg = 'www.reddit.com/r/all'
        await client.send_message(message.channel, msg)

    if message.content.startswith('/r/'):
        embed = discord.Embed(title="HyperReddit",
                            description='[{}](http://www.reddit.com{})'.format(message.content[3:], message.content),
                            color=0x118ab2)
        await client.send_message(message.channel, embed=embed)

    await client.process_commands(message)

@client.command()
async def help():
    embed = discord.Embed(title="Roach", description="Roach. List of commands are:", color=0xeee657)

    embed.add_field(name="Prefixes", value="**?** OR **!** OR **;;**", inline=False)
    embed.add_field(name="/r/*", value="HyperReddit", inline=False)
    embed.add_field(name="!add", value="Adds two numbers together", inline=False)

    embed.add_field(name="!badroach", value="Badroach", inline=True)
    embed.add_field(name="!goodroach", value="Goodroach", inline=True)
    embed.add_field(name="!roach", value="Generic Algorithm for self-monitoring and enhancement", inline=False)

    await client.say(embed=embed)

@client.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await client.say(left + right)

@client.command()
async def define(obj : str):
    """Returns summary of subject."""
    # await client.send_typing()
    get = requests.get('https://en.wikipedia.org/api/rest_v1/page/summary/{}'.format(obj.replace(' ', '_')))
    json_file = get.json()
    if json_file['type'] != 'disambiguation':
        if json_file['title'] == "Not found.":
            embed = discord.Embed(title="Wiki to prove a point", description="Error 404: Subject not found", color=0x118ab2)
        else:
            embed = discord.Embed(title="Wiki to prove a point", description=json_file['extract'], color=0x118ab2)
            embed.add_field(name="Wikipedia Link", value="[{}]({})".format(obj.title(), json_file["content_urls"]["desktop"]["page"]))
        await client.say(embed=embed)

@client.command()
async def badroach():
    """Bad Roach"""
    # vote -= 1
    await client.say('oops')

@client.command()
async def goodroach():
    """Good Roach"""
    # vote += 1
    await client.say('Yeet')

@client.command()
async def info():
    """Roach's identity"""
    embed = discord.Embed(title="Roachy McRoachface", description="Most random creature of the 5 kingdoms", color=0x118ab2)
    embed.add_field(name="Author", value="MaXeraph")
    embed.add_field(name="Invite", value="lol nah")
    # embed.add_field(name="Merit", value=vote)
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

client.run(TOKEN)
