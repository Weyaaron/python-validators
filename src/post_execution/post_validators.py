from typing import Any


def post_validate_result_in_bounds(min: Any, max: Any):
    print("One")

    def wrapper_with_func(func):
        print("Two")

        def raise_error(*args):
            print("Three")
            result = func(*args)
            if not min < result < max:
                raise AssertionError("The Validator failed!")
            return result

        return raise_error

    return wrapper_with_func


def decorator_with_arg(*name, **kw):
    range = kw.get("is_in_range", [])
    print(f"Has been called with{name}")

    def inner_func(func):
        return func

    return inner_func
