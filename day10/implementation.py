def solver(filename: str):
    f = open(filename, 'r')
    cycle = 1
    register_value = 1
    sum_of_signals = 0
    register_increment = 0
    image = ""
    while True:
        if register_increment == 0:
            line = f.readline().strip('\n')
            if not line:
                break
            register_increment = int(line.split(" ")[1]) if line[0] == 'a' else 0
            registered_at = cycle
        image += "#" if (register_value - 1 <= (cycle - 1) - 40 * ((cycle - 1) // 40) <= register_value + 1) else "."
        if (cycle - 20) % 40 == 0 and cycle <= 220:
            sum_of_signals += cycle * register_value
        elif cycle % 40 == 0:
            image += "\n"
        if registered_at == cycle - 1:
            register_value += register_increment
            register_increment = 0
        cycle += 1
    f.close()
    return sum_of_signals, image


if __name__ == "__main__":
    result_task_1_example, result_task_2_example = solver("day10/example_data.txt")
    result_task_1, result_task_2 = solver("day10/test_data.txt")
    print("Solution to example task 1 is:", result_task_1_example)
    print("Image from example task 2 is:\n" + result_task_2_example)
    print("Solution to task 1 is:", result_task_1)
    print("Image from task 2 is:\n" + result_task_2)