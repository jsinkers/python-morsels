class EasyDict(dict):
    def __init__(self, *args, **kwargs):
        if 'normalize' in kwargs.keys():
            self.normalize = True
        else:
            self.normalize = False

        super().__init__(*args, **kwargs)

    def __getattr__(self, name):
        if name is not "normalize" and self.normalize:
            name = " ".join(name.split('_'))

        try:
            return self.__getitem__(name)
        except KeyError:
            raise AttributeError

    def __setattr__(self, key, value):
        if key is not "normalize" and self.normalize:
            key = " ".join(key.split('_'))

        return self.__setitem__(key, value)

