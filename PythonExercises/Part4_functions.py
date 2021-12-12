"""
Create 1 function that takes in details about a person. The function should have:
- At least one required argument and one non-required argument (default value)
- The ability to handle additional keyword arguments
- if keyword arguments are passed, output them
- Output a pretty formatted version of the input
"""

def persondetails(name, age=None, **kwargs):
    if kwargs:
        print(kwargs)
    if not age:
        print(name)
    else:
        print(name, age)


persondetails("alex", 28, sex='M')