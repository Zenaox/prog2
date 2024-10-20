
"""
Solutions to module 4
Review date:
"""

student = "Zena Alomar"
reviewer = ""


import random as r
import matplotlib.pyplot as plt 
import numpy as np

def approximate_pi(n):
    kvad_stor = 2
    r = 1

    dots = np.random.uniform(-1, 1, size=(n, 2)) #hitta slumpmässif punkter inuti cirkel
    distans = (dots[:,0]**2 + dots[:,1]**2)**0.5 #beräkna distansen
    inside = distans <= r #inuti cirkel

    e_area = np.sum(inside)/n*kvad_stor**2 #uppskattad area
    a_area = np.pi * r**2  #riktig area
    plt.figure(figsize=(8, 8))
    plt.scatter(dots[:,0], dots[:,1], 
                c = inside, cmap='plasma', s = 3)
    cirkel = plt.Circle((0,0), r, color ='black', fill=False)
    plt.gca().add_patch(cirkel)
    plt.gca().set_aspect('equal')
    plt.title('Monte Carlo Estimation')
    plt.savefig(f'MC_SIM_{n}.png')
    #plt.show()
    return e_area

    #print(f'Estimates area: {e_area}')
    #print(f'Real area: {a_area}')


def main():
    lst = [1000, 10000, 100000]
    estima_lst = []
    for n in lst:
        pival = approximate_pi(n)
        estima_lst.append(pival)
        print(f"Estimated π with {n} points: {pival}")
        #sorted_estim_lst = sorted(estima_lst)
    return sorted(estima_lst) 
if __name__ == '__main__':
    main()