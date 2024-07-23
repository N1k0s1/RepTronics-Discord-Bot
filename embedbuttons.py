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

    @discord.ui.button(label='Bluetrum', custom_id='bl')
    async def on_button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 2 | Bluetrum", "pro2bluetrum")
        await interaction.response.send_message('bl', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Airoha 1562AE (HR)', custom_id='hr')
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 2 | BES", "pro21562aeh")
        await interaction.response.send_message('hr', embed=embed1, ephemeral=True)

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

    @discord.ui.button(label='Airoha 1562AE (TB)', custom_id='1562AE')
    async def on_button8(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 2 | Airoha 1562AE", "pro21562ae")
        await interaction.response.send_message('1562AE', embed=embed1, ephemeral=True)

# Maxes - Plastic Buttons/Embeds
class MaxesView(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='Metal Maxes', custom_id='metalmaxes')
    async def on_button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        metal_maxes_view = MetalMaxes()
        await interaction.response.send_message('Metal Maxes', view=metal_maxes_view, ephemeral=True)

    @discord.ui.button(label='Plastic Maxes', custom_id='plasticmaxes')
    async def on_button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        plastic_maxes_view = PlasticMaxes()
        await interaction.response.send_message('Plastic Maxes', view=plastic_maxes_view, ephemeral=True)

    @discord.ui.button(label='Aluminium Sprayed Maxes', custom_id='aluminiummaxes')
    async def on_button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        aluminium_maxes_view = AluminiumMaxes()
        await interaction.response.send_message('Aluminium Sprayed Maxes', view=aluminium_maxes_view, ephemeral=True)    


class PlasticMaxes(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='JL', custom_id='JL')
    async def on_button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Maxes (Plastic) | JL", "maxesjl")
        await interaction.response.send_message('JL', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Zhongke Lanxun', custom_id='zl')
    async def on_button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Maxes (Avalible in both Plastic & Aluminium Sprayed) | Zhongke Lanxun", "pro2zl")
        await interaction.response.send_message('zl', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Qualcommm', custom_id='qualcomm')
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Maxes (Avalible in both Plastic & Aluminium Sprayed| Qualcomm", "maxesqualcomm")
        await interaction.response.send_message('qualcomm', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Airoha 1561M', custom_id='1561m')
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Maxes (Avalible in both Plastic & Aluminium Sprayed | Airoha 1561M", "maxes1561m")
        await interaction.response.send_message('1561m', embed=embed1, ephemeral=True)

class MetalMaxes(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='JL', custom_id='JL')
    async def on_button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Maxes (Plastic) | JL", "maxesjl")
        await interaction.response.send_message('JL', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Zhongke Lanxun', custom_id='zl')
    async def on_button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Maxes (Avalible in both Plastic & Aluminium Sprayed) | Zhongke Lanxun", "pro2zl")
        await interaction.response.send_message('zl', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Qualcommm', custom_id='qualcomm')
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Maxes (Avalible in both Plastic & Aluminium Sprayed| Qualcomm", "maxesqualcomm")
        await interaction.response.send_message('qualcomm', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Airoha 1561M', custom_id='1561m')
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Maxes (Avalible in both Plastic & Aluminium Sprayed | Airoha 1561M", "maxes1561m")
        await interaction.response.send_message('1561m', embed=embed1, ephemeral=True)

class AluminiumMaxes(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='Zhongke Lanxun', custom_id='zl')
    async def on_button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Maxes (Avalible in both Plastic & Aluminium Sprayed) | Zhongke Lanxun", "pro2zl")
        await interaction.response.send_message('zl', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Qualcommm', custom_id='qualcomm')
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Maxes (Avalible in both Plastic & Aluminium Sprayed| Qualcomm", "maxesqualcomm")
        await interaction.response.send_message('qualcomm', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Airoha 1561M', custom_id='1561m')
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Maxes (Avalible in both Plastic & Aluminium Sprayed | Airoha 1561M", "maxes1561m")
        await interaction.response.send_message('1561m', embed=embed1, ephemeral=True)