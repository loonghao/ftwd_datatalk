# Import third-party modules
from fuzzywuzzy import process


class FuzzyDict(dict):
    def __getitem__(self, key):
        if key in self:
            return super().__getitem__(key)

        keys = list(self.keys())
        best_match, score = process.extractOne(key, keys)

        if score >= 80:
            return super().__getitem__(best_match)

        raise KeyError(f"Key '{key}' not found and no close match found.")

    def get(self, key, default=None):
        try:
            return self.__getitem__(key)
        except KeyError:
            return default
