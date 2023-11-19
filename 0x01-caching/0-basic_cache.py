#!/usr/bin/env python3
'''Basic caching method'''

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    ''' Basic Cache class'''

    def put(self, key, item):
        '''Add an item to the cache'''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''Get an item from the cache'''
        if key is not None:
            return self.cache_data.get(key)
        return None
