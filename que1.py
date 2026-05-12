from statistics import mean, median, mode

def list_to_matrix(lst):
    matrix = []

    while len(lst) < 9:
        lst.append(None)

    lst = lst[:9]

    for i in range(0, 9, 3):
        matrix.append(lst[i:i+3])

    return matrix


def tuple_statistics(lst):
    

    clean_list = [x for x in lst if x is not None]

    tpl = tuple(clean_list)

    result = {
        "Tuple": tpl,
        "Mean": mean(clean_list),
        "Median": median(clean_list),
        "Mode": mode(clean_list)
    }

    return result

def process_data(lst):

    matrix_result = list_to_matrix(lst.copy())
    stats_result = tuple_statistics(lst)

    final_result = {
        "Matrix_Function": matrix_result,
        "Tuple_Statistics_Function": stats_result
    }

    return final_result


user_list = list(map(int, input("Enter elements separated by space: ").split()))

output = process_data(user_list)

print("\nFinal Dictionary Output:\n")
print(output)