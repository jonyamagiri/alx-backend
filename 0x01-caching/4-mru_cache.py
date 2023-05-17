#!/usr/bin/env python3
""" module 4-mru_cache.py """

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Represents a data structure that implements a Most Recently Used (MRU)
     mechanism for storing and retrieving items from a dictionary. When the
      maximum capacity is reached, the most recently accessed item is
       automatically removed to make space for new entries.
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
                    mru_key = next(iter(self.cache_data))
                    del self.cache_data[mru_key]
                    print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key."""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key)
