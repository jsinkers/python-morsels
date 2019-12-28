from dataclasses import dataclass
from functools import wraps


@dataclass
class Call:
    args: tuple
    kwargs: dict

def record_calls(func):
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        func_wrapper.call_count += 1
        func_wrapper.calls.append(Call(args, kwargs))
        print(f"call count: {func_wrapper.call_count}")
        return func(*args, **kwargs)

    func_wrapper.call_count = 0
    func_wrapper.calls = []
    return func_wrapper
