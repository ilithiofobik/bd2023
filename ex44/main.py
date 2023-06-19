import random as rand
import math
import matplotlib.pyplot as plt
from skspatial.objects import Point

def getDists(n, k):
    points = [Point([rand.random() for _ in range(n)]) for _ in range(k)]
    dists = []

    for i in range(k - 1):
        for j in range(i + 1, k):
            dists.append(points[i].distance_point(points[j])  / math.sqrt(n))

    return dists
    
if __name__ == "__main__":
    ns = [ 1, 10, 100, 1000, 10000 ]
    k = 100

    for n in ns:
        plt.hist(getDists(n,k), bins=100)
        plt.savefig('z44_n={}.png'.format(n), dpi=300)
        plt.xlabel('Dist')
        plt.ylabel('Frequency')
        plt.title('n = {}'.format(n))
        plt.close()