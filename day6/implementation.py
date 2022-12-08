
def solver(filename: str, number_of_uniques: int):
    f = open(filename, 'r')
    line = f.readline()
    window = line[:number_of_uniques]
    for i in range(number_of_uniques, len(line)):
        if len(set(window)) == number_of_uniques:
            break
        window = window[1:] + line[i]
    return i


def one_line_solver(filename: str, number_of_uniques: int):
    return [i + number_of_uniques for i in range(0, len(open(filename, 'r').readline())) if len(set(open(filename, 'r').readline()[i:number_of_uniques+i])) == number_of_uniques][0]


if __name__ == "__main__":
    result_task_1_example = solver("day6/example_data.txt", 4)
    result_task_2_example = solver("day6/example_data.txt", 14)
    result_task_1 = solver("day6/test_data.txt", 4)
    result_task_2 = solver("day6/test_data.txt", 14)
    result_task_1_shorter_solver = one_line_solver("day6/test_data.txt", 4)
    result_task_2_shorter_solver = one_line_solver("day6/test_data.txt", 14)
    print("Solution to example task 1 is:", result_task_1_example)
    print("Solution to example task 2 is:", result_task_2_example)
    print("Solution to task 1 is:", result_task_1)
    print("Solution to task 2 is:", result_task_2)
    print("Short solver task 1:", result_task_1_shorter_solver)
    print("Short solver task 2:", result_task_2_shorter_solver)