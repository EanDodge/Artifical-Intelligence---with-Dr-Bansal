import random
import math
import numpy as np

DATA_SIZE = 2
def generate_data(size_of_input, size_of_output):
    
    training_pairs = list()
    for index in range(DATA_SIZE):
        training_input = list()
        training_output = list()
        for i in range(size_of_input):
            rand1 = random.randint(0,10)
            training_input.append(rand1)
        for i in range(size_of_output):
            rand1 = random.randint(0,10)
            training_output.append(rand1)
        training_pairs.append((training_input,training_output))
    return training_pairs

def threshold_fire(input_vector, threshold_to_fire):
    output_vector = {}
    for i in input_vector:
        if(i > threshold_to_fire):
            output_vector.append(1/(math.exp(-i)))
        else:
            output_vector.append(0)
    return output_vector

def feed_forward_neural_network(size_of_input, size_of_output, training_pairs, threshold_to_fire,
                                phidden, nhidden, bias, maxcycle, tadj, learning_rate):
    
    
    trained_matracies = {}
    trained_matracies.append( np.random.rand(size_of_input, phidden))
    index = 1
    while(index < nhidden - 1):
        trained_matracies.append( np.random.rand(phidden,phidden))
        index = index+1
    trained_matracies.append( np.random.rand(phidden, size_of_output))
    training_input  = [i[0] for i in training_pairs]
    training_output = [i[1] for i in training_pairs]
    bias_vector_input = np.full(bias, size_of_input)
    bias_vector_hidden = np.full(bias, phidden)
    bias_vector_output = np.full(bias, size_of_output)

    iteration = 0
    adjusted = False
    while((iteration < maxcycle) and not(adjusted)):
        Vin = training_input
        Vin = Vin + bias_vector_input
        Vout = threshold_fire(Vin, threshold_to_fire)
        Vc = process_hidden_layers(1,nhidden)
        error = np.linalg.norm(Vout - Vc)
        if(error>tadj): 
            adjust_weights(Vout, Vc)
        else:
            adjusted = True

        if (adjusted): 
            return trained_matracies
        else:
            iteration = iteration + 1

# Main function
def main():
    training_pairs = generate_data(3,2)
    for pair in training_pairs:
        print (pair[0]," ", pair[1])
        print ()

    # phidden = input("Give number of perceptrons in each hidden layer: ")
    # nhidden = input("Give the number of hidden layers: ")
    # bias = input("Give the perceptron bias: ")
    # maxcycle = input("Give cycles to be repeated: ")
    # tadj = input("Give the threshold for neural network adjustment: ")
    # learning_rate = input("Give the learning rate: ")

if __name__ == "__main__":
    main()