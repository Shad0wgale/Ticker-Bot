import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import requests
import asyncio
from stock_graph import GraphPlotInfo

load_dotenv()

# Initialize the bot
intents = discord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)

#grab token

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


@bot.command(name='stock')
async def stock(ctx):
    await ctx.send("Please enter the stock ticker symbol (e.g., AAPL, TSLA):")

    # Define a check to ensure the bot listens for the next message from the same user
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    # Wait for the user to respond with the ticker symbol
    try:
        msg = await bot.wait_for('message', check=check, timeout=30)  # Timeout of 30 seconds
    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond! Please try again.")
        return

    ticker = msg.content.upper()  # Get the ticker and convert it to uppercase

    # Inform the user that the bot is generating the graph
    await ctx.send(f"Generating graph for {ticker}...")

    # Use the GraphPlotInfo function to generate the graph
    image_path = f"{ticker}_plot.png"
    GraphPlotInfo(ticker, image_path)  # Call the graph function

    # Send the generated image to the Discord channel
    if os.path.exists(image_path):
        await ctx.send(file=discord.File(image_path))
        os.remove(image_path)  # Clean up and remove the file after sending it
    else:
        await ctx.send(f"Failed to generate the graph for {ticker}. Please try again.")

# Run the bot with the token
bot.run(DISCORD_TOKEN)