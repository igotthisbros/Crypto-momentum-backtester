import asyncio
import websockets
import json
from strategies.moving_average import send_signal
from binance_parser import parse_binance_kline_message

async def ws_feed(queue):
    url = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"
    while True:
        try:
            async with websockets.connect(url) as websocket:
                while True:
                    feed_data = await websocket.recv()
                    data = json.loads(feed_data)
                    event = parse_binance_kline_message(data)
                    if event is not None:
                        await queue.put(event)
                    
                    
        except websockets.ConnectionClosed:
            print("Disconnected, reconnecting..")
            await asyncio.sleep(3)
            continue

async def main():
    data_queue = asyncio.Queue()

    producer_task = asyncio.create_task(ws_feed(data_queue))
    consumer_task = asyncio.create_task(send_signal(data_queue))

    await asyncio.gather (producer_task, consumer_task)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Project stopped.")