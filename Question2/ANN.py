import random
import math
import numpy as np

DATA_SIZE = 100
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
    output_vector = list()
    for i in input_vector:
        if(i > threshold_to_fire):
            output_vector.append((1/(1+math.exp(-i)))*7)
        else:
            output_vector.append(0)
    return output_vector

def make_random_matrix(size_of_input, nhidden,phidden, size_of_output):
    trained_matracies = list()
    trained_matracies.append( np.random.uniform(-1,1,size = (phidden, size_of_input)))
    index = 0
    while(index < nhidden):
        trained_matracies.append( np.random.uniform(-1,1,size=(phidden, phidden)))
        index = index+1
    trained_matracies.append( np.random.uniform(-1,1,size = (size_of_output, phidden)))
    return trained_matracies


def calculate_input_vector(training_input, trained_matrix,bias):
    input_vector = list()
    # print(training_input)
    for i in trained_matrix:
        index = 0
        result = 0
        for j in i:
            result += training_input[index] * j
            index = index + 1
        input_vector.append(result+bias)
    return input_vector

def weight_change(target, output, learning_rate, previous_input ):
    return (learning_rate)* (target - output) * previous_input


def feed_forward_neural_network(size_of_input, size_of_output, training_input,training_output, threshold_to_fire,
                                phidden, nhidden, bias, maxcycle, tadj, learning_rate, data_index, trained_matracies):
    
    #make random matricies of weights
    #for i in trained_matracies:
        #print (i)
        #print()

    input_vector = list()
    input_vector = calculate_input_vector(training_input, trained_matracies[0],bias)
    #print(input_vector)
    output_vector = threshold_fire(input_vector, threshold_to_fire)
    #print(output_vector)
    #print()
    for i in range(nhidden):
        input_vector = calculate_input_vector(output_vector, trained_matracies[i+1],bias)
        #print(input_vector)
        output_vector = threshold_fire(input_vector, threshold_to_fire)
        #print(output_vector)
        #print()
    old_input = output_vector
    input_vector = calculate_input_vector(output_vector, trained_matracies[nhidden+1],bias)
    #print(input_vector)
    output_vector = threshold_fire(input_vector, threshold_to_fire)
    #print(output_vector)
    #print()

    #print(training_output[0])
    #print(trained_matracies[nhidden+1])
    for i in trained_matracies[nhidden+1]:
        index = 0
        input_index = 0
        for j in i:
            #print(len(input_vector), input_index)
            change_in_weight = weight_change(training_output[index], output_vector[index],learning_rate, old_input[input_index])
            #print ("Initial is: ", j, "+ weight change(", change_in_weight, ") is: ")
            j += change_in_weight
            #print(j)
            input_index+=1
        index += 1
    error = get_error(training_output, output_vector)
    print("ERROR ", data_index, error)
    if(error < tadj):
        print("Network is done, error is low")
        #exit()
    return trained_matracies
            
def get_error(target, output):
    result = 0
    for i in range(len(target)):
        difference = target[i]-output[i]
        #print("difference ",difference)
        result += difference**2
        #print("result ", result)
    result = math.sqrt(result)
    #print("after sqrt", result)
    return result

# Main function
def main():

    size_of_input =  int(input("size of your input vector: "))
    size_of_output = int(input("size of your output vector: "))
    threshold_to_fire = int(input("what is your threshold to fire: "))
    phidden = int(input("Give number of perceptrons in each hidden layer: "))
    nhidden = int(input("Give the number of hidden layers: "))
    bias = float(input("Give the perceptron bias: "))
    maxcycle = int(input("Give cycles to be repeated: "))
    tadj = int(input("Give the threshold for neural network adjustment: "))
    learning_rate = float(input("Give the learning rate: "))
    # size_of_input = 4 # int(input("size of your input vector: "))
    # size_of_output = 3#int(input("size of your output vector: "))
    # threshold_to_fire = -1#int(input("what is your threshold to fire: "))
    # phidden = 3#int(input("Give number of perceptrons in each hidden layer: "))
    # nhidden = 3#int(input("Give the number of hidden layers: "))
    # bias = 0#float(input("Give the perceptron bias: "))
    # maxcycle = 0#int(input("Give cycles to be repeated: "))
    # tadj = 3#int(input("Give the threshold for neural network adjustment: "))
    # learning_rate = .01#float(input("Give the learning rate: "))
    training_pairs = generate_data(size_of_input,size_of_output)
    training_input  = [i[0] for i in training_pairs]
    training_output = [i[1] for i in training_pairs]
    trained_matracies = make_random_matrix(size_of_input,nhidden,phidden,size_of_output)

    for i in range(DATA_SIZE):
        trained_matracies = feed_forward_neural_network(size_of_input, size_of_output, training_input[i],training_output[i], threshold_to_fire,
                                phidden, nhidden, bias, maxcycle, tadj, learning_rate,i,trained_matracies)
if __name__ == "__main__":
    main()