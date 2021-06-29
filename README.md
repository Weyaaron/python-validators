

# Python-Validators

This project aims to implement decorators that help with "validation"
of other python code. It is inspired by the instance of this idea used in [sqlalchemy](https://docs.sqlalchemy.org/en/14/orm/mapped_attributes.html#sqlalchemy.orm.validates).

Since this is my first attempt at a public python library, caution is advised.

Any contribution is appreciated, especially those that aim to improve the overall quality
of the code. 

The current status is experimental at best, please do not use this in any sort
of live-system. Once stable versions have been added, this description will be 
updated. 

# Minimal Example
```
@post_validate_result_in_bounds(min=0, max=100)
def add_one(input:int ) -> int:
        return input + 1
```
If the result is not inside the specified bounds, 
an Error will be thrown. The actions that happen after
the validation has taken place will be customisable.
