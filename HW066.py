def get_recipe(path, search_id):
    with open(path, 'r') as file:
        for line in file:
            recipe_lines = line.split(",")
            recipe_lines[-1] = recipe_lines[-1].strip()
            if search_id == recipe_lines[0]:
                recipe = {'id': recipe_lines[0], 'name': recipe_lines[1], 
                           'ingredients': recipe_lines[2:]}
                return(recipe)
        return None