#!/usr/bin/env python3
""" Basic Caching System Implementation
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
        return self.cache_data.get(key)
