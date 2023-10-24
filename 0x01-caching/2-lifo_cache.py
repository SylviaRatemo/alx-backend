#!/usr/bin/python3
""" LIFO
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO
      - caching system
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            pass
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            k, v = next(iter(self.cache_data.items()))
            self.cache_data.pop(k)
            print(f'DISCARD: {k}')
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
