class PermaDict(dict):
    def update(self, E=None, **F):
        if isinstance(E, dict):
            if set(E.keys()).intersection(self.keys()):
                raise KeyError
            else:
                dict.update(self, E, **F)
        elif isinstance(E, list):
            for ind, (key, val) in enumerate(E):
                if key in self.keys():
                    print(key)
                    raise KeyError
                else:
                    dict.update(self, {key: val}, **F)
        elif E is not None:
            dict.update(self, E, **F)
        else:
            dict.update(self, **F)

    def __setitem__(self, *args, **kwargs):
        for arg in args:
            if arg in self.keys():
                raise KeyError

        dict.__setitem__(self, *args, **kwargs)

    def force_set(self, *args):
        if len(args) == 1 and isinstance(args, dict):
            dict.update(self, args)
        elif len(args) == 2:
            key, val = args
            dict.update(self, {key: val})
        else:
            raise TypeError

