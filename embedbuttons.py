import discord
from embed import genembed
from embed import sellerembed

# Gen 2 Buttons/Embeds

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
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Gen 2 | Airoha 1562E", "gen21562e")
        await interaction.response.send_message('1562E', embed=embed1, ephemeral=True)

# Gen 3 Buttons/Embeds

class Gen3View(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='JL', custom_id='JL')
    async def on_button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Gen 3 | JL", "gen3jl")
        await interaction.response.send_message('JL', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Airoha 1562U', custom_id='1562U')
    async def on_button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Gen 3 | Airoha 1562U", "gen31562u")
        await interaction.response.send_message('1562U', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Airoha 1562E', custom_id='1562E')
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Gen 3 | Airoha 1562E", "gen31562e")
        await interaction.response.send_message('1562E', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Huilian A10', custom_id='a10')
    async def on_button4(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Gen 3 | Huilian A10", "gen3a10")
        await interaction.response.send_message('a10', embed=embed1, ephemeral=True)

# Pro 1 Buttons/Embeds

class Pro1View(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='JL', custom_id='JL')
    async def on_button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 1 | JL", "pro1jl")
        await interaction.response.send_message('JL', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Zhongke Lanxun', custom_id='zl')
    async def on_button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 1 | Zhongke Lanxun", "pro1zl")
        await interaction.response.send_message('zl', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Airoha 1562F', custom_id='1562F')
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 1 | Airoha 1562F", "pro11562f")
        await interaction.response.send_message('1562F', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Airoha 1562A', custom_id='1562A')
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 1 | Airoha 1562A", "pro11562a")
        await interaction.response.send_message('1562A', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Airoha 1562AE', custom_id='1562AE')
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 1 | Airoha 1562AE", "pro11562ae")
        await interaction.response.send_message('1562AE', embed=embed1, ephemeral=True)

# Pro 2 Buttons/Embeds

class Pro2View(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='JL', custom_id='JL')
    async def on_button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 2 | JL", "pro2jl")
        await interaction.response.send_message('JL', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Zhongke Lanxun', custom_id='zl')
    async def on_button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 2 | Zhongke Lanxun", "pro2zl")
        await interaction.response.send_message('zl', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Airoha 1562F', custom_id='1562F')
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 2 | Airoha 1562F", "pro21562f")
        await interaction.response.send_message('1562F', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Airoha 1562AE', custom_id='1562AE')
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 2 | Airoha 1562AE", "pro21562ae")
        await interaction.response.send_message('1562AE', embed=embed1, ephemeral=True)