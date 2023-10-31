from collections import UserDict

class DefaultExecutionDict(UserDict):
    def __getitem__(self, arg):
        key, DEFAULT_METHOD = arg
        if not key in self.data.keys():
            return DEFAULT_METHOD
        else:
            return self.data.get(key)
        