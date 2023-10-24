#!/usr/bin/python3
""" Baseic Cacche
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache
      - caching system
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
