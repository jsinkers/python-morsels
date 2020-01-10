class EasyDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getattr__(self, name):
        return self.__getitem__(name)

    def __setattr__(self, key, value):
        return self.__setitem__(key, value)

