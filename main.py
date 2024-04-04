import discord
import json
from discord.ext import commands
from discord import app_commands
import json
import logging

TOKEN = 'MTE0OTQ1MDA3MTQyODA0Njg4MA.GxI4qY.baleW3fU37oTdg0ReOimGXjbtv-qI_uTjw1yYY' 
intents = discord.Intents.default()
intents.members = True # Example: Enable member events
intents.message_content = True  # Enable the message_content intent
intents.presences = True  # Enable the presence intent

bot = commands.Bot(command_prefix='/', case_insensitive=True, intents=intents)

with open('data.json') as f:
    data = json.load(f)

tree = bot._connection._command_tree 

@bot.command(name='sync', description='Owner only')
async def sync(interaction: discord.Interaction):
        await tree.sync()
        print('Command tree synced.')



@bot.tree.command(name="gen2", description="Display information about Generation 2 AirPods")
async def gen2info(interaction: discord.Interaction):
    embed = discord.Embed(title="Gen 2", color=discord.Color.blue())
    product = data['versions']['gen2']

    embed.add_field(name="Chip Models", value=product['chipmodels'], inline=False)
    embed.add_field(name="Features", value="\n".join(product['features']), inline=False) 
    embed.add_field(name="Price", value=product['price'], inline=True)
    embed.add_field(name="Notes", value=product['note'], inline=True)

    # Add seller fields
    for seller_name in product['sellers']:
        seller = data['sellers'][seller_name]
        embed.add_field(name=seller_name, value=seller['store_link'], inline=True)

    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="gen3", description="Display information about Generation 3 AirPods")
async def gen3info(interaction: discord.Interaction):
    embed = discord.Embed(title="Gen 3", color=discord.Color.blue())
    product = data['versions']['gen3']

    embed.add_field(name="Chip Models", value=product['chipmodels'], inline=False)
    embed.add_field(name="Features", value="\n".join(product['features']), inline=False) 
    embed.add_field(name="Price", value=product['price'], inline=True)
    embed.add_field(name="Notes", value=product['note'], inline=True)

    # Add seller fields
    for seller_name in product['sellers']:
        seller = data['sellers'][seller_name]
        embed.add_field(name=seller_name, value=seller['store_link'], inline=True)

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="pro1", description="Display information about Pro 1 AirPods")
async def pro1info(interaction: discord.Interaction):
    embed = discord.Embed(title="Pro 1", color=discord.Color.blue())
    product = data['versions']['pro1']

    embed.add_field(name="Chip Models", value=product['chipmodels'], inline=False)
    embed.add_field(name="Features", value="\n".join(product['features']), inline=False) 
    embed.add_field(name="Price", value=product['price'], inline=True)
    embed.add_field(name="Notes", value=product['note'], inline=True)

    # Add seller fields
    for seller_name in product['sellers']:
        seller = data['sellers'][seller_name]
        embed.add_field(name=seller_name, value=seller['store_link'], inline=True)

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="pro2", description="Display information about Pro 2 AirPods")
async def pro2info(interaction: discord.Interaction):
    embed = discord.Embed(title="Pro 2", color=discord.Color.blue())
    product = data['versions']['pro2']

    embed.add_field(name="Chip Models", value=product['chipmodels'], inline=False)
    embed.add_field(name="Features", value="\n".join(product['features']), inline=False) 
    embed.add_field(name="Price", value=product['price'], inline=True)
    embed.add_field(name="Notes", value=product['note'], inline=True)

    # Add seller fields
    for seller_name in product['sellers']:
        seller = data['sellers'][seller_name]
        embed.add_field(name=seller_name, value=seller['store_link'], inline=True)

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="maxes", description="Display information about AirPod Maxes")
async def maxesinfo(interaction: discord.Interaction):
    embed = discord.Embed(title="Maxes", color=discord.Color.blue())
    product = data['versions']['maxes']

    embed.add_field(name="Chip Models", value=product['chipmodels'], inline=False)
    embed.add_field(name="Features", value="\n".join(product['features']), inline=False) 
    embed.add_field(name="Price", value=product['price'], inline=True)
    embed.add_field(name="Notes", value=product['note'], inline=True)

    # Add seller fields
    for seller_name in product['sellers']:
        seller = data['sellers'][seller_name]
        embed.add_field(name=seller_name, value=seller['store_link'], inline=True)

    await interaction.response.send_message(embed=embed)



@bot.tree.command(name="hicity", description="Information about HiCity")
async def hicity(interaction: discord.Interaction):
    embed = discord.Embed(title="HiCity", color=discord.Color.blue())
    seller = data['sellers']['HiCity']

    embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
    embed.add_field(name="Discord", value=seller['discord'], inline=False)
    embed.add_field(name="Website", value=seller['store_link'], inline=False)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="dyson", description="Information about Dyson")
async def dyson(interaction: discord.Interaction):
    embed = discord.Embed(title="Dyson", color=discord.Color.blue())
    seller = data['sellers']['Dyson']

    embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
    embed.add_field(name="Discord", value=seller['discord'], inline=False)
    embed.add_field(name="Website", value=seller['store_link'], inline=False)

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="jenny", description="Information about Jenny")
async def jenny(interaction: discord.Interaction):
    embed = discord.Embed(title="Jenny", color=discord.Color.blue())
    seller = data['sellers']['Jenny']

    embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
    embed.add_field(name="Discord", value=seller['discord'], inline=False)
    embed.add_field(name="Website", value=seller['store_link'], inline=False)

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="beschan", description="Information about Beschan")
async def gen2info(interaction: discord.Interaction):
    embed = discord.Embed(title="Beschan", color=discord.Color.blue())
    seller = data['sellers']['Beschan']

    embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
    embed.add_field(name="Discord", value=seller['discord'], inline=False)
    embed.add_field(name="Website", value=seller['store_link'], inline=False)

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="mikeym", description="Information about Mike-YM")
async def mikeym(interaction: discord.Interaction):
    embed = discord.Embed(title="Mike-YM", color=discord.Color.blue())
    seller = data['sellers']['Mike-YM']

    embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
    embed.add_field(name="Discord", value=seller['discord'], inline=False)
    embed.add_field(name="Website", value=seller['store_link'], inline=False)

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="jdfoot", description="Information for JD-Foot")
async def gen2info(interaction: discord.Interaction):
    embed = discord.Embed(title="JD-Foot", color=discord.Color.blue())
    seller = data['sellers']['JdFoot']

    embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
    embed.add_field(name="Discord", value=seller['discord'], inline=False)
    embed.add_field(name="Website", value=seller['store_link'], inline=False)

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="bxm", description="Information for BXM")
async def bxm(interaction: discord.Interaction):
    embed = discord.Embed(title="BXM", color=discord.Color.blue())
    seller = data['sellers']['BXM']

    embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
    embed.add_field(name="Discord", value=seller['discord'], inline=False)
    embed.add_field(name="Website", value=seller['store_link'], inline=False)

    await interaction.response.send_message(embed=embed)

@bot.event 
async def on_ready():
    await tree.sync(guild=discord.Object(id=1224260115188809728)) # REMEMBER TO UPDATE GUILD ID
    print(f"We have logged in as {bot.user}")

bot.run(TOKEN) 
