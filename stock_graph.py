import yfinance as yf
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import requests

def GraphPlotInfo(ticker:str,save_path:str = "graph.png"):
    data = yf.Ticker(ticker)
    historical_data = data.history(period="1y")
    
    # Convert historical data to DataFrame and drop unnecessary columns
    df = pd.DataFrame(historical_data)
    #df = df.drop(columns=["Dividends", "Stock Splits", "Capital Gains", "Volume"])
    
    # Ensure the DataFrame index is in datetime format
    df.index = pd.to_datetime(df.index)
    
    # Reset index to use it as a column for plotting
    df_reset = df.reset_index()
    df_reset.rename(columns={'Date': 'Date'}, inplace=True)
    
    # Set up the Seaborn style
    sb.set(style="whitegrid")

    # Plot 'Open' and 'Close' prices
    plt.figure(figsize=(14, 6))
    sb.lineplot(data=df_reset, x='Date', y='Open', label='Open Price', color='blue', marker='o')
    sb.lineplot(data=df_reset, x='Date', y='Close', label='Close Price', color='red', marker='o')

    # Customize the plot
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'{ticker} Open and Close Prices Over Time')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Find the lowest and highest prices for 'Open' and 'Close'
    min_open = df_reset['Open'].idxmin()
    max_open = df_reset['Open'].idxmax()
    min_close = df_reset['Close'].idxmin()
    max_close = df_reset['Close'].idxmax()
    
    min_open_price = df_reset.loc[min_open, 'Open']
    max_open_price = df_reset.loc[max_open, 'Open']
    min_close_price = df_reset.loc[min_close, 'Close']
    max_close_price = df_reset.loc[max_close, 'Close']
    
    plt.scatter(df_reset.loc[min_open, 'Date'], min_open_price, color='blue', edgecolor='black', s=100, zorder=5, label='Lowest Open Price')
    plt.scatter(df_reset.loc[max_open, 'Date'], max_open_price, color='blue', edgecolor='black', s=100, zorder=5, label='Highest Open Price')
    plt.scatter(df_reset.loc[min_close, 'Date'], min_close_price, color='red', edgecolor='black', s=100, zorder=5, label='Lowest Close Price')
    plt.scatter(df_reset.loc[max_close, 'Date'], max_close_price, color='red', edgecolor='black', s=100, zorder=5, label='Highest Close Price')

    # Save plot
    plt.savefig(save_path)
    plt.close
    return save_path