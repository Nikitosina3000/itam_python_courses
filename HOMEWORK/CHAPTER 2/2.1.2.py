def summation(numbers):
    plus_numbers = []
    ok_numbers = []
    numbers_list = numbers.split()
    for idx, arg in enumerate(numbers_list):
        int_arg = int(arg)
        if int_arg < 0:
            new_arg = abs(int_arg) * 2
        else:
            new_arg = int_arg
        plus_numbers.append(new_arg)
    max_of_plus_numbers = max(plus_numbers)
    for idx, arg in enumerate(plus_numbers):
        ok_arg = arg / max_of_plus_numbers
        ok_numbers.append(ok_arg)
    print(sum(ok_numbers))

summation(input())


