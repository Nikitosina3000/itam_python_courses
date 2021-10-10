def debug_control(*args, **kwargs):
    count_of_int = 0
    count_of_str = 0
    count_of_float = 0
    for idx, arg in enumerate(args):
        if type(arg) == str:
            count_of_str += 1
        elif type(arg) == int:
            count_of_int += 1
        else:
            count_of_float += 1
    for key, kwarg in kwargs.items():
        if type(kwarg) == str:
            count_of_str += 1
        elif type(kwarg) == int:
            count_of_int += 1
        else:
            count_of_float += 1
    print(f"str: {count_of_str}, int: {count_of_int}, float: {count_of_float}")


debug_control("Hello!", 1000, 7, 993.0, name="Petr", task="Eliminate")
