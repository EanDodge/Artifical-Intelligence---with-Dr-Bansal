import random
import math
DATA_SIZE = 200
def get_data():
    result = list()
    for i in range(DATA_SIZE):
        rand1 = random.randint(0,100)
        rand2 = random.randint(0,100)
        result.append((rand1,rand2))
    return result

def distance(one, two):
    return (math.sqrt((one[0] - two[0])**2 + (one[1] - two[1])**2))



def points_in_marcoblocks(data, low_x, low_y, high_x, high_y):
    num_of_macro = 0
    for point in data:
        if ((point[0] >= low_x) and (point[0]< high_x) 
            and (point[1] >= low_y) and (point[1] < high_y )):
            num_of_macro += 1
    return num_of_macro

def generate_seed(data, number_of_centriods):
    set_x = [i[0] for i in data]
    set_y = [i[1] for i in data]
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
            low_y = min_x + (j*size_x)
            high_y = low_y + size_y
            mid_y = (low_y + high_y)/2
            num_of_points = points_in_marcoblocks(data, low_x, low_y, high_x, high_y)
            print(num_of_points, avr_density)
            if (num_of_points > avr_density-(avr_density/6)):
                high_density.append((mid_x , mid_y))
    final_seeds = list()
#     next_seed = randomly_select(Shigher); % randomly select one of the seed points
# Sseed = Sseed + next_seed; % put the seed point in the set of selected seeds Sseed
# Shigher = Shigher – next_seed;} % remove the selected seed from the set Shighe
    print(high_density)
    indicies = random.sample(range(0, len(high_density)-1), number_of_centriods)

    for i in range(number_of_centriods):
        next_seed = high_density[indicies[i]]
        final_seeds.append(next_seed)
        #high_density.remove(high_density[indicies[i]])
    radius = (min(size_x,size_y)) / number_of_centriods
    for i in range(number_of_centriods):
        ith_seed = final_seeds[i]
        for j in range(number_of_centriods):
            if ( i != j):
                jth_seed = final_seeds[j]
                distance = distance(ith_seed,jth_seed)
                if (distance < 2*radius): radius = distance / 2
    return (final_seeds, radius)

def kmeans(data, number_of_centriods, max_iterations, max_shift):
    seed_points, radius = generate_seed(data, number_of_centriods)
    clusters = list(list())
    count = 1
    stable = False
    while((count < max_iterations) and not(stable)):
        outliers = data
        for i in range(number_of_centriods):
            for j in range(DATA_SIZE):
                distance = distance(seed_points[i],data[j])
                if(distance < radius):
                    clusters[i].append(data[j])
                    outliers.remove(data[j])
            new_cluster_x = 0
            new_cluster_y = 0
            for point in data:
                new_cluster_x += point[0]
                new_cluster_y += point[1]
            new_cluster_x /= len(clusters[i])
            new_cluster_y /= len(clusters[i])




def main():
    data = get_data()
    generate_seed(data, 3)
    print(data)


if __name__ == "__main__":
    main()

