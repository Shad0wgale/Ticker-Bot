import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import requests

load_dotenv()

# Initialize the bot
intents = discord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)

#grab token

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


# Command to get currency exchange rates from poe.ninja. !currencysoftcore
@bot.command()
async def currencysoftcore(ctx):
    url = 'https://poe.ninja/api/data/currencyoverview?league=Necropolis&type=Currency'    
    # Extract relevant data from the response
    response = requests.get('https://poe.ninja/api/data/currencyoverview?league=Ancestor&type=Currency')
    dict = response.json()
    currencies = dict['lines']
    
    data = [0] * len(currencies)
    for x in range(len(currencies)):
        data[x] = (currencies[x])
    
    
    #ASK FOR WHICH CURRENCY
    await ctx.send("Please enter a currency, ex: Awakener's Orb")
    
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel
    try:
        msg = await bot.wait_for('message', timeout=30, check=check)  # Wait for user's response for 30 seconds
        input_string = msg.content
    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond.")
    
    for item in data:
        if 'currencyTypeName' in item and item['currencyTypeName'] in input_string:
            await ctx.send(item['currencyTypeName'] +" is currently "+ str(item['chaosEquivalent'])+" chaos")
    
    

    # Format the data into a readable message
    
    #await ctx.send("Currency exchange rates:\n" + "insert info here")

# Run the bot
bot.run(DISCORD_TOKEN)