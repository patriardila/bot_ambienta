import discord
from discord.ext import commands
import requests
intents= discord.Intents.default()
intents.message_content=True

bot=commands.Bot(command_prefix="/",intents=intents)
NASA_API_KEY = 'TNq1vVA0R6EtWgVcB19rrx2eZTdhjYQZaxaIOWgKM'
UNSPLASH_ACCESS_KEY = 'hECtvB3IM-czDaJuKV33zu7Anh-Wp5hBB4l7ifBflng'

@bot.event
async def on_reday():
    print(f"hemos iniciado sesion {bot.user}")

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

descomposicion={
    "botella":500,
    "lata":50,
    "bolsa":150,
    "vidrio":4000
}

@bot.command()
async def impacto(ctx,objeto):
    objeto=objeto.lower()
    if objeto in descomposicion:
        tiempo=descomposicion[objeto]
        await ctx.send(f"El objeto{objeto},dura aprox {tiempo} en descomponerse")
        if tiempo>=100:
            await ctx.send(f"S.O.S nos quedamos sin planeta")
    else: 
        await ctx.send("No registro ese objeto")

recycling_ideas = {
    "plástico": ["macetas para plantas", "joyería artesanal", "ladrillos ecológicos"],
    "papel": ["cuadernos reciclados", "decoraciones para el hogar", "papel maché"],
    "vidrio": ["lámparas decorativas", "jarrones", "ladrillos de vidrio"],
    "metal": ["macetas", "arte decorativo", "portavelas"],
    "cartón": ["organizadores de escritorio", "casitas para mascotas", "manualidades infantiles"],
}
@bot.command()
async def reciclar(ctx, elemento: str):
    elemento = elemento.lower()  # Convertir a minúsculas para evitar errores de entrada
    if elemento in recycling_ideas:
        objetos =recycling_ideas[elemento]
        await ctx.send(f"Con {elemento} puedes hacer: {objetos}.")
    else:
        await ctx.send("Lo siento, no tengo ideas de reciclaje para ese elemento.")
@bot.command()
async def contaminación(ctx):
    response = requests.get(f'https://api.nasa.gov/planetary/earth/assets?api_key={NASA_API_KEY}')
    if response.status_code == 200:
        data = response.json()
        await ctx.send(f"Aquí hay una imagen de la Tierra desde la NASA: {data['url']}")
    else:
        await ctx.send('No pude obtener la imagen. Por favor, intenta más tarde.')

@bot.command()
async def contam(ctx):
    query = "contaminación"
    url = f"https://api.unsplash.com/photos/random?query={query}&client_id={UNSPLASH_ACCESS_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        image_url = data['urls']['regular']
        await ctx.send(f"Aquí tienes una imagen sobre contaminación: {image_url}")
    else:
        await ctx.send('No pude obtener la imagen. Por favor, intenta más tarde.')

bot.run("")
