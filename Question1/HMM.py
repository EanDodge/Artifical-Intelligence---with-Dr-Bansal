import numpy as np
from itertools import product

# transition matrix, emission matrix, init vec
def hidden_markov_model(size_of_graph, size_of_emissions):
    # Transition matrix
    transitions = np.random.rand(size_of_graph, size_of_graph)
    transitions /= transitions.sum(axis=1, keepdims=True)
    print("trans", transitions)
    # Emission matrix
    emissions = np.random.rand(size_of_graph, size_of_emissions)
    emissions /= emissions.sum(axis=1, keepdims=True)
    print("emit", emissions)
    # Initial vector
    init_vec = np.random.rand(size_of_graph)
    init_vec /= init_vec.sum()
    print("init", init_vec)

    return transitions, emissions, init_vec


def all_paths(size_of_graph, size_of_emissions, transitions, emissions, init_vec):
    states = np.arange(size_of_graph)
    cartesian = list(product(states, repeat=size_of_graph))
    #print (cartesian)
    newcartesian = list()
    
    # Filter paths 
    for path in cartesian:
        add_flag = True #check when to add it
        if init_vec[path[0]] < .15:
            #print("init issue")
            add_flag = False  # Skip paths where the initial probability is 0

        for j in range(len(path) - 1):
            state1 = path[j]
            state2 = path[j + 1]
            
            if transitions[state1][state2] < 0.25:
                #print("transitions issue")
                add_flag = False # we no longer want to add it
                break
            if emissions[state1][state2] < 0.10:
                #print("emission issue")
                add_flag = False # we no longer want to add it
                break

        # if path is good, add it
        if add_flag:
            newcartesian.append(path)
    
    return newcartesian

def best_path(newcartesian, transitions, emissions, init_vec, emits):
    print(newcartesian)
    min_value = list()
    for path in newcartesian:
        result = 0
        init_prob = init_vec[path[0]]
        emit_prob = emissions[path[0]][int(emits[0])]
        result = init_prob * emit_prob
        for i in range(len(path)-1):
            state1 = path[i]
            state2 = path[i+1]
            value = transitions[state1][state2]
            value2 = emissions[state2][i]
            result *= value 
            result *= value2
        min_value.append(result)
    min_val = min(min_value) 
    min_index = min_value.index(min_val)
    min_val = round(min_val, 6)
    print(min_val)
    return newcartesian[min_index]




# Main function
def main():
    emits = list("0123")
    #print(emits[2])
    emit_size = len(emits)
    state_size = 3
    transitions, emissions, init_vec = hidden_markov_model(state_size,emit_size )
    newcartesian = all_paths(state_size, emit_size, transitions, emissions, init_vec)
    min_car = best_path(newcartesian,transitions, emissions, init_vec, emits )
    print(min_car)


if __name__ == "__main__":
    main()
