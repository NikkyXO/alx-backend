#!/usr/bin/python3
"""LIFOCache Module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache Class"""

    def __int__(self):
        """The init method of LIFOCache Class"""
        super().__init__()
        self.last_in = []

    def put(self, key, item):
        """Cache a key-value pair"""
        if key and item:
            length = len(self.cache_data)
            if key not in self.cache_data.keys() \
                    and length >= self.MAX_ITEMS:
                print(f"Discard: {self.last_in[-1]}")
                del self.cache_data[self.last_in[-1]]
                del self.last_in[-1]
            if key in self.last_in:
                del self.last_in[self.last_in.index(key)]
            self.last_in.append(key)

            self.cache_data.update({key: item})

    def get(self, key):
        """Return the value linked to a given key, or None"""
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
