from contextlib import ContextDecorator


class suppress(ContextDecorator):
    def __init__(self, *err):
        self.err = err

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.err:
            return True
        else:
            return False
