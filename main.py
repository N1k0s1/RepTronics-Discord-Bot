id = 718418845194256404
allowed_users = [1136290556591485039, 978886408964026378]
allowed_channel_id = 1263491691638292521
import discord
from discord.ext import commands
import os
bot = commands.Bot()
import asyncio
from embed import create_survey_embed
from embedbuttons import Gen2View, Gen3View, Pro1View, Pro2View, MaxesView, SellersView
from discord.ext import tasks
import json 
# BOT TOKEN
from dotenv import load_dotenv
load_dotenv("token.env")
bot_token = os.getenv("DISCORD_BOT_TOKEN")

apringle = 978886408964026378

with open('data.json') as f:
    data = json.load(f)

@tasks.loop(seconds=20)
async def status_task() -> None:
    guild = bot.get_guild(id)
    if guild:
        member_count = guild.member_count
        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{member_count} members!"))
        await asyncio.sleep(20)
        await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name="Ultimate Guide", url="https://weare.reptronics.top/blog/"))
    else:
        print("Guild not found")

@bot.event
async def on_ready():
    status_task.start()
    print(f"We have logged in as {bot.user}")
#    await bot.sync_commands()
    print(f"Succesfully synced commands")
    try:
        user = await bot.fetch_user(apringle)
        if user:
            embed = discord.Embed(title="Bot Status", description="The RepTronics discord bot is currently online!!", color=discord.Color.green())
            embed.set_footer(text="Bot created by apringle", icon_url="https://styles.redditmedia.com/t5_38xyy/styles/communityIcon_mk1i0se5yboa1.png")
            await user.send(embed=embed)        
        else:
            print("User not found")
    except Exception as e:
        print(f"Error fetching user: {e}")


@bot.slash_command(name="loadcog", description="Loads a cog of the user's choosing", guild_id=id)
async def loadcog(ctx, *, cog: str):
    if ctx.author.id in allowed_users:
        try:
            bot.load_extension(f"cogs.{cog}")
            await ctx.send(f"Successfully loaded cog: {cog}")
        except commands.ExtensionNotFound:
            await ctx.send("Cog not found")
        except Exception as e:
            await ctx.send(f"Error while loading cog: {cog}\n{e}")
    else:
        await ctx.send("You do not have permission to use this command.", ephemeral=True)
        
@bot.slash_command(name='unloadcog', description= "Unloads a cog of the users choosing", guild_id = id)
async def unload(ctx, *, cog: str):
    if ctx.author.id in allowed_users:
        try:
            bot.unload_extension(f"cogs.{cog}")
            await ctx.send(f"Unloaded cog: {cog}")
        except commands.ExtensionNotFound:
            await ctx.send("Cog not found")
        except Exception as e:
            await ctx.send(f"Error while unloading cog: {cog}\n{e}")
    else:
        await ctx.send("You do not have permission to use this command.", ephemeral=True)

@bot.slash_command(name="quiz", description="Sends link to quiz", guild_id=id)
async def quiz(ctx):
    if ctx.channel.id == allowed_channel_id or ctx.author.guild_permissions.administrator:
        embed = discord.Embed(title="AirPod Quizzes", description="Click [here](https://weare.reptronics.top/category/quiz/) to take the quiz!", color=discord.Color.green())
        embed.set_footer(text="Bot created by apringle", icon_url="https://styles.redditmedia.com/t5_38xyy/styles/communityIcon_mk1i0se5yboa1.png")
        await ctx.respond(embed=embed)
    else:
        await ctx.respond("This command can only be used in a specific channel.", ephemeral=True)

@bot.slash_command(guild_id = id)
async def ping(ctx):
    embed = discord.Embed(title="Pong!", description=f"Latency: {bot.latency*1000}ms", color=discord.Color.green())
    embed.set_footer(text="Bot created by apringle", icon_url="https://styles.redditmedia.com/t5_38xyy/styles/communityIcon_mk1i0se5yboa1.png")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_id = id)
async def sync(ctx):
    if ctx.author.id in allowed_users:
        await bot.sync_commands()
        await ctx.respond("Successfully synced commands")
    else:
        await ctx.respond("This command can only be used in a specific channel.", ephemeral=True)

# COMMANDS FOR THE CHIP MENU

@bot.slash_command(name="gen2", description="Show the gen 2 menu", guild_id = id)
async def gen2(ctx):
    if ctx.channel.id == allowed_channel_id or ctx.author.guild_permissions.administrator:
        await ctx.respond('Gen 2 chips - Choose an option:', view=Gen2View())
    else:
        await ctx.respond("This command can only be used in a specific channel.", ephemeral=True)
    
@bot.slash_command(name="gen3", description="Show the gen 3 menu", guild_id = id)
async def gen3(ctx):
    if ctx.channel.id == allowed_channel_id or ctx.author.guild_permissions.administrator:
        await ctx.respond('Gen 3 chips - Choose an option:', view=Gen3View())
    else:
        await ctx.respond("This command can only be used in a specific channel.", ephemeral=True)
    
@bot.slash_command(name="pro1", description="Show the pro 1 menu", guild_id = id)
async def pro1(ctx):
    if ctx.channel.id == allowed_channel_id or ctx.author.guild_permissions.administrator:
        await ctx.respond('Pro 1 chips - Choose an option:', view=Pro1View())
    else:
        await ctx.respond("This command can only be used in a specific channel.", ephemeral=True)
    
@bot.slash_command(name="pro2", description="Show the pro 2 menu", guild_id = id)
async def pro2(ctx):
    if ctx.channel.id == allowed_channel_id or ctx.author.guild_permissions.administrator:
        await ctx.respond('Pro 2 chips - Choose an option:', view=Pro2View())
    else:
        await ctx.respond("This command can only be used in a specific channel.", ephemeral=True)
    
@bot.slash_command(name="maxes", description="Show the maxes menu", guild_id = id)
async def maxes(ctx):
    if ctx.channel.id == allowed_channel_id or ctx.author.guild_permissions.administrator:
        await ctx.respond('Maxes Models - Choose an option:', view=MaxesView())
    else:
        await ctx.respond("This command can only be used in a specific channel.", ephemeral=True)
    
# COMMAND FOR SELLERS
@bot.slash_command(name="sellers", description="Information about sellers", guild_id = id)
async def sellers(ctx):
    if ctx.channel.id == allowed_channel_id or ctx.author.guild_permissions.administrator:
        await ctx.respond('Sellers: Choose an option.', view=SellersView())
    else:
        await ctx.respond("This command can only be used in a specific channel.", ephemeral=True)
    
@bot.slash_command(name='ts', description='Sends the user a survey', guild_id=id)
async def send_survey(ctx, user: discord.Member):
    if ctx.author.id in allowed_users:
        survey_data = data['misc']['survey_message']
        embed = create_survey_embed(user, survey_data)
        await user.send(embed=embed)
        embed1 = discord.Embed(title="Ticket Survey", description=f"Ticket Survey sent to {user.display_name}.", color=discord.Color.green())
        await ctx.respond(embed=embed1)
    else:
        await ctx.respond("You do not have permission to use this command.", ephemeral=True)

# @bot.slash_command(name="modmail" description="Sends a message to the modmail channel", guild_id=id)
#

bot.run(bot_token)