from enum import Enum

class Coordinates:
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
    
    def __add__(self, other: "Coordinates"):
        return Coordinates(
            self.x_coordinate + other.x_coordinate,
            self.y_coordinate + other.y_coordinate
        )

    def __eq__(self, other: "Coordinates"):
        return self.x_coordinate == other.x_coordinate and self.y_coordinate == other.y_coordinate

    def get_differences(self, other: "Coordinates"):
        return self.x_coordinate - other.x_coordinate, self.y_coordinate - other.y_coordinate

class Direction(tuple[int], Enum):
    U = (1, 0)
    D = (-1, 0)
    R = (0, 1)
    L = (0, -1)


class Head:
    def __init__(self, initial_coordinates: Coordinates):
        self.position = initial_coordinates
    
    def move_head(self, direction: Coordinates):
        self.position += direction


class Segment:
    def __init__(self, initial_coordinates: Coordinates):
        self.position = initial_coordinates
        self.prev_position_of_predecessor = initial_coordinates

    def move_segment(self, predecessor_position: Coordinates):
        difference_x, difference_y = self.position.get_differences(predecessor_position)
        if abs(difference_x) >= 2 or abs(difference_y) >= 2:
            suggested_position = self.prev_position_of_predecessor
            suggested_difference_x, suggested_difference_y = suggested_position.get_differences(predecessor_position)
            if abs(suggested_difference_x) == 1 and abs(suggested_difference_y) == 1:
                

        self.prev_position_of_predecessor = predecessor_position

class Tail(Segment):
    def __init__(self, initial_coordinates: Coordinates):
        super().__init__(initial_coordinates)
        self.positions_visited = [initial_coordinates]

    def add_position_if_not_previously_visited(self):
        if self.position not in self.positions_visited:
            self.positions_visited.append(self.position)


def solver(filename: str, number_of_extra_segments: int = 0):
    f = open(filename, 'r')
    initial_position = Coordinates(0, 0)
    head = Head(initial_position)
    tail = Tail(initial_position)
    segments = [Segment(initial_position) for i in range(number_of_extra_segments)]
    for line in f.readlines():
        line = line.strip('\n')
        direction = Direction[line[0]]
        direction_in_coordinates = Coordinates(direction[0], direction[1])
        number_of_moves = int(line[2:])
        for i in range(number_of_moves):
            head.move_head(direction_in_coordinates)
            prev_segment_position = head.position
            for i in range(len(segments)):
                segments[i].move_segment(prev_segment_position)
                prev_segment_position = segments[i].position
            tail.move_segment(prev_segment_position)
            tail.add_position_if_not_previously_visited()
    number_of_positions_visited = len(tail.positions_visited)
    return number_of_positions_visited


if __name__ == "__main__":
    result_task_1_example = solver("day9/example_data.txt")
    result_task_2_example = solver("day9/example_data.txt", 8)
    result_task_1 = solver("day9/test_data.txt")
    result_task_2 = solver("day9/test_data.txt", 8)
    print("Solution to example task 1 is:", result_task_1_example)
    print("Solution to example task 2 is:", result_task_2_example)
    print("Solution to task 1 is:", result_task_1)
    print("Solution to task 2 is:", result_task_2)