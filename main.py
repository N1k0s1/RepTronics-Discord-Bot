id = [1261831251254317066]
import discord
bot = discord.Bot()
    
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")



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

class MyView(discord.ui.View):
    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.primary, emoji="😎")
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked the button!")

@bot.slash_command(name="button", description= "Uses a button of the users choosing", guild_id = id)
async def button(ctx):
    await ctx.respond("This is a button!", view=MyView())

bot.run('')