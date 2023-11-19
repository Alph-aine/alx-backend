#!/usr/bin/python3
""" LIFO Caching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Puts item in cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.queue:
                last = self.queue.pop()
                del self.cache_data[last]
                print(f"DISCARD: {last}")

        if key not in self.queue:
            self.queue.append(key)
        else:
            self.move_to_last(key)

    def get(self, key):
        """ Gets item from cache """
        return self.cache_data.get(key, None)

    def move_to_last(self, item):
        """ Moves element to last idx of list """
        if self.queue[-1] != item:
            self.queue.remove(item)
            self.queue.append(item)
