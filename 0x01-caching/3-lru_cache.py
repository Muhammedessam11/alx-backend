#!/usr/bin/env python3
'''caching module
'''
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''FIFO Cache class
    '''

    def __init__(self) -> None:
        '''Init constructor method
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Adds item to cache_data with provided key
        '''
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                rm_key, _ = self.cache_data.popitem(True)
                print("DISCARD: {}".format(rm_key))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        '''retrives item from cache_data with provided key
        '''
        if key is None or key not in self.cache_data.keys():
            return None
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
