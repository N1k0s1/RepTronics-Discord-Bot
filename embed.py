import discord
import json 
with open('data.json') as f:
    data = json.load(f)

def genembed(title, version):
        # Define the embed1 variable
        embed1 = discord.Embed(title=title, color=discord.Color.blue())
        product = data['versions'][version]

        embed1.add_field(name="Chip Models", value=product['chipmodels'], inline=False)
        embed1.add_field(name="Features", value="\n".join(product['features']), inline=False) 
        embed1.add_field(name="Price", value=product['price'], inline=True)
        embed1.add_field(name="General Features", value=product['note'], inline=True)

        # Add seller fields
        for seller_name in product['sellers']:
            seller = data['sellers'][seller_name]
            embed1.add_field(name=seller_name, value=seller['store_link'], inline=True)
        return embed1

def sellerembed(title, seller):
        embed = discord.Embed(title=title, color=discord.Color.blue())
        seller = data['sellers'][seller]

        embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
        embed.add_field(name="Discord", value=seller['discord'], inline=False)
        embed.add_field(name="Website", value=seller['store_link'], inline=False)
        return embed