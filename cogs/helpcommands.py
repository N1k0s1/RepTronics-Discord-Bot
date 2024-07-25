id = [1261831251254317066]

import discord
from discord.ext import commands
from embedbuttons import SellersView
from embed import sellerembed

class HelpCommands(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot


    @discord.slash_command(name="hicity", description="Information about HiCity", guild_id = id)
    async def sam(self, ctx):
        embed1 = sellerembed("Sam", "sam")
        await ctx.respond(embed=embed1)

'''    @discord.slash_command(name="hicity", description="Information about HiCity", guild_id = id)
    async def hicityinfo(self, ctx):
        embed = discord.Embed(title="HiCity", color=discord.Color.blue())
        seller = data['sellers']['HiCity']

        embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
        embed.add_field(name="Discord", value=seller['discord'], inline=False)
        embed.add_field(name="Website", value=seller['store_link'], inline=False)

        await ctx.respond(embed=embed)

    @discord.slash_command(name="dyson", description="Information about Dyson", guild_id = id)
    async def dysoninfo(self, ctx):
        embed = discord.Embed(title="Dyson", color=discord.Color.blue())
        seller = data['sellers']['Dyson']

        embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
        embed.add_field(name="Discord", value=seller['discord'], inline=False)
        embed.add_field(name="Website", value=seller['store_link'], inline=False)

        await ctx.respond(embed=embed)

    @discord.slash_command(name="jenny", description="Information about Jenny", guild_id = id)
    async def jennyinfo(self, ctx):
        embed = discord.Embed(title="Jenny", color=discord.Color.blue())
        seller = data['sellers']['Jenny']

        embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
        embed.add_field(name="Discord", value=seller['discord'], inline=False)
        embed.add_field(name="Website", value=seller['store_link'], inline=False)

        await ctx.respond(embed=embed)

    @discord.slash_command(name="beschan", description="Information about Beschan", guild_id = id)
    async def beschaninfo(self, ctx):
        embed = discord.Embed(title="Beschan", color=discord.Color.blue())
        seller = data['sellers']['Beschan']

        embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
        embed.add_field(name="Discord", value=seller['discord'], inline=False)
        embed.add_field(name="Website", value=seller['store_link'], inline=False)

        await ctx.respond(embed=embed)

    @discord.slash_command(name="mikeym", description="Information about Mike-YM", guild_id = id)
    async def mikeyminfo(self, ctx):
        embed = discord.Embed(title="Mike-YM", color=discord.Color.blue())
        seller = data['sellers']['Mike-YM']

        embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
        embed.add_field(name="Discord", value=seller['discord'], inline=False)
        embed.add_field(name="Website", value=seller['store_link'], inline=False)

        await ctx.respond(embed=embed)

    @discord.slash_command(name="jdfoot", description="Information for JD-Foot", guild_id = id)
    async def jdfootinfo(self, ctx):
        embed = discord.Embed(title="JD-Foot", color=discord.Color.blue())
        seller = data['sellers']['JdFoot']

        embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
        embed.add_field(name="Discord", value=seller['discord'], inline=False)
        embed.add_field(name="Website", value=seller['store_link'], inline=False)

        await ctx.respond(embed=embed)

    @discord.slash_command(name="bxm", description="Information for BXM", guild_id = id)
    async def bxminfo(self, ctx):
        embed = discord.Embed(title="BXM", color=discord.Color.blue())
        seller = data['sellers']['BXM']

        embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
        embed.add_field(name="Discord", value=seller['discord'], inline=False)
        embed.add_field(name="Website", value=seller['store_link'], inline=False)

    @discord.slash_command(name="york", description="Information for York", guild_id = id)
    async def bxminfo(self, ctx):
        embed = discord.Embed(title="BXM", color=discord.Color.blue())
        seller = data['sellers']['BXM']

        embed.add_field(name="WhatsApp", value=seller['whatsapp'], inline=False)
        embed.add_field(name="Discord", value=seller['discord'], inline=False)
        embed.add_field(name="Website", value=seller['store_link'], inline=False)
        await ctx.respond(embed=embed)'''
        
def setup(bot):
    bot.add_cog(HelpCommands(bot))
