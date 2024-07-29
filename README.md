#  Two Exponential Moving Averages 

This trading strategy for Binance is based on the crossover of two Exponential Moving Averages (EMAs) to identify buy and sell signals. Here’s a detailed explanation:

## Buy Signal:
``` Condition: The 5-period EMA crosses above the 12-period EMA.
Explanation: The EMA (Exponential Moving Average) is a type of moving average that places a greater weight and significance on the most recent data points. A 5-period EMA is calculated based on the past 5 periods (e.g., 5 minutes, hours, days, depending on the chosen timeframe), while a 12-period EMA is based on the past 12 periods.
Logic: When the 5-period EMA crosses above the 12-period EMA, it indicates a potential upward trend. This crossover suggests that recent prices are rising faster than they were in the more extended period, signaling a possible buying opportunity. ```
## Sell Signal:
``` 
Condition: The 5-period EMA crosses below the 12-period EMA.
Explanation: Similar to the buy signal, but in reverse.
Logic: When the 5-period EMA crosses below the 12-period EMA, it indicates a potential downward trend. This crossover suggests that recent prices are falling faster than they were in the more extended period, signaling a possible selling opportunity.
```

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Features](#features)
- [Requirements](#requirements)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/solana-trading-script.git
    cd solana-trading-script
    ```

2. Install the required Python libraries:
    ```bash
    pip install solathon
    ```

## Usage

To run the script, you need to provide the contract address and wallet private keys as console arguments.

```bash
python main.py <CONTRACT_ADDRESS> <PRIVATE_KEY_1> <PRIVATE_KEY_2> 

```

## Configuration

```
The script uses the following configuration:

Contract Address: The Solana contract address you want to interact with.
- Wallet Private Keys: Private keys of the Solana wallets you want to use for trading.
- Buy Amounts: Amounts of SOL to buy in each cycle (defined in the script).
- Cycle Delays: Delays between transaction cycles to ensure transaction confirmations.

```


### Buy Amounts
``` 
The script includes an example list of buy amounts. You can modify these values in the script as needed:


buy_amounts = [0.01, 0.02, 0.01, 0.03, 0.01]  # Example buy amounts

```

## Features

```
- Automated Trading: Executes buy and sell transactions in a loop.
- Multi-Wallet Support: Runs concurrently for multiple wallets.
- On-Chain Transactions: Uses Solana's blockchain for all transactions.
- Customizable Buy Amounts: Easily modify the buy amounts and cycles.

```

## Requirements

```
- Python 3.6 or higher

- solathon library
```


## License

```
This project is licensed under the MIT License. See the LICENSE file for details.

```
