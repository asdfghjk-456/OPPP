def group_by_type(input_list):
    result = dict()
    for i in input_list:
        i_type = str(type(i).__name__)
        result.setdefault(i_type, []).append(i)
    return result

print(group_by_type([1, "privet", 3.14, [1, 2, 3], "laptop", 52]))

