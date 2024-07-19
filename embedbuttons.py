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
    async def on_button4(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 1 | Airoha 1562A", "pro11562a")
        await interaction.response.send_message('1562A', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Airoha 1562AE', custom_id='1562AE')
    async def on_button5(self, button: discord.ui.Button, interaction: discord.Interaction):
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

    @discord.ui.button(label='BES', custom_id='bes')
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 2 | BES", "pro2bes")
        await interaction.response.send_message('bes', embed=embed1, ephemeral=True)

    @discord.ui.button(label='HS2', custom_id='hs2')
    async def on_button4(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 2 | HS2", "pro2hs2")
        await interaction.response.send_message('hs2', embed=embed1, ephemeral=True)

    @discord.ui.button(label='HS2 Pro', custom_id='hs2pro')
    async def on_button5(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 2 | HS2 Pro", "pro2hs2pro")
        await interaction.response.send_message('hs2pro', embed=embed1, ephemeral=True)

    @discord.ui.button(label='HS2 Ultra', custom_id='hs2ultra')
    async def on_button6(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 2 | HS2 Ultra", "pro2hs2ultra")
        await interaction.response.send_message('hs2ultra', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Airoha 1562F', custom_id='1562F')
    async def on_button7(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 2 | Airoha 1562F", "pro21562f")
        await interaction.response.send_message('1562F', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Airoha 1562AE', custom_id='1562AE')
    async def on_button8(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 2 | Airoha 1562AE", "pro21562ae")
        await interaction.response.send_message('1562AE', embed=embed1, ephemeral=True)

# Maxes - Plastic Buttons/Embeds

class MaxesView(discord.ui.View):
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