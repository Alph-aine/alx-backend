#!/usr/bin/env python3
'''FIFO cache'''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''Implementing a first in first out cache'''
    def __init__(self):
        '''Initializes the FIFO cache'''
        super().__init__()

    def put(self, key, item):
        '''puts items to the cache'''
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            first_key = list(self.cache_data.keys())[0]
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        '''Gets items from the cache'''
        if key is not None:
            return self.cache_data.get(key)
