import asyncio
import websockets
import json
from collections import deque

d1 = deque(maxlen=10)
d2 = deque(maxlen=30)

async def hello():
    url = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"
    async with websockets.connect(url) as websocket:
        
        while(True):
            btc_data = await websocket.recv()
            data = json.loads(btc_data)
            if(data["k"]["x"]):
                print(data["k"]["c"])
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
                if(ma10<ma30):
                    print(f"BUY at ${data['k']['c']}")
                else:
                    print(f"SELL at ${data['k']['c']}")


            
            


if __name__ == "__main__" :
    asyncio.run(hello())