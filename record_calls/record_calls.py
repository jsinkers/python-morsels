from functools import wraps


def record_calls(func):
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        func_wrapper.call_count += 1
        print(f"call count: {func_wrapper.call_count}")
        return func(*args, **kwargs)

    func_wrapper.call_count = 0
    return func_wrapper
