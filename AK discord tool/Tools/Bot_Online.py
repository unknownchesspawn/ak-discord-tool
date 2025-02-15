import discord
from discord.ext import commands

ascii_art = r"""
            ____        __     ____        ___          
           / __ )____  / /_   / __ \____  / (_)___  ___ 
          / __  / __ \/ __/  / / / / __ \/ / / __ \/ _ \
         / /_/ / /_/ / /_   / /_/ / / / / / / / / /  __/
        /_____/\____/\__/   \____/_/ /_/_/_/_/ /_/\___/ 
                                               
"""

print(ascii_art)


token = input("Enter your Discord bot token: ").strip()

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="", intents=intents, self_bot=True)

@bot.event
async def on_ready():
    print(f"{bot.user.display_name} is online!")
    input("Press Enter to exit...") 
    exit()

try:
    bot.run(token)
except discord.LoginFailure:
    print("Invalid token provided. Please check and try again.")
    input("Press Enter to exit...")
