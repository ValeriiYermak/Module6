def get_cats_info(path):
    
    cat_list = []
    
    with open(path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            cat_info = {
                "id": parts[0],
                "name": parts[1],
                "age": parts[2]
            }
            cat_list.append(cat_info)
    return cat_list