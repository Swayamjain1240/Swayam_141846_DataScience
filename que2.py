def add_numbers(a, b):
    return a + b

def process_list(lst, total):

    mid_index = len(lst) // 2
    mid_value = lst[mid_index]

    print("Middle Value :", mid_value)

    
    if total > mid_value:
        result = set(lst[:mid_index + 1])
        print("Set Output :", result)

    
    elif total == mid_value:
        result = {mid_index: mid_value}
        print("Dictionary Output :", result)

    
    else:
        result = tuple(lst[mid_index + 1:])
        print("Tuple Output :", result)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


lst = list(map(int, input("Enter list elements separated by space: ").split()))

sum_result = add_numbers(num1, num2)
print("Sum =", sum_result)
process_list(lst, sum_result)