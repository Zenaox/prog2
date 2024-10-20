
"""
Solutions to module 4
Review date:
"""

student = "Zena Alomar"
reviewer = ""

import math 
import random as r
import numpy as np

def sphere_volume(n, d): 
    r = 1 #radie = 1
    punkter_inne = 0 #antal punkter inuti hypersaken
    for i in range(n): #en forloop genom alla slumpmässig punkter som är genererat (n)
        punkter = [np.random.uniform(-r,r) for _ in range(d)] #generar en punkt med korrdinaterna [-r,r]
        punkter_hyper= list(map(lambda x: x**2, punkter))  #given formel, beräknar om punkten är inuti hypersfären
        if (sum(punkter_hyper)) <= r**2:
            punkter_inne += 1
    #return points_inside

    kub_volym=  (2*r)**d #kubens volym
    hypersfar_uppskatt_volym = punkter_inne/n #förhållandet antal punkter inuti ggr kubens volym
    return (hypersfar_uppskatt_volym * kub_volym)  #approx volym av hypersfären
    #pass

def hypersphere_exact(n, d, r=1): 
    return (r**d)*math.pi**(d/2)/math.gamma(d/2 + 1) #given formel för exakt volym

if __name__ == '__main__':
    #start = pc()
    volym = sphere_volume(100000, 11)
    #print(f" volym of sphere is {volym} units")
    #end = pc()
    n = 100000
    d = 2
    #d = 11
    estimated_volume = sphere_volume(n, d)
    actual_volume= hypersphere_exact(n, d, r=1)
    print(f'Approx volume for {d}-dimensional hypersphere: {estimated_volume}')
    print(f'Actual volume for {d}-dimensional hypersphere: {actual_volume}')