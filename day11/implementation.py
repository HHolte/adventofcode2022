from math import floor
from re import split as sp


GOD_NUMBER = 9699690


class Monkey:
    def __init__(self, monkey_specs: list[str], worry_decrease_factor: int):
        self.id = int(monkey_specs[0].strip(":").split(" ")[1])
        self.items = [int(element) for element in sp(":|,", monkey_specs[1].strip(" "))[1:]]
        self.operator, self.second_operand = monkey_specs[2].split(" ")[-2:]
        self.test_specs = {
            "divisor": int(monkey_specs[3].split(" ")[-1]), 
            "true": int(monkey_specs[4].split(" ")[-1]),
            "false": int(monkey_specs[5].split(" ")[-1])
        }
        self.worry_decrease_factor = worry_decrease_factor
        self.number_of_inspections = 0

    def perform_turn(self, monkeys: list["Monkey"]):
        for item in self.items:
            item = self.inspect_item(item)
            throw_to_monkey_id = self.perform_test(item)
            monkey = [monkey for monkey in monkeys if monkey.id == throw_to_monkey_id][0]
            self.throw_item(item, monkey)
        self.items.clear()

    def inspect_item(self, item: int):
        self.number_of_inspections += 1
        second_operand = item if self.second_operand == "old" else int(self.second_operand)
        item = item + second_operand if self.operator == "+" else item * second_operand
        return item % GOD_NUMBER if self.worry_decrease_factor < 2 else floor(item / self.worry_decrease_factor)

    def perform_test(self, item: int):
        return self.test_specs["true"] if item % self.test_specs["divisor"] == 0 else self.test_specs["false"]

    def receive_item(self, item: int):
        self.items.append(item)

    def throw_item(self, item: int, recipient_monkey: "Monkey"):
        recipient_monkey.receive_item(item)


def solver(filename: str, number_of_rounds, worry_decrease_factor):
    f = open(filename, 'r')
    content = f.readlines()
    f.close()
    content = [line.strip("\n") for line in content]
    monkeys = [Monkey(content[i: i + 7], worry_decrease_factor) for i in range(0, len(content), 7)]
    for i in range(number_of_rounds):
        for monkey in monkeys:
            monkey.perform_turn(monkeys)
    inspections = [monkey.number_of_inspections for monkey in monkeys]
    print(inspections)
    largest_number = max(inspections)
    inspections.remove(largest_number)
    second_largest_number = max(inspections)
    monkey_business = largest_number * second_largest_number
    return monkey_business, 0


if __name__ == "__main__":
    result_task_1_example = solver("day11/example_data.txt", 20, 3)
    result_task_2_example = solver("day11/example_data.txt", 10000, 1)
    result_task_1 = solver("day11/test_data.txt", 20, 3)
    result_task_2 = solver("day11/test_data.txt", 10000, 1)
    print("Solution to example task 1 is:", result_task_1_example)
    print("Solution to example task 2 is:", result_task_2_example)
    print("Solution to task 1 is:", result_task_1)
    print("Solution to task 1 is:", result_task_2)