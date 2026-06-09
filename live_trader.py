import asyncio
import websockets
import json
from collections import deque

d1 = deque(maxlen=10)
d2 = deque(maxlen=30)


async def btc_quant():
    url = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"
    start_price= None
    bought = 0
    sold = 0
    while(True):
        try:
            async with websockets.connect(url) as websocket:
                while(True):
                    btc_data = await websocket.recv()
                    data = json.loads(btc_data)
                    print(data)
                    #The data comes in a dictionary. The data we need is in the key 'k'
                    # 'k' is another dictionary where 'x' key has the boolean data of if the price is closed or not.
                    if(data["k"]["x"]):
                        if(start_price is None):
                            start_price = float(data["k"]["c"])
                            print(f"Start Price! {start_price}")
                        #'c' contains data on the closing price of the bitcoin
                        print(data["k"]["c"])
                        #'v' contains data on the volume of the bitcoin trades
                        print(data["k"]["v"])
                        print(data["k"]["x"])
                        d1.append(float(data["k"]["c"]))
                        d2.append(float(data["k"]["c"]))
                        if(len(d1)>=10):
                            ma10 = sum(d1) / 10 
                            print(ma10)
                        if(len(d2) >= 30):
                            ma30 = sum(d2) / 30 
                            print(ma30)
                            current_price = float(data['k']['c'])
                            if(ma10<ma30):
                                print(f"BUY at ${data['k']['c']}")
                                bought = data['k']['c']
                            else:
                                print(f"SELL at ${data['k']['c']}")
                                buynhold = (current_price-start_price) / start_price * 100
                                sold = (current_price-bought) / bought *100
                                if(sold>0): print(f"Net profit of {sold} gained \n")
                                else: print(f"Net loss of {sold} lost")
                                print(f"While buy&hold performed {buynhold}")
                                
                                
        except websockets.ConnectionClosed:
            print("Disconnected, reconnecting..")
            await asyncio.sleep(3)
            continue

            
            


if __name__ == "__main__" :
    asyncio.run(btc_quant())