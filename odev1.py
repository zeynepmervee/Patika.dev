def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def reverse_nested(lst):
    reversed_list = []
    for item in reversed(lst):
        if isinstance(item, list):
            reversed_list.append(reverse_nested(item))
        else:
            reversed_list.append(item)
    return reversed_list
