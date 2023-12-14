def add_employee_to_file(record, path):
    
    file = open(path, "a")
    file.write(record + '\n')
    file.close()

    