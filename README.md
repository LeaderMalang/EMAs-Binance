#  Two Exponential Moving Averages 

This trading strategy for Binance is based on the crossover of two Exponential Moving Averages (EMAs) to identify buy and sell signals. Here’s a detailed explanation:

## Buy Signal:
``` Condition: The 5-period EMA crosses above the 12-period EMA.
Explanation: The EMA (Exponential Moving Average) is a type of moving average that places a greater weight and significance on the most recent data points. A 5-period EMA is calculated based on the past 5 periods (e.g., 5 minutes, hours, days, depending on the chosen timeframe), while a 12-period EMA is based on the past 12 periods.
Logic: When the 5-period EMA crosses above the 12-period EMA, it indicates a potential upward trend. This crossover suggests that recent prices are rising faster than they were in the more extended period, signaling a possible buying opportunity. 

```
## Sell Signal:
``` 
Condition: The 5-period EMA crosses below the 12-period EMA.
Explanation: Similar to the buy signal, but in reverse.
Logic: When the 5-period EMA crosses below the 12-period EMA, it indicates a potential downward trend. This crossover suggests that recent prices are falling faster than they were in the more extended period, signaling a possible selling opportunity.
```

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/LeaderMalang/EMAs-Binance.git
    cd EMAs-Binance
    ```

2. Install the required Python libraries:
    ```
    pip install -r requirements.txt
    ```

## Usage

To run the script, you need to add binance api keys in .env file

```
python main.py 

```



## Requirements

```
- Python 3.6 or higher


```


## License

```
This project is licensed under the MIT License. See the LICENSE file for details.

```
