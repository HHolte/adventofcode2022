from re import split

def solver(filename: str):
    f = open(filename, 'r')
    number_of_complete_overlaps = 0
    total_number_of_overlaps = 0
    for line in f.readlines():
        sections = split('-|,', line)
        sections = [int(section) for section in sections]
        complete_overlap = (sections[0] >= sections[2] and sections[1] <= sections[3]) or (sections[2] >= sections[0] and sections[3] <= sections[1])
        number_of_complete_overlaps += complete_overlap
        total_number_of_overlaps += (sections[2] <= sections[0] <= sections[3]) ^ (sections[2] <= sections[1] <= sections[3]) and not complete_overlap
    total_number_of_overlaps += number_of_complete_overlaps
    return number_of_complete_overlaps, total_number_of_overlaps


if __name__ == "__main__":
    result_task_1, result_task_2 = solver("day4/test_data.txt")
    print("Solution to task 1 is:", result_task_1)
    print("Solution to task 2 is:", result_task_2)