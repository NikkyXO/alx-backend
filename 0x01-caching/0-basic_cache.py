#!/usr/bin/python3
"""BasicCache Module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache Class"""

    def __int__(self):
        """The init method of BasicCache Class"""
        super().__init__()

    def put(self, key, item):
        """The put method of BasicCache Class"""
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key):
        """The get method of BasicCache Class"""
        if key:
            if key in self.cache_data:
                return self.cache_data.get(key)
            return None
        return None
