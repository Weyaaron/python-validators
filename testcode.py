from typeguard import typechecked

from src.post_execution.post_validators import post_validate_result_in_bounds


@post_validate_result_in_bounds(min=0, max=100)
#@typechecked
def add_one_up_until(input: int, max: int) -> int:
    if input < max:
        return input + 1
    return input


if __name__ == '__main__':
    for i in range(0, 10):
        print(add_one_up_until(i, 5))

"""
def pretty_sumab(func):
    def inner(a, b):
        print(str(a) + " + " + str(b) + " is ", end="")
        return func(a, b)

    return inner


@pretty_sumab
def sumab(a, b):
    summed = a + b
    print(summed)


#if __name__ == "__main__":
#    sumab(5, 3)



from src.input_validator import this_is_a_wrapper


@this_is_a_wrapper
def basic_func(age:int)->int:
    return age +10


if __name__ == '__main__':
    basic_func(10)
    """
