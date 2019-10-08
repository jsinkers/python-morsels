from contextlib import ContextDecorator


class suppress(ContextDecorator):
    def __init__(self, *err):
        self.err = err

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"exc_type: {exc_type}, exc_val: {exc_val}")
            suppress_exc = [issubclass(exc_type, err) for err in self.err]
            if True in suppress_exc:
                return {"exception": exc_type, "traceback": exc_tb}

        return False
