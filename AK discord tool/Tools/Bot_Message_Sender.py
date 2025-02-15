import discord
from discord.ext import commands

ascii_art = r"""

            ____        __     __  ___                                   _____                __             
           / __ )____  / /_   /  |/  /__  ______________ _____ ____     / ___/___  ____  ____/ /__  _____    
          / __  / __ \/ __/  / /|_/ / _ \/ ___/ ___/ __ `/ __ `/ _ \    \__ \/ _ \/ __ \/ __  / _ \/ ___/    
         / /_/ / /_/ / /_   / /  / /  __(__  |__  ) /_/ / /_/ /  __/   ___/ /  __/ / / / /_/ /  __/ /        
        /_____/\____/\__/  /_/  /_/\___/____/____/\__,_/\__, /\___/   /____/\___/_/ /_/\__,_/\___/_/
                                                       /____/
                                                       
"""

print(ascii_art)

token = input("Enter your Discord bot token: ").strip()
message_to_send = input("Enter the message you want to send: ").strip()

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="", intents=intents, self_bot=True)

@bot.event
async def on_ready():
    print(f"{bot.user.display_name} is online!")
    channel_id = input("Enter the channel ID where you want to send the message: ").strip()

    try:
        channel = bot.get_channel(int(channel_id))
        if not channel:
            print("Invalid channel ID or the bot doesn't have access to the channel.")
        else:
            print(f"Sending message '{message_to_send}'")
            for _ in range(repeat_count):
                await channel.send(message_to_send)
            print("Messages sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

    input("Press Enter to exit...")
    await bot.close()

try:
    bot.run(token)
except discord.LoginFailure:
    print("Invalid token provided. Please check and try again.")
    input("Press Enter to exit...")
