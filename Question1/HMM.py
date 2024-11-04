import numpy as np
from itertools import product

# transition matrix, emission matrix, init vec
def hidden_markov_model(size_of_graph, size_of_emissions):
    # Transition matrix
    transitions = np.random.rand(size_of_graph, size_of_graph)
    transitions /= transitions.sum(axis=1, keepdims=True)
    print(transitions)
    # Emission matrix
    emissions = np.random.rand(size_of_graph, size_of_emissions)
    emissions /= emissions.sum(axis=1, keepdims=True)

    # Initial vector
    init_vec = np.random.rand(size_of_graph)
    init_vec /= init_vec.sum()

    return transitions, emissions, init_vec


def best_path(size_of_graph, size_of_emissions, transitions, emissions, init_vec):
    states = np.arange(size_of_graph)
    cartesian = list(product(states, repeat=size_of_graph))
    print (cartesian)
    newcartesian = list()
    
    # Filter paths 
    for path in cartesian:
        add_flag = True #check when to add it
        if init_vec[path[0]] == 0:
            add_flag = False  # Skip paths where the initial probability is 0

        for j in range(len(path) - 1):
            state1 = path[j]
            state2 = path[j + 1]
            
            if transitions[state1][state2] < 0.25:
                add_flag = False # we no longer want to add it
                break

        # if path is good, add it
        if add_flag:
            newcartesian.append(path)
    
    print(newcartesian)
# Main function
def main():
    transitions, emissions, init_vec = hidden_markov_model(3, 4)
    best_path(3, 4, transitions, emissions, init_vec)

if __name__ == "__main__":
    main()
