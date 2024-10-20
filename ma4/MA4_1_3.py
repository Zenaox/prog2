
"""
Solutions to module 4
Review date:
"""

student = "Zena Alomar"
reviewer = ""

import math
import random as r
import numpy 
import matplotlib.pyplot as plt
import concurrent.futures
from time import sleep as pause
from time import perf_counter as pc


def sphere_volume(n, d): 
    r = 1 #radie = 1
    punkter_inne = 0 #antal punkter inuti hypersaken
    for i in range(n): #en forloop genom alla slumpmässig punkter som är genererat (n)
        punkter = [numpy.random.uniform(-r,r) for _ in range(d)] #generar en punkt med korrdinaterna [-r,r]
        punkter_hyper= list(map(lambda x: x**2, punkter))  #given formel, beräknar om punkten är inuti hypersfären
        if (sum(punkter_hyper)) <= r**2:
            punkter_inne += 1
    #return points_inside

    kub_volym=  (2*r)**d #kubens volym
    hypersfar_uppskatt_volym = punkter_inne/n #förhållandet antal punkter inuti ggr kubens volym
    return (hypersfar_uppskatt_volym * kub_volym)  #approx volym av hypersfären 

def hypersphere_exact(n,d):
    return (r**d)*math.pi**(d/2)/math.gamma(d/2 + 1) #given formel för exakt volym


# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
     #using multiprocessor to perform 10 iterations of volume function  
    with concurrent.futures.ProcessPoolExecutor() as ex:
        all_points = list(ex.map(sphere_volume, [n]*np, [d]*np))
    return sum(all_points)/len(all_points)

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
    #using multiprocessor to perform 10 iterations of volume function  
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as ex:
        all_points = list(ex.map(sphere_volume, [n // np]*np, [d]*np))
    return sum(all_points)/len(all_points)
 

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    start_time = pc()
    n = 100000
    d = 11

    for y in range (10):
        regular_volume = sphere_volume(n,d)
    finish_time = pc()
    print(f'The calculated volume is {regular_volume} units')
    print(f'The time it took to calculate the volume was {finish_time-start_time} seconds ')
    
    #First parallelized volume 
    start_parallelized1_time = pc()
    n = 100000
    d = 11
    np = 5

    First_parallelized_volume = sphere_volume_parallel1(n,d,np)
    
    finish_parallelized1_time = pc()
    print(f'The calculated parallelized volume is {First_parallelized_volume} units')
    print(f'The time it takes to calculate the parallelized volume was {finish_parallelized1_time-start_parallelized1_time} seconds ')

    #First parallelized volume 
    start_parallelized2_time = pc()
    n = 100000
    d = 11
    np = 5

    second_parallelized_volume = sphere_volume_parallel2(n,d,np)
    
    finish_parallelized2_time = pc()
    print(f'The calculated parallelized volume is {second_parallelized_volume} units')
    print(f'The time it took to calculate the parallelized volume was {finish_parallelized2_time-start_parallelized2_time} seconds ')


if __name__ == '__main__':
	main()
