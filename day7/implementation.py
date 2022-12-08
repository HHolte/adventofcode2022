### NOT SOLVED ###

def solver(filename: str):
    f = open(filename, 'r')
    directory_sizes = {}
    current_dir_size = 0
    current_dir_name = ""
    total_sum_of_relevant_directories = 0
    potential_delete_directory_sizes = []
    total_size = 0
    taken_into_account = []
    for line in reversed(f.readlines()):
        line = line.strip("\n")
        if line[0] == '$':
            if line[2] == 'l':
                continue
            elif line[-1] == '.':
                continue
            elif line[-1] == '/':
                total_size += current_dir_size
            else:
                current_dir_name = line[5:]
                if current_dir_name in directory_sizes.keys():
                    if directory_sizes[current_dir_name] <= 100000:
                        total_sum_of_relevant_directories += directory_sizes[current_dir_name]
                    if directory_sizes[current_dir_name] >= 1198493:
                        potential_delete_directory_sizes.append(directory_sizes[current_dir_name])
                    if current_dir_name not in taken_into_account:
                        total_size += directory_sizes[current_dir_name] - current_dir_size
                    else:
                        taken_into_account.remove(current_dir_name)
                directory_sizes[current_dir_name] = current_dir_size
                current_dir_size = 0
        elif line[0] == 'd':
            current_dir_size += directory_sizes[line[4:]]
            taken_into_account.append(line[4:])
        else:
            current_dir_size += int(line.split(" ")[0])
    for size in directory_sizes.values():
        if size <= 100000:
            total_sum_of_relevant_directories += size
        if size >= 1198493:
            potential_delete_directory_sizes.append(size)
    best_delete_size = min(potential_delete_directory_sizes)
    return total_sum_of_relevant_directories, best_delete_size
    # Find bottom directory by finding last cd, say it's called d
    # Sum names of all files up to ls statement, call the sum S_d
    # Then size(dir d) = S_d
    # Save this as a variable
    # Find next directory by finding the next cd statement followed by a letter, call it c
    # Sum file names as before, but if any file names are directories then add the size of that directory
    # Do this all the way to the top and it should work

if __name__ == "__main__":
    result_task_1, result_task_2 = solver("day7/test_data.txt")
    print("Note: This implementation does not obtain the correct solutions.")
    print("Solution to task 1 is:", result_task_1)
    print("Solution to task 2 is:", result_task_2)