import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import requests
import json

client = commands.Bot(command_prefix='.') #PREFIS TO CALL BOT
URL_API = 'https://pokeapi.co/api/v2/pokemon/' #API URL

@client.event
async def on_ready():
    print("Bot On!")
    #PRINT IF BOT IS ONLINE

@client.command()
async def pokemon(ctx, *, args):
  
    pokeName = args.lower()
    try:
        r = requests.get(f'{URL_API}{pokeName}')
        packages_json = r.json()
        packages_json.keys()

        embed = discord.Embed(title="Pokemon", color=0xff0000)
        embed.add_field(name="Name", value=packages_json['name'], inline=True)
        embed.add_field(name="Pokedex Order", value=packages_json['order'], inline=True)
        #embed.set_thumbnail(url=packages_json['sprites']['back_default']) PICTURE FROM POKEAPI
        #embed.set_thumbnail(url=packages_json['sprites']['versions']['generation-v']['black-white']['animated']['front_default']) GIF FROM POKEAPI
        embed.set_thumbnail(url= f'https://play.pokemonshowdown.com/sprites/ani/{pokeName}.gif')
        embed.add_field(name="Peso", value=packages_json['weight'], inline=True)
        embed.add_field(name="Altura", value=packages_json['height'], inline=True)
        embed.add_field(name="XP Base", value=packages_json['base_experience'], inline=True)
        for type in packages_json['types']: #FOR TO GET A TYPE OF A POKEMON
            embed.add_field(name="Types", value= type['type']['name'], inline=True)
        embed.set_footer(text="Pokemon Bot - Python ")
        await ctx.send(embed=embed)
    except:
        await ctx.send("Pokemon not found!")

                                        
client.run('YOUR BOT TOKEN') #RUN BOT
