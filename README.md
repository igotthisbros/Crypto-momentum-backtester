# Crypto-momentum-backtester

This is a project about analyzing the moving average of Bitcoin prices to find patterns and backtest a trading strategy, and putting that to test in live date. I used Binance's public API to get the data.

### The Strategy
The program compares the 30-hour and 10-hour moving averages of BTC closing prices:
* **Buy:** When the 10-hour moving average is higher than the 30-hour moving average.
* **Sell:** When the 10-hour moving average falls below the 30-hour moving average.
In the live trader version, to see results more quickly, I changed the 10/30 hour moving average to 10/30 minutes moving average. 

### Performance
After testing on 1,000 hours of data, the program saw an 18.2% gain. In comparison, simply buying and holding BTC over the same period would have only returned 13.6%. 

### Future Improvements
I plan to receive live data from binance using websockets to simulate trading in real time and see if my strategy is working real time.

### Installation
You need to install pandas, numpy, and matplotlib for the backtester, and websockets for the live trader:
```bash
pip install pandas numpy matplotlib websockets
```
### How to use
To run the backtester, simply run the backtester.ipynb notebook in order. It will fetch the data and calculate the returns automatically. 
To test it with live date, run the live_trader.py. The program will receive live data through websocket from binance. Minimum of 30 minutes must be waited to observe its first buy/sell.