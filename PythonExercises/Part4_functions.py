"""
Create 1 function that takes in details about a person. The function should have:
- At least one required argument and one non-required argument (default value)
- The ability to handle additional keyword arguments
- if keyword arguments are passed, output them
- Output a pretty formatted version of the input
"""


def keyword_test(name, age=None, **kwargs):
    print(f"Name: {name}")
    if age:
        print(f"Age: {str(age)}")
    if kwargs:
        for k, v in kwargs.items():
            print(f"{k}: {v}")


if __name__ == "__main__":
    keyword_test("Alexandre", age=28, address="123 Main Street", phone="12345678")
