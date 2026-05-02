# Crypto-momentum-backtester

This is a project about analyzing the moving average of the price of a bitcoin to find patterns in it and try to earn money out of it. I used Binance's public api to get data.

I compared between the moving average of the past 30 hour's BTC closing price and if the moving average of it was higher than the moving average of the past 10 hour's BTC closing price, I made a 'signal' to buy. Did the opposite for chossing when to sell.

To run this program, simply run the main.ipynb notebook in order. You would need to install pandas,numpy, and matplotlib from pip.

They can be done with the following commands:
pip install pandas
pip install numpy
pip install matplotlib

After applying it to 1000hours it we saw an 18.2% gain. So if I had invested 1 dollar into BTC and have this program sell and buy, it would have performed better than if I had invested and not done anything and wait. As it only rose 13.6% without intervention. 