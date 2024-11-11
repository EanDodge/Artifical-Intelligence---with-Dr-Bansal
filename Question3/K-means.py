import random
import math
import matplotlib.pyplot as plt
DATA_SIZE = 250
def get_data():
    result = list()
    for i in range(DATA_SIZE):
        rand1 = random.randint(0,100)
        rand2 = random.randint(0,100)
        result.append((rand1,rand2))
    return result

def distance_of_points(one, two):
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
    print(high_density)
    indicies = random.sample(range(0, len(high_density)-1), number_of_centriods)

    for i in range(number_of_centriods):
        next_seed = high_density[indicies[i]]
        final_seeds.append(next_seed)
        #high_density.remove(high_density[indicies[i]])
    radius = ((min(size_x,size_y)) / number_of_centriods)+(DATA_SIZE / 100)
    for i in range(number_of_centriods):
        ith_seed = final_seeds[i]
        for j in range(number_of_centriods):
            if ( i != j):
                jth_seed = final_seeds[j]
                distance = distance_of_points(ith_seed,jth_seed)
                if (distance < 2*radius): 
                    radius = distance / 2
                    print("in here")
    return (final_seeds, radius)

def kmeans(data, number_of_centriods, max_iterations, max_shift):
    seed_points, radius = generate_seed(data, number_of_centriods)
    count = 1
    stable = False
    while((count < max_iterations) and not(stable)):
        outliers = list(data)
        clusters = [[] for i in range(number_of_centriods)]
        for i in range(number_of_centriods):
            for point in data:
                distance = distance_of_points(seed_points[i],point)
                if(distance < radius):
                    clusters[i].append(point)
                    outliers.remove(point)
            new_centriod_x = 0
            new_centriod_y = 0
            for point1 in clusters[i]:
                new_centriod_x += point1[0]
                new_centriod_y += point1[1]
            if (len(clusters[i])>0):
                new_centriod_x /= len(clusters[i])
                new_centriod_y /= len(clusters[i])
                new_centriod = (new_centriod_x,new_centriod_y)
                seed_points[i] = new_centriod
                print ("cluster #", i, "new centroid:", (new_centriod_x, new_centriod_y))
            else:
                new_centriod = seed_points[i]
                new_centriod_x = new_centriod[0]
                new_centriod_y = new_centriod[1]
                print ("cluster #", i, "new centroid:", (new_centriod_x, new_centriod_y))
        #print("Current outliers", outliers); 
        stable = True
        #print(len(seed_points), len(new_clusters), number_of_centriods)
        for i in range(number_of_centriods - 1):
            shift = distance_of_points(seed_points[i], new_centriod)
            if ( shift > max_shift): stable = False
        count = count + 1
    print("Final Centroids")
    for seed in seed_points:
        print(seed)
    print("Final Clusters")
    cluster_count=1
    for clust in clusters:
        print("#",cluster_count )
        for i in clust:
            print(i)
        cluster_count+=1
    print("Final Outliers")
    for outlier in outliers:
        print(outlier)
    return clusters, seed_points, radius

def test_final(clusters, centriods, radius):
    count = 0
    #print(radius)
    for cluster in clusters:
        for point in cluster:
            distance = distance_of_points(point, centriods[count])
            #print("cluster#", count, " point ", point, "distance, ", distance)
            if(distance > radius):
                #print("in here")
                cluster.remove(point)
        count +=1

def plot(data, centriods, my_radius,clusters):
    x,y = zip(*data)
    fig, ax = plt.subplots()
    ax.scatter(x,y,color='blue',label = 'data')

    for cluster in clusters:
        if(len(cluster)>1):
            x,y = zip(*cluster)
            ax.scatter(x,y,color='red',label = 'data')
        else:
            print("cluster did not have any items")

    count = 1
    for point in centriods:
        circle1 = plt.Circle(point, radius=my_radius, color='red', fill=False)
        ax.add_artist(circle1)
        ax.text(point[0],point[1]+10,str(count),fontsize=20, ha='center', va='center', color='red')
        count += 1
    plt.show()





def main():
    data = get_data()
    number_of_centriods = input("How many centriods would u like?")
    max_iterations = input("Max interarions of the algorithm?")
    max_shift = input("At what shift are the clusters stable?")
    #generate_seed(data, 3)
    clusters, centriods,radius = kmeans(data,int(number_of_centriods),int(max_iterations),int(max_shift))
    test_final(clusters, centriods, radius)
    #print(data)
    plot(data, centriods, radius, clusters)


if __name__ == "__main__":
    main()

