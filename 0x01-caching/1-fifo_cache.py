#!/usr/bin/python3
"""FIFOCache Module"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache Class"""

    def __int__(self):
        """The init method of FIFOCache Class"""
        super().__init__()

    def put(self, key, item):
        """Cache a key-value pair"""
        if key and item:
            if len(self.cache_data) == self.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                first_item_key = list(self.cache_data.keys())[0]
                self.cache_data.pop(first_item_key)
                print(f"Discard: {first_item_key}")

            self.cache_data.update({key: item})

    def get(self, key):
        """The get method of FIFOCache Class"""
        if key:
            if key in self.cache_data:
                return self.cache_data.get(key)
            return None
        return None
