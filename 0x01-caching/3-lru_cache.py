#!/usr/bin/python3
""" LRU Caching """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU caching """

    def __init__(self):
        """Initializes the class"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Puts item in cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.get_first(self.queue)
            if first_key:
                self.queue.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

        if key not in self.queue:
            self.queue.append(key)
        else:
            self.move_to_last(key)

    def get(self, key):
        """ Gets item from cache """
        item = self.cache_data.get(key, None)
        if item is not None:
            self.move_to_last(key)
        return item

    def move_to_last(self, item):
        """ Moves element to last idx of list """
        if self.queue[-1] != item:
            self.queue.remove(item)
            self.queue.append(item)

    @staticmethod
    def get_first(array):
        '''gets the first element of a list'''
        return array[0] if array else None
