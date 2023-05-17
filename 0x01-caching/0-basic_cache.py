#!/usr/bin/env python3
""" module 0-basic_cache.py """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Represents an object that allows storing and retrieving
     items from a dictionary.
    """

    def put(self, key, item):
        """Adds an item in the cache."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves a cached item by key."""
        return self.cache_data.get(key)
