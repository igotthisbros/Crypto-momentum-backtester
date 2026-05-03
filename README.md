# Crypto-momentum-backtester

This is a project about analyzing the moving average of Bitcoin prices to find patterns and backtest a trading strategy. I used Binance's public API to get the data.

### The Strategy
The program compares the 30-hour and 10-hour moving averages of BTC closing prices:
* **Buy:** When the 10-hour moving average is higher than the 30-hour moving average.
* **Sell:** When the 10-hour moving average falls below the 30-hour moving average.

### Performance
After testing on 1,000 hours of data, the program saw an 18.2% gain. In comparison, simply buying and holding BTC over the same period would have only returned 13.6%. 

### Future Improvements
I plan to add a stop-loss mechanism to protect against sudden price drops and experiment with different time intervals to see if the strategy holds up across longer periods.

### Installation
You need to install pandas, numpy, and matplotlib via pip:
```bash
pip install pandas numpy matplotlib
```
### How to use
To run the program, simply run the main.ipynb notebook in order. It will fetch the data and calculate the returns automatically.