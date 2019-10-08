from contextlib import ContextDecorator


class suppress(ContextDecorator):
    def __init__(self, *err):
        self.err = err

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            suppress_exc = [issubclass(exc_type, err) for err in self.err]
            if True in suppress_exc:
                self.exception = exc_val
                self.traceback = exc_tb
                return True

        return False
