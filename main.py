id = [1261831251254317066]
import discord
bot = discord.Bot()
#Testing
import json 
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.sync_commands()
    print(f"Succesfully synced commands")

@bot.slash_command(name="loadcog", description= "Loads a cog of the users choosing", guild_id = id)
async def cogs(ctx, cogs):
    if cogs in cogs:
        bot.load_extension(f'cogs.{cogs}')
        await ctx.respond(f"Successfully loaded {cogs}")
    else:
        await ctx.respond("Cog not found")
#    elif:
        
@bot.slash_command(name="unloadcog", description= "Unloads a cog of the users choosing", guild_id = id)
async def cogs(ctx, cogs):
    if cogs in cogs:
        bot.unload_extension(f'cogs.{cogs}')
        await ctx.respond(f"Successfully unloaded {cogs}")
    else:
        await ctx.respond("Cog not found")
#    elif:

@bot.slash_command(guild_id = id)
async def ping(ctx):
    await ctx.respond(f"Pong! ({bot.latency*1000}ms)")

@bot.slash_command(guild_id = id)
async def sync(ctx): 
    await bot.sync_commands()
    await ctx.respond(f"Succesfully synced commands")

# TESTING!!!

class MyView(discord.ui.View):
    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.primary, emoji="😎")
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked the button!")

@bot.slash_command(name="button", description= "Uses a button of the users choosing", guild_id = id)
async def button(ctx):
    await ctx.respond("This is a button!", view=MyView())

@discord.slash_command(name="gen2", description="Show the gen 2 menu", guild_id = id)
async def gen2(self, ctx):
    view = Gen2View()
    await ctx.respond('Choose an option:', view=view)

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

bot.run('')