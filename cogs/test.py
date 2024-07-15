id = [1261831251254317066]

import discord
from discord.ext import commands
import json

with open('data.json') as f:
    data = json.load(f)

class Test(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

class Gen2View(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(discord.ui.Button(label='Button 1', custom_id='button1'))
        self.add_item(discord.ui.Button(label='Button 2', custom_id='button2'))
        self.add_item(discord.ui.Button(label='Button 3', custom_id='button3'))
        self.add_item(discord.ui.Button(label='Button 4', custom_id='button4'))

# EMBED1
        embed1 = discord.Embed(title="Gen 3", color=discord.Color.blue())
        product = data['versions']['gen3']

        embed1.add_field(name="Chip Models", value=product['chipmodels'], inline=False)
        embed1.add_field(name="Features", value="\n".join(product['features']), inline=False) 
        embed1.add_field(name="Price", value=product['price'], inline=True)
        embed1.add_field(name="Notes", value=product['note'], inline=True)

        # Add seller fields
        for seller_name in product['sellers']:
            seller = data['sellers'][seller_name]
            embed1.add_field(name=seller_name, value=seller['store_link'], inline=True)



    @discord.ui.button(label='Button 1', custom_id='button1')
    async def on_button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        # Define the embed1 variable
        embed1 = discord.Embed(title="Gen 2", color=discord.Color.blue())
        product = data['versions']['gen2']

        embed1.add_field(name="Chip Models", value=product['chipmodels'], inline=False)
        embed1.add_field(name="Features", value="\n".join(product['features']), inline=False) 
        embed1.add_field(name="Price", value=product['price'], inline=True)
        embed1.add_field(name="Notes", value=product['note'], inline=True)

        # Add seller fields
        for seller_name in product['sellers']:
            seller = data['sellers'][seller_name]
            embed1.add_field(name=seller_name, value=seller['store_link'], inline=True)

        # Send the first embed
        await interaction.response.send_message('Button 1', embed=embed1, ephemeral=True)

    # Repeat for the other buttons

@discord.slash_command(name="gen2", description="Show the gen 2 menu", guild_id = id)
async def gen2(ctx):
    view = Gen2View()
    await ctx.respond('Choose an option:', view=view)

def setup(bot):
    bot.add_cog(Test(bot))