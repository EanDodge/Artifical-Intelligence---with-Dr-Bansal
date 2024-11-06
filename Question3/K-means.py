import random
DATA_SIZE = 100
def get_data():
    result = list()
    for i in range(DATA_SIZE):
        rand1 = random.randint(0,100)
        rand2 = random.randint(0,100)
        result.append((rand1,rand2))
    return result

def points_in_marcoblocks(data, low_x, low_y, high_x, high_y):
    num_of_macro = 0
    for point in data:
        if ((point[0] >= low_x) and (point[0]< high_x) 
            and (point[1] >= low_y) and (point[1] < high_y )):
            num_of_macro += 1
    return num_of_macro

def generate_seed(data, number_of_centriods):
    set_x = [data[0] for i in data]
    set_y = [data[1] for i in data]
    max_x,min_x = max(set_x), min(set_x)
    max_y,min_y = max(set_y), min(set_y)
    size_x = (max_x - min_x)/number_of_centriods
    size_y = (max_y - min_y)/number_of_centriods
    macro_num = number_of_centriods ** 2
    avr_density = DATA_SIZE / macro_num
    high_density = list()
    for i in range(number_of_centriods):
        low_x = min_x + (i*size_x)
        high_x = low_x + size_x
        mid_x = (low_x + high_x)/2
        for j in range(number_of_centriods):
            low_y = min_x + (i*size_x)
            high_y = low_y + size_y
            mid_y = (low_y + high_y)/2
            num_of_points = points_in_marcoblocks(data, low_x, low_y, high_x, high_y)
            if (num_of_points > avr_density):
                high_density = high_density + (mid_x , mid_y)




def main():
    data = get_data()
    print(data)


if __name__ == "__main__":
    main()

