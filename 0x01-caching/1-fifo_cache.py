#!/usr/bin/env python3
""" module 1-fifo_cache.py """

from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Represents a data structure that implements a First-In-First-Out (FIFO)
     mechanism for storing and retrieving items from a dictionary. When the
      maximum capacity is reached, the oldest item is automatically removed
       to make space for new entries.
    """
    def __init__(self):
        """Initializes the cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache."""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print("DISCARD:", first_key)

    def get(self, key):
        """Retrieves an item by key."""
        return self.cache_data.get(key)
