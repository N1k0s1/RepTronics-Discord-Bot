import discord
from embed import genembed
from embed import sellerembed

# Gen 2 Buttons/Embeds

class Gen2View(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='JL', custom_id='JL', style=discord.ButtonStyle.green)
    async def on_button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Gen 2 | JL", "gen2jl")
        await interaction.response.send_message(embed=embed1)

    @discord.ui.button(label='Airoha 1562U', custom_id='1562U', style=discord.ButtonStyle.green)
    async def on_button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Gen 2 | Airoha 1562U", "gen21562u")
        await interaction.response.send_message(embed=embed1)

    @discord.ui.button(label='Airoha 1562E', custom_id='1562E', style=discord.ButtonStyle.green)
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Gen 2 | Airoha 1562E", "gen21562e")
        await interaction.response.send_message(embed=embed1)

# Gen 3 Buttons/Embeds

class Gen3View(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='JL', custom_id='JL', style=discord.ButtonStyle.green)
    async def on_button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Gen 3 | JL", "gen3jl")
        await interaction.response.send_message(embed=embed1)

    @discord.ui.button(label='Airoha 1562U', custom_id='1562U', style=discord.ButtonStyle.green)
    async def on_button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Gen 3 | Airoha 1562U", "gen31562u")
        await interaction.response.send_message(embed=embed1)

    @discord.ui.button(label='Airoha 1562E', custom_id='1562E', style=discord.ButtonStyle.green)
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Gen 3 | Airoha 1562E", "gen31562e")
        await interaction.response.send_message(embed=embed1)

    @discord.ui.button(label='Huilian A10', custom_id='a10', style=discord.ButtonStyle.green)
    async def on_button4(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Gen 3 | Huilian A10", "gen3a10")
        await interaction.response.send_message(embed=embed1)

# Pro 1 Buttons/Embeds

class Pro1View(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='JL', custom_id='JL', style=discord.ButtonStyle.green)
    async def on_button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 1 | JL", "pro1jl")
        await interaction.response.send_message(embed=embed1)

    @discord.ui.button(label='Zhongke Lanxun', custom_id='zl', style=discord.ButtonStyle.green)
    async def on_button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 1 | Zhongke Lanxun", "pro1zl")
        await interaction.response.send_message(embed=embed1)

    @discord.ui.button(label='Airoha 1562F', custom_id='1562F', style=discord.ButtonStyle.green)
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 1 | Airoha 1562F", "pro11562f")
        await interaction.response.send_message(embed=embed1)

    @discord.ui.button(label='Airoha 1562A', custom_id='1562A', style=discord.ButtonStyle.green)
    async def on_button4(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 1 | Airoha 1562A", "pro11562a")
        await interaction.response.send_message(embed=embed1)

    @discord.ui.button(label='Airoha 1562AE', custom_id='1562AE', style=discord.ButtonStyle.green)
    async def on_button5(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 1 | Airoha 1562AE", "pro11562ae")
        await interaction.response.send_message(embed=embed1)

# Pro 2 Buttons/Embeds

class Pro2View(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='JL', custom_id='JL', style=discord.ButtonStyle.green)
    async def on_button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 2 | JL", "pro2jl")
        await interaction.response.send_message(embed=embed1)

    @discord.ui.button(label='Bluetrum', custom_id='pro2blueturm', style=discord.ButtonStyle.green)
    async def on_button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 2 | Bluetrum", "pro2blueturm")
        await interaction.response.send_message(embed=embed1)

    @discord.ui.button(label='Airoha 1562AE (HR)', custom_id='hr', style=discord.ButtonStyle.green)
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 2 | Airoha 1562AE (HR)", "pro21562aehr")
        await interaction.response.send_message(embed=embed1)

    @discord.ui.button(label='H2S', custom_id='h2s', style=discord.ButtonStyle.green)
    async def on_button4(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 2 | H2S", "pro2h2s")
        await interaction.response.send_message(embed=embed1)

    @discord.ui.button(label='H2S Pro', custom_id='h2spro', style=discord.ButtonStyle.green)
    async def on_button5(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 2 | H2S Pro", "pro2h2spro")
        await interaction.response.send_message(embed=embed1)

    @discord.ui.button(label='H2S Ultra', custom_id='h2sultra', style=discord.ButtonStyle.green)
    async def on_button6(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 2 | H2S Ultra", "pro2h2sultra")
        await interaction.response.send_message(embed=embed1)

    @discord.ui.button(label='Airoha 1562F', custom_id='1562F', style=discord.ButtonStyle.green)
    async def on_button7(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 2 | Airoha 1562F", "pro21562f")
        await interaction.response.send_message(embed=embed1)

    @discord.ui.button(label='Airoha 1562AE (TB)', custom_id='1562AE', style=discord.ButtonStyle.green)
    async def on_button8(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Pro 2 | Airoha 1562AE", "pro21562ae")
        await interaction.response.send_message(embed=embed1)

# Maxes - Plastic Buttons/Embeds
class MaxesView(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='Metal Maxes', custom_id='metalmaxes', style=discord.ButtonStyle.green)
    async def on_button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        metal_maxes_view = MetalMaxes()
        await interaction.response.send_message(view=metal_maxes_view)

    @discord.ui.button(label='Plastic Maxes', custom_id='plasticmaxes', style=discord.ButtonStyle.green)
    async def on_button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        plastic_maxes_view = PlasticMaxes()
        await interaction.response.send_message(view=plastic_maxes_view)

class PlasticMaxes(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='JL', custom_id='JL', style=discord.ButtonStyle.green)
    async def on_button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Maxes (Plastic) | JL", "maxesjlplastic")
        await interaction.response.send_message(embed=embed1)

    @discord.ui.button(label='Zhongke Lanxun', custom_id='zl', style=discord.ButtonStyle.green)
    async def on_button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Maxes (Available in both Plastic & Aluminium Sprayed) | Zhongke Lanxun", "maxeszlplastic")
        await interaction.response.send_message(embed=embed1)

    @discord.ui.button(label='Qualcommm', custom_id='qualcomm', style=discord.ButtonStyle.green)
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Maxes (Available in both Plastic & Aluminium Sprayed) | Qualcomm", "maxesqualcommplastic")
        await interaction.response.send_message(embed=embed1)

    @discord.ui.button(label='Airoha 1561M', custom_id='1561m', style=discord.ButtonStyle.green)
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Maxes (Available in both Plastic & Aluminium Sprayed) | Airoha 1561M", "maxes1561mplastic")
        await interaction.response.send_message(embed=embed1)

class MetalMaxes(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='Zhongke Lanxun', custom_id='zl', style=discord.ButtonStyle.green)
    async def on_button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Maxes | Zhongke Lanxun", "maxeszl")
        await interaction.response.send_message(embed=embed1)

    @discord.ui.button(label='Qualcommm', custom_id='qualcomm', style=discord.ButtonStyle.green)
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Maxes | Qualcomm", "maxesqualcomm")
        await interaction.response.send_message(embed=embed1)

    @discord.ui.button(label='Airoha 1561M', custom_id='1561m', style=discord.ButtonStyle.green)
    async def on_button4(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Maxes | Airoha 1561M", "maxes1561m")
        await interaction.response.send_message(embed=embed1)
    
    @discord.ui.button(label='Realtek 8763ESE', custom_id='rt', style=discord.ButtonStyle.green)
    async def on_button5(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Maxes | Realtek 8763ESE", "maxesrt")
        await interaction.response.send_message(embed=embed1)

# SELLERS
class SellersView(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='JDFoot', custom_id='JDFoot', style=discord.ButtonStyle.green)
    async def on_button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = sellerembed("JDFoot", "JDFoot")        
        await interaction.response.send_message(embed=embed)

    @discord.ui.button(label='HiCity', custom_id='hicity', style=discord.ButtonStyle.green)
    async def on_button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = sellerembed("HiCity", "HiCity")
        await interaction.response.send_message(embed=embed)

    @discord.ui.button(label='Jenny', custom_id='Jenny', style=discord.ButtonStyle.green)
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = sellerembed("Jenny", "Jenny")
        await interaction.response.send_message(embed=embed)

    @discord.ui.button(label='Mike-YM', custom_id='Mike-YM', style=discord.ButtonStyle.green)
    async def on_button5(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = sellerembed("Mike-YM", "Mike-YM")
        await interaction.response.send_message(embed=embed)

    @discord.ui.button(label='York', custom_id='York', style=discord.ButtonStyle.green)
    async def on_button7(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = sellerembed("York", "York")
        await interaction.response.send_message(embed=embed)

    @discord.ui.button(label='Criss', custom_id='Criss', style=discord.ButtonStyle.green)
    async def on_button8(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = sellerembed("Criss", "Criss")
        await interaction.response.send_message(embed=embed)

    @discord.ui.button(label='Sam', custom_id='Sam', style=discord.ButtonStyle.green)
    async def on_button9(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = sellerembed("Sam", "Sam")
        await interaction.response.send_message(embed=embed)

    @discord.ui.button(label='BXM/Sunfler', custom_id='BXM/Sunfler', style=discord.ButtonStyle.green)
    async def on_button10(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = sellerembed("BXM/Sunfler", "BXM/Sunfler")
        await interaction.response.send_message(embed=embed)
