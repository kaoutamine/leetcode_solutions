class StockPrice:
    """for maximum and minimum, I need to track the highest price and also  
    able to know if this price was modified so I'll probably also need to 
    store the maximum and minimum index if it's updated Does that also mean 
    I'll need to refind the maximum or minimum in O(n) 
    if it's needed => do it via a minheap"""
    def __init__(self):
        self.ttp = {} #timestamp to price
        self.max_timestamp = 0
        self.price_min_heap = []
        self.price_max_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.ttp[timestamp] = price
        self.max_timestamp = max(timestamp, self.max_timestamp)
        heappush(self.price_min_heap, (price, timestamp))
        heappush(self.price_max_heap, (-price, timestamp))

    def current(self) -> int:
        return self.ttp[self.max_timestamp]
        

    def maximum(self) -> int:
        price, timestamp = heappop(self.price_max_heap)
        while self.ttp[timestamp] != - price: #skip outdated values in heap
            price, timestamp = heappop(self.price_max_heap)
        heappush(self.price_max_heap, (price, timestamp))
        return - price
        

    def minimum(self) -> int:
        price, timestamp = heappop(self.price_min_heap)
        while self.ttp[timestamp] != price: #skip outdated values in the heap
            price, timestamp = heappop(self.price_min_heap)
        heappush(self.price_min_heap, (price, timestamp))
        return price
    
        

        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()