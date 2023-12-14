def write_employees_to_file(employee_list, path):

    file = open(path,"w")

    n_string = ""

    for el in employee_list:
        string = "\n".join(el)
        n_string = n_string + string + "\n"
        file.write(n_string)
    file.close()
    
