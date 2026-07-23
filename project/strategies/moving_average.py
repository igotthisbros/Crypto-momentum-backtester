from utils.indicators import RollingMean

class MovingAverageStrategy:
    def __init__ (self,short_window=10,long_window=30):
        self.short = RollingMean(short_window)
        self.long = RollingMean(long_window)
        self.start_price = None
        self.bought = None

    def make_signal(self,signal,price,**extra_fields):
        base = { 
            "signal" : signal,
            "price" : price,
        }
        base.update(extra_fields)
        return base

    def on_event(self,event):
        if(self.start_price is None):
            self.start_price = event["close_price"]
        
        current_price = float(event["close_price"])
        short = self.short.update(event["close_price"])
        long = self.long.update(event["close_price"])
        if short is None or long is None:
            return
        if(short<long):
            self.bought = event["close_price"]
            return self.make_signal("BUY",current_price,short_ma=short,long_ma=long)
        else:
            buynhold = (current_price-self.start_price) / self.start_price * 100
            
            if self.bought is None:
                return self.make_signal("SELL_IGNORED",current_price,buy_and_hold_return_pct = buynhold)
            else:
                sold = (current_price-self.bought) / self.bought *100
                self.bought = None

            return self.make_signal("SELL",current_price,entry_price=self.bought,strategy_return_pct=sold, buy_and_hold_return_pct = buynhold)

async def send_signal(queue):
    strategy = MovingAverageStrategy(short_window=10, long_window=30)

    while True:
        event = await queue.get()
        
        signal = strategy.on_event(event)
        if signal is not None:
            print (signal) 
        queue.task_done()
        
        
    