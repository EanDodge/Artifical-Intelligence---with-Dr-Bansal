#Ean Dodge
#Algorithm regression_analysis

import random
import numpy as np
import matplotlib.pyplot as plt
DATA_SIZE = 200
def get_data_random():
    result = list()
    for i in range(DATA_SIZE):
        rand1 = random.randint(0,100)
        rand2 = random.randint(0,100)
        result.append((rand1,rand2))
    return result

def regression_analysis(data):
    x_total = 0
    y_total = 0
    for point in data:
        x_total += point[0]
        y_total += point[1]
    x_avg = x_total / len(data)
    y_avg = y_total / len(data)
    sigma_x = 0
    for point in data:
        sigma_x += (point[0] - x_avg)**2
    sigma_x /= len(data)-1
    covariance_xy = 0
    for point in data:
        covariance_xy += (point[0] - x_avg) * (point[1] - y_avg)
    covariance_xy /= len(data)-1

    slope = covariance_xy/sigma_x
    intercept = y_avg - slope * x_avg
    return slope, intercept

def plot(data, slope, intercept):
    x,y = zip(*data)
    fig, ax = plt.subplots()
    ax.scatter(x,y,color='blue',label = 'data')
    x = np.linspace(0, 100, 1000)

    m = slope
    b = intercept
    y = m * x + b

# Plot the line
    ax.plot(x, y, color = 'red', label="f'y = {m}x + {b}'") 
    plt.show()

def predict_dependant(slope,intercept,independent):
    return (slope * independent) + intercept

def main():
    data = get_data_random()
    slope, intercept = regression_analysis(data)
    print("the equation is:", slope,"x +",intercept )
    plot(data, slope, intercept)
    independent = input("what is the independent variable you would like to put in to predict dependent")
    print(predict_dependant(slope,intercept, int(independent)))



if __name__ == "__main__":
    main()


