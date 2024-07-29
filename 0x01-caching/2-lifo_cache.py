#!/usr/bin/env python3
'''caching module
'''
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''FIFO Cache class
    '''

    def __init__(self) -> None:
        '''Init constructor method
        '''
        super().__init__()

    def put(self, key, item):
        '''Adds item to cache_data with provided key
        '''
        if key is None or item is None:
            return
        if key in self.cache_data.keys():
            del self.cache_data[key]
        self.cache_data[key] = item
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            first_key = list(self.cache_data.keys())[-2]
            print("DISCARD: {}".format(first_key))
            del self.cache_data[first_key]

    def get(self, key):
        '''retrives item from cache_data with provided key
        '''
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
