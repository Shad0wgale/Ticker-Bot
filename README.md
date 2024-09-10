# Discord Stock Graph Bot

This Discord bot allows you to generate and share stock price graphs directly in your Discord channel. Simply use the `!stock` command to request a graph for any stock ticker symbol, and the bot will generate and send the graph back to the channel.
![image](https://github.com/user-attachments/assets/4ceb99ae-77da-4769-8ec4-9875fda4c93e)

## Features

- **Interactive Commands**: Request stock graphs using the `!stock` command.
- **Graph Generation**: Automatically generates graphs for stock price data.
- **Dynamic Responses**: The bot responds with the graph and handles user input.

## Requirements

- **Python 3.8+**
- **`discord.py`**: For interacting with the Discord API.
- **`yfinance`**: For fetching stock data.
- **`pandas`**: For data manipulation.
- **`matplotlib`**: For plotting graphs.
- **`seaborn`**: For enhancing graph visuals.
- **`python-dotenv`**: For managing environment variables.

## Setup

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/discord-stock-graph-bot.git
cd discord-stock-graph-bot
```

### 2. Clone the Repository

```bash
pip install discord.py yfinance pandas matplotlib seaborn python-dotenv
```

### 3. Clone the Repository

```bash
DISCORD_TOKEN=your_discord_bot_token_here
```

### 4. Add Bot Token
Make sure to replace your_discord_bot_token_here in the .env file with the token you received from the Discord Developer Portal.
https://discord.com/developers/applications
### 5. Run the Bot

```bash
python bot.py
```

## Usage
Invite the Bot: Make sure the bot is invited to your Discord server with the appropriate permissions.
Command: In any channel where the bot has access, type !stock followed by the stock ticker symbol (e.g., !stock AAPL).
Receive Graph: The bot will respond with a graph of the stock's open and close prices for the past year.
## Troubleshooting
Bot Not Responding: Ensure that the bot has the correct permissions and is running properly.
Invalid Token: Double-check your .env file and make sure the token is correct.
