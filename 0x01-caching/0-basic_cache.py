#!/usr/bin/env python3
'''Basic Dictionary
'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''Class inheriting from BaseCashing
    '''

    def put(self, key, item):
        '''Adds item to cache data with the provided key
        '''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''retrives item from cache_data with provided key
        '''
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
