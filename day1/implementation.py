def check_number(number: int, highest_scores: list[int]) -> list[int]:
    if number > highest_scores[0]:
        highest_scores.pop()
        highest_scores.insert(0, number)
    elif number > highest_scores[1]:
        highest_scores.pop()
        highest_scores.insert(1, number)
    elif number > highest_scores[2]:
        highest_scores.pop()
        highest_scores.insert(2, number)
    return highest_scores

def solver(file_name: str) -> float:
    f = open(file_name, 'r')
    highest_scores = [0, 0, 0]
    current_number = 0
    for line in f.readlines():
        if line == "\n":
            highest_scores = check_number(current_number, highest_scores)
            current_number = 0
            continue
        current_number += int(line)
    highest_scores = check_number(current_number, highest_scores)
    f.close()
    return highest_scores

if __name__ == "__main__":
    example_solution = solver("day1/test_data.txt")
    print("Solution to task 1:", example_solution[0])
    print("Solution to task 2:", sum(example_solution))