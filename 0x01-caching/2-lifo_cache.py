#!/usr/bin/env python3
""" module 2-lifo_cache.py """

from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Represents a data structure that implements a Last-In-First-Out (LIFO)
     mechanism for storing and retrieving items from a dictionary. When the
      maximum capacity is reached, the most recent item is automatically
       removed to make space for new entries.
    """
    def __init__(self):
        """Initializes the cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache."""
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > self.MAX_ITEMS:
                    last_key = next(reversed(self.cache_data))
                    del self.cache_data[last_key]
                    print("DISCARD:", last_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieves an item by key."""
        return self.cache_data.get(key)
