import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(file_name)
            await ctx.send('Guardado')
            try:
                class_name = get_class('keras_model.h5','labels.txt',file_name)
                await ctx.send(class_name)
                if class_name[0]== "Carros":
                    await ctx.send('Esto es un carro, los carros son vehiculos que pueden transportar entre 1 y 5 personas, poseen 4 llantas y incluyen sistemas de seguridad como cinturones o frenos.')
                elif class_name[0]== "Buses":
                    await  ctx.send("Esto es un bus, los buses son vehiculos que pueden transportar muchas personas al mismo tiempo, son mas grandes que los carros o motos y generalmente tienen 6 ruedas .")
                elif class_name[0]== "Motos":
                    await  ctx.send("Esto es una moto, las motos son vehiculos que pueden transportar 1 o 2 personas, tienen 2 ruedas y son agiles y faciles de maniobrar.")    
            except:
                await ctx.send('La clasificacion ha fallado')  
bot.run("")
