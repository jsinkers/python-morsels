from dataclasses import dataclass
from functools import wraps


NO_RETURN = object()


@dataclass
class Call:
    args: tuple
    kwargs: dict


def record_calls(func):
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        func_wrapper.call_count += 1
        call = Call(args, kwargs)
        func_wrapper.calls.append(call)
        print(f"call count: {func_wrapper.call_count}")
        try:
            call.exception = None
            call.return_value = func(*args, **kwargs)
        except BaseException as e:
            call.exception = e
            call.return_value = NO_RETURN
            raise

        return call.return_value

    func_wrapper.call_count = 0
    func_wrapper.calls = []
    return func_wrapper
