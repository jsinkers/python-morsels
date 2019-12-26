# @record_calls
# def function()
def record_calls(func):
    def func_wrapper(func):
        try:
            func.call_count += 1
        except AttributeError:
            func.call_count = 0
        return func

    return func_wrapper(func)
