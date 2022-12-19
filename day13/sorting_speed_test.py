from ast import literal_eval
from implementation import sort_into_list, binary_sort_into_list
from timeit import default_timer as timer


methods_to_test = [sort_into_list, binary_sort_into_list]


def test_sorting_methods(filename: str, methods_to_test, iterations):
    lines = []
    f = open(filename, 'r')
    for line in f.readlines():
        line = line.strip("\n")
        if line != "":
            line_as_list = literal_eval(line)
            lines.append(line_as_list)
    f.close()
    times = {}
    for method in methods_to_test:
        times_for_method = []
        for i in range(iterations):
            sortd_list = [[[2]], [[6]]]
            start = timer()
            for line in lines:
                sortd_list = method(sortd_list, line)
            end = timer()
            times_for_method.append((end - start) * 1000)
        times[method.__name__] = sum(times_for_method) / iterations
    return times


if __name__ =="__main__":
    iterations = 10
    timer_results = test_sorting_methods("day13/test_data.txt", methods_to_test, iterations)
    print("Results from speed testing with " + str(iterations) + " iterations\n"
    + "-" * 45)
    for key, value in timer_results.items():
        print(key + ": " + str(round(value, 3)) + "ms")
    print("-" * 45)