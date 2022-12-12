
def get_compartments_without_duplicates(line: str):
    center_point = len(line)//2
    first_compartment = line[0:center_point]
    second_compartment = line[center_point:-1]
    return "".join(set(first_compartment)), "".join(set(second_compartment))


def get_priority_from_character(character: str):
    ascii_value = ord(character[0])
    return ascii_value - 96 if ascii_value > 90 else ascii_value - 38


def solver(filename: str):
    f = open(filename, 'r')
    sum_of_priorities_single = 0
    sum_of_priorities_badge = 0
    shared_items = ""
    for line in f.readlines():
        first_compartment, second_compartment = get_compartments_without_duplicates(line)
        shared_character = [character for character in first_compartment if character in second_compartment]
        sum_of_priorities_single += get_priority_from_character(shared_character[0])
        rucksack_without_duplicates = "".join([first_compartment, second_compartment])
        shared_items = rucksack_without_duplicates if shared_items == "" else "".join([character for character in rucksack_without_duplicates if character in shared_items])
        if len(shared_items) == 1:
            sum_of_priorities_badge += get_priority_from_character(shared_items)
            shared_items = ""
    f.close()
    return sum_of_priorities_single, sum_of_priorities_badge


if __name__ == "__main__":
    result_task_1, result_task_2 = solver("day3/test_data.txt")
    print("Solution to task 1 is:", result_task_1)
    print("Solution to task 2 is:", result_task_2)

    