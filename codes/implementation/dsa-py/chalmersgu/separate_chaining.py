from .adt.map import Map

class SeparateChainingHashMap(Map):
    def get(self, key):
        I = self._hash(key)