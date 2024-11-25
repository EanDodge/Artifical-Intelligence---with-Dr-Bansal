import numpy as np
def feed_forward_neural_network(size_of_input, size_of_output, training_vectors, threshold_to_fire):
    
    phidden = input("Give number of perceptrons in each hidden layer: ")
    nhidden = input("Give the number of hidden layers: ")
    bias = input("Give the perceptron bias: ")
    maxcycle = input("Give cycles to be repeated: ")
    tadj = input("Give the threshold for neural network adjustment: ")
    learning_rate = input("Give the learning rate: ")
    trained_matracies = list(nhidden)
    trained_matracies[0] = np.random.rand(size_of_input, phidden)
    trained_matracies[nhidden-1] = np.random.rand(phidden, size_of_output)
    index = 1
    while(index < nhidden - 1):
        trained_matracies[index] = np.random.rand(phidden,phidden)
        index = index+1




    