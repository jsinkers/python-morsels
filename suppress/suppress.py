from contextlib import contextmanager


@contextmanager
def suppress(error):
    try:
        yield
    except error:
        pass
