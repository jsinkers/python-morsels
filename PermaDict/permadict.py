class PermaDict(dict):
    def __init__(self, *args, silent=False, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self.silent = silent

    def update(self, E=None, **F):
        if isinstance(E, dict):
            if set(E.keys()).intersection(self.keys()):
                self.update_existing()
            else:
                dict.update(self, E, **F)
        elif isinstance(E, list):
            for ind, (key, val) in enumerate(E):
                if key in self.keys():
                    self.update_existing()
                else:
                    dict.update(self, {key: val}, **F)
        elif E is not None:
            dict.update(self, E, **F)
        else:
            dict.update(self, **F)

    def __setitem__(self, *args, **kwargs):
        key, val = args
        if key in self.keys():
            self.update_existing()
        else:
            dict.__setitem__(self, *args, **kwargs)

    def force_set(self, *args):
        if len(args) == 1 and isinstance(args, dict):
            dict.update(self, args)
        elif len(args) == 2:
            key, val = args
            dict.update(self, {key: val})
        else:
            raise TypeError

    def update_existing(self):
        if not self.silent:
            raise KeyError
