from ast import literal_eval
from math import floor


def evaluate_lists(first_list, second_list):
    first_length = len(first_list)
    second_length = len(second_list)
    if first_length == 0 and second_length != 0:
        return 1
    elif second_length == 0 and first_length != 0:
        return -1
    shortest = min(first_length, second_length)
    for i in range(shortest):
        current_item_first = first_list[i]
        current_item_second = second_list[i]
        if type(current_item_first) == int and type(current_item_second) == int:
            if current_item_first < current_item_second:
                return 1
            if current_item_second < current_item_first:
                return -1
        else:
            out = evaluate_lists([current_item_first] if type(current_item_first) == int else current_item_first, [current_item_second] if type(current_item_second) == int else current_item_second)
            if out != 0:
                return out
        if i == shortest - 1:
            if first_length < second_length:
                return 1
            elif first_length > second_length:
                return -1
            else:
                return 0
    return 0


def sort_into_list(main_list, list_to_insert):
    for i in range(len(main_list)):
        sort_above = evaluate_lists(list_to_insert, main_list[i])
        if sort_above == 1 or sort_above == 0:
            main_list.insert(i, list_to_insert)
            break
    return main_list


def binary_sort_into_list(main_list, list_to_insert):
    middle_point = floor(len(main_list) / 2)
    sort_above = evaluate_lists(list_to_insert, main_list[middle_point])
    if sort_above == 1 or sort_above == 0:
        if len(main_list[:middle_point + 1]) == 1:
            main_list.insert(0, list_to_insert)
        else:
            main_list[:middle_point] = binary_sort_into_list(main_list[:middle_point], list_to_insert)
    else:
        if len(main_list[middle_point:]) == 1:
            main_list.append(list_to_insert)
        else:
            main_list[middle_point + 1:] = binary_sort_into_list(main_list[middle_point + 1:], list_to_insert)
    return main_list


def solver_task_1(filename: str):
    f = open(filename, 'r')
    pairs_are_in_order = []
    current_pair = []
    for line in f.readlines():
        line = line.strip("\n")
        if line != "":
            line_as_list = literal_eval(line)
            current_pair.append(line_as_list)
        if len(current_pair) == 2:
            order_is_correct = evaluate_lists(current_pair[0], current_pair[1])
            pairs_are_in_order.append(True if order_is_correct != -1 else False)
            current_pair.clear()
    f.close()
    sum_of_indices = sum([i + 1 for i in range(len(pairs_are_in_order)) if pairs_are_in_order[i]])
    return sum_of_indices


def solver_task_2(filename: str):
    f = open(filename, 'r')
    sorted_packets = [[[2]], [[6]]]
    for line in f.readlines():
        line = line.strip("\n")
        if line != "":
            line_as_list = literal_eval(line)
            sorted_packets = binary_sort_into_list(sorted_packets, line_as_list)
    f.close()
    first_divider = sorted_packets.index([[2]]) + 1
    second_divider = sorted_packets.index([[6]]) + 1
    return first_divider * second_divider


if __name__ == "__main__":
    result_task_1_example = solver_task_1("day13/example_data.txt")
    result_task_1 = solver_task_1("day13/test_data.txt")
    result_task_2_example = solver_task_2("day13/example_data.txt")
    result_task_2 = solver_task_2("day13/test_data.txt")
    print("Solution to example task 1 is:", result_task_1_example)
    print("Solution to task 1 is:", result_task_1)
    print("Solution to example task 2 is:", result_task_2_example)
    print("Solution to task 2 is:", result_task_2)