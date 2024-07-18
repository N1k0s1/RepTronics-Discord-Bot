import discord
from embed import genembed
from embed import sellerembed

class Gen2View(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='JL', custom_id='JL')
    async def on_button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Gen 2 | JL", "gen2jl")
        await interaction.response.send_message('JL', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Airoha 1562U', custom_id='1562U')
    async def on_button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Gen 2 | Airoha 1562U", "gen21562u")
        await interaction.response.send_message('1562U', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Airoha 1562E', custom_id='1562E')
    async def on_button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Gen 2 | Airoha 1562E", "gen21562e")
        await interaction.response.send_message('1562E', embed=embed1, ephemeral=True)