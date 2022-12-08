from math import ceil
from copy import deepcopy

def move_crates(n_crates: int, from_stack: list[str], to_stack: list[str], crane_9001 = False):
    n_crates = len(from_stack) if n_crates > len(from_stack) else n_crates
    if crane_9001:
        to_stack += [from_stack.pop(-n_crates + i) for i in range(n_crates)]
    else:
        to_stack += [from_stack.pop() for i in range(n_crates)]
    return from_stack, to_stack


def get_move_data(line: str):
    split_line = line.split(" ")
    return int(split_line[1]), int(split_line[3]), int(split_line[5])


def assign_crates_to_stacks(line: str, stacks):
    for i in range(len(line)):
        if line[i].isalpha():
            stacks[ceil(i/4)].insert(0, (line[i]))
    return stacks


def solver(filname: str):
    f = open(filname, 'r')
    first_line = f.readline()
    number_of_stacks = ceil(len(first_line) / 4)
    stacks = assign_crates_to_stacks(first_line, {i: [] for i in range(1, number_of_stacks+1)})
    stacks_for_crane_9001 = {}
    structure_not_complete = True
    for line in f.readlines():
        line = line.strip('\n')
        if structure_not_complete:
            stacks = assign_crates_to_stacks(line, stacks)
            if line == "":
                structure_not_complete = False
                stacks_for_crane_9001 = deepcopy(stacks)
            continue
        n_crates, from_stack, to_stack = get_move_data(line)
        updated_from_stack, updated_to_stack = move_crates(n_crates, stacks[from_stack], stacks[to_stack])
        updated_from_stack_crane_9001, updated_to_stack_crane_9001 = move_crates(n_crates, stacks_for_crane_9001[from_stack], stacks_for_crane_9001[to_stack], True)
        stacks[from_stack] = updated_from_stack
        stacks[to_stack] = updated_to_stack
        stacks_for_crane_9001[from_stack] = updated_from_stack_crane_9001
        stacks_for_crane_9001[to_stack] = updated_to_stack_crane_9001
    return "".join([stack[-1] for stack in stacks.values() if stack]), "".join([stack[-1] for stack in stacks_for_crane_9001.values() if stack]) 

if __name__ == "__main__":
    result_task_1_example, result_task_2_example = solver("day5/example_data.txt")
    result_task_1, result_task_2 = solver("day5/test_data.txt")
    print("Solution to example task 1 is:", result_task_1_example)
    print("Solution to example task 2 is:", result_task_2_example)
    print("Solution to task 1 is:", result_task_1)
    print("Solution to task 2 is:", result_task_2)