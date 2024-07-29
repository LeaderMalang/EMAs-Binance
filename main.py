import pandas as pd
import numpy as np
from binance.client import Client
import asyncio
from dotenv import dotenv_values
config = dotenv_values(".env")

# Your Binance API Key and Secret
api_key = config['API_KEY']
api_secret = config['API_SECRET']

# Initialize the Binance client
client = Client(api_key, api_secret)

# Fetch historical price data
symbol = 'FTMUSDT'
interval = Client.KLINE_INTERVAL_1HOUR
klines = client.get_historical_klines(symbol, interval, "1 month ago UTC")

# Convert data into a DataFrame
data = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
data.set_index('timestamp', inplace=True)
data['close'] = data['close'].astype(float)

# Calculate EMAs
data['EMA_5'] = data['close'].ewm(span=5, adjust=False).mean()
data['EMA_12'] = data['close'].ewm(span=12, adjust=False).mean()

# Detect crossovers
data['previous_EMA_5'] = data['EMA_5'].shift(1)
data['previous_EMA_12'] = data['EMA_12'].shift(1)

# Cross above condition
data['cross_above'] = ((data['EMA_5'] > data['EMA_12']) & (data['previous_EMA_5'] <= data['previous_EMA_12']))

# Cross below condition
data['cross_below'] = ((data['EMA_5'] < data['EMA_12']) & (data['previous_EMA_5'] >= data['previous_EMA_12']))

# Initialize variables to track trades
global position 

buy_price = 0
trades = []

#get mini Qty for order
def get_mini_qty(symbol):
    info = client.get_symbol_info(symbol)
    print(info)
    quantity =info['filters'][1]['minQty']
    return quantity

quantity=get_mini_qty(symbol)



# Function to place a market buy order
def place_buy_order(symbol, quantity):
    try:
        order = client.order_market_buy(
            symbol=symbol,
            quantity=quantity
        )
        return order
    except Exception as e:
        print(f"An exception occurred - {e}")
        return None

# Function to place a market sell order
def place_sell_order(symbol, quantity):
    try:
        order = client.order_market_sell(
            symbol=symbol,
            quantity=quantity
        )
        return order
    except Exception as e:
        print(f"An exception occurred - {e}")
        return None
async def main():
    position =None
    # Implement buy/sell logic based on crossovers
    for index, row in data.iterrows():
        if row['cross_above'] and position != 'long':
            # Execute buy order
            # quantity = 0.001  # Example quantity, adjust as needed
            order = place_buy_order(symbol, quantity)
            if order:
                position = 'long'
                buy_price = row['close']
                trades.append({'action': 'buy', 'price': buy_price, 'timestamp': index, 'order_id': order['orderId']})
                print(f"Buy at {buy_price} on {index} - Order ID: {order['orderId']}")
        elif row['cross_below'] and position == 'long':
            # Execute sell order
            # quantity = 0.001  # Example quantity, adjust as needed
            order = place_sell_order(symbol, quantity)
            if order:
                position = 'short'
                sell_price = row['close']
                trades.append({'action': 'sell', 'price': sell_price, 'timestamp': index, 'order_id': order['orderId']})
                print(f"Sell at {sell_price} on {index} - Order ID: {order['orderId']}")

    # Print all trades
    print("Executed Trades:")
    for trade in trades:
        print(trade)

# Optional: Plot the data with crossover points and trades highlighted
# plt.figure(figsize=(12, 6))
# plt.plot(data['close'], label='Close Price', color='black')
# plt.plot(data['EMA_5'], label='5-period EMA', color='blue')
# plt.plot(data['EMA_12'], label='12-period EMA', color='red')
# buy_signals = data[data['cross_above']]
# sell_signals = data[data['cross_below']]
# plt.scatter(buy_signals.index, buy_signals['close'], marker='^', color='green', label='Buy Signal', s=100)
# plt.scatter(sell_signals.index, sell_signals['close'], marker='v', color='red', label='Sell Signal', s=100)
# plt.legend()
# plt.show()
while True:
    
    asyncio.run(main())