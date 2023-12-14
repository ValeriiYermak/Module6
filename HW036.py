def read_employees_from_file(path):

    file = open(path, "r")
    new_list = []
    for line in file:
        new_line = line.strip()
        new_list.append(new_line)
    file.close()
    return new_list


