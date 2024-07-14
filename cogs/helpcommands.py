id = [1261831251254317066]

import discord
from discord.ext import commands
import json

with open('data.json') as f:
    data = json.load(f)

class HelpCommands(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="gen2", description="Display information about Generation 2 AirPods", guild_id = id)
    async def gen2info(interaction: discord.Interaction, context):
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


    @discord.slash_command(name="gen3", description="Display information about Generation 3 AirPods", guild_id = id)
    async def gen3info(interaction: discord.Interaction, context):
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

    @discord.slash_command(name="pro1", description="Display information about Pro 1 AirPods", guild_id = id)
    async def pro1info(interaction: discord.Interaction, context):
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

    @discord.slash_command(name="pro2", description="Display information about Pro 2 AirPods", guild_id = id)
    async def pro2info(interaction: discord.Interaction, context):
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

    @discord.slash_command(name="maxes", description="Display information about AirPod Maxes", guild_id = id)
    async def maxesinfo(interaction: discord.Interaction, context):
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



    @discord.slash_command(name="hicity", description="Information about HiCity", guild_id = id)
    async def hicity(interaction: discord.Interaction, context):
        embed = discord.Embed(title="HiCity", color=discord.Color.blue())
        seller = data['sellers']['HiCity']

        embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
        embed.add_field(name="Discord", value=seller['discord'], inline=False)
        embed.add_field(name="Website", value=seller['store_link'], inline=False)
        await interaction.response.send_message(embed=embed)

    @discord.slash_command(name="dyson", description="Information about Dyson", guild_id = id)
    async def dyson(interaction: discord.Interaction, context):
        embed = discord.Embed(title="Dyson", color=discord.Color.blue())
        seller = data['sellers']['Dyson']

        embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
        embed.add_field(name="Discord", value=seller['discord'], inline=False)
        embed.add_field(name="Website", value=seller['store_link'], inline=False)

        await interaction.response.send_message(embed=embed)

    @discord.slash_command(name="jenny", description="Information about Jenny", guild_id = id)
    async def jenny(interaction: discord.Interaction, context):
        embed = discord.Embed(title="Jenny", color=discord.Color.blue())
        seller = data['sellers']['Jenny']

        embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
        embed.add_field(name="Discord", value=seller['discord'], inline=False)
        embed.add_field(name="Website", value=seller['store_link'], inline=False)

        await interaction.response.send_message(embed=embed)

    @discord.slash_command(name="beschan", description="Information about Beschan", guild_id = id)
    async def gen2info(interaction: discord.Interaction, context):
        embed = discord.Embed(title="Beschan", color=discord.Color.blue())
        seller = data['sellers']['Beschan']

        embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
        embed.add_field(name="Discord", value=seller['discord'], inline=False)
        embed.add_field(name="Website", value=seller['store_link'], inline=False)

        await interaction.response.send_message(embed=embed)

    @discord.slash_command(name="mikeym", description="Information about Mike-YM", guild_id = id)
    async def mikeym(interaction: discord.Interaction, context):
        embed = discord.Embed(title="Mike-YM", color=discord.Color.blue())
        seller = data['sellers']['Mike-YM']

        embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
        embed.add_field(name="Discord", value=seller['discord'], inline=False)
        embed.add_field(name="Website", value=seller['store_link'], inline=False)

        await interaction.response.send_message(embed=embed)

    @discord.slash_command(name="jdfoot", description="Information for JD-Foot", guild_id = id)
    async def gen2info(interaction: discord.Interaction, context):
        embed = discord.Embed(title="JD-Foot", color=discord.Color.blue())
        seller = data['sellers']['JdFoot']

        embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
        embed.add_field(name="Discord", value=seller['discord'], inline=False)
        embed.add_field(name="Website", value=seller['store_link'], inline=False)

        await interaction.response.send_message(embed=embed)

    @discord.slash_command(name="bxm", description="Information for BXM", guild_id = id)
    async def bxm(interaction: discord.Interaction, context):
        embed = discord.Embed(title="BXM", color=discord.Color.blue())
        seller = data['sellers']['BXM']

        embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
        embed.add_field(name="Discord", value=seller['discord'], inline=False)
        embed.add_field(name="Website", value=seller['store_link'], inline=False)

        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(HelpCommands(bot))
