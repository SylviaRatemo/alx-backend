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
            k = list(self.cache_data.keys())[-1]
            del self.cache_data[k]
            print(f'DISCARD: {k}')
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
