from enum import Enum

class OpponentMove(int, Enum):
    A = 1 # Rock
    B = 2 # Paper
    C = 3 # Scissors


class MyMove(int, Enum):
    X = 1
    Y = 2
    Z = 3


def score_round_move_based(opponent_move: OpponentMove, my_move: MyMove):
    opponent_value = opponent_move.value
    my_value = my_move.value
    if opponent_value == my_value:
        return my_value + 3
    elif opponent_value - my_value == 1 or opponent_value - my_value == -2:
        return my_value
    else:
        return my_value + 6


def score_round_outcome_based(opponent_move: OpponentMove, outcome: str):
    opponent_value = opponent_move.value
    if outcome == 'Y':
        return opponent_value + 3
    elif outcome == 'Z':
        return 7 if opponent_value == 3 else opponent_value + 1 + 6
    else:
        return 3 if opponent_move == 1 else opponent_move - 1


def solver(file_name: str):
    f = open(file_name, 'r')
    total_score_move_based = 0
    total_score_outcome_based = 0
    for line in f.readlines():
        total_score_move_based += score_round_move_based(OpponentMove[line[0]], MyMove[line[2]])
        total_score_outcome_based += score_round_outcome_based(OpponentMove[line[0]], line[2])
    return total_score_move_based, total_score_outcome_based


if __name__ == "__main__":
    score_task_1, score_task_2 = solver("day2/test_data.txt")
    print("Solution to task 1:", score_task_1)
    print("Solution to task 2:", score_task_2)
