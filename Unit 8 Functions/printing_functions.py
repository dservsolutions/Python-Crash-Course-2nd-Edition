def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing models: {current_design}")
        completed_models.append(current_design)
    

def show_completed_models(completed_models):
    print(f"\nThe following models have been printed: {completed_models}")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

