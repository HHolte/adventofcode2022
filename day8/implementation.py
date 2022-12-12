import numpy as np


def get_visibility_status_and_scenic_score(data_row, current_element, backwards = False):
    visible = True
    scenic_score = -1
    if backwards:
        data_row = np.flip(data_row)
    for k in range(len(data_row)):
        if data_row[k] >= current_element:
            visible = False
            scenic_score = k + 1
            break
    if scenic_score == -1:
        scenic_score = len(data_row)
    return visible, scenic_score


def solver(filename: str):
    f = open(filename, 'r')
    data_list = []
    for line in f.readlines():
        line = line.strip('\n')
        data_list.append([int(height) for height in line])
    data_matrix = np.array(data_list)
    n_rows, n_columns = data_matrix.shape
    n_visible_trees = 0
    scenic_scores = []
    for i in range(1, n_rows - 1):
        for j in range(1, n_columns - 1):
            current_element = data_matrix[i, j]
            visible_from_left, scenic_score_left = get_visibility_status_and_scenic_score(data_matrix[i, 0:j], current_element, True)
            visible_from_right, scenic_score_right = get_visibility_status_and_scenic_score(data_matrix[i, j+1:n_columns], current_element)
            visible_from_above, scenic_score_above = get_visibility_status_and_scenic_score(data_matrix[0:i, j], current_element, True)
            visible_from_below, scenic_score_below = get_visibility_status_and_scenic_score(data_matrix[i+1:n_rows, j], current_element)
            n_visible_trees += any([visible_from_left, visible_from_right, visible_from_below, visible_from_above])
            scenic_score = scenic_score_left * scenic_score_right * scenic_score_below * scenic_score_above
            scenic_scores.append(scenic_score)
    n_visible_trees += 2 * n_rows + 2 * n_columns - 4
    scenic_score = max(scenic_scores)
    f.close()
    return n_visible_trees, scenic_score


if __name__ == "__main__":
    result_task_1, result_task_2 = solver("day8/test_data.txt")
    print("Solution to task 1 is:", result_task_1)
    print("Solution to task 2 is:", result_task_2)
