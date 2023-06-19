from skspatial.objects import Plane, Point, Vector
import random 
import numpy as np
import math 
import matplotlib.pyplot as plt

def rand_vec():
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    z = random.uniform(-1.0, 1.0)
    p = Vector.from_points([0, 0, 0], [x, y, z])
    return p.unit()

def rand_ortogonal_base():
    # n1 = rand_vec()
    # n2 = rand_vec()
    # n3 = n1.cross(n2).unit()
    # n2 = n1.cross(n3).unit()

    #return [n1, n2, n3]
    zeros = [0.0, 0.0, 0.0]
    return [
            Vector.from_points(zeros, [ -0.21026414, 0.80410475, 0.55606164 ]),
            Vector.from_points(zeros, [ -0.85618238, -0.4260293, 0.29231963 ]),
            Vector.from_points(zeros, [ -0.47195415, 0.41462584, -0.778039  ])
        ]

def l_points():
    A = [-1, 1]
    return [ Point([x,y,z]) for x in A for y in A for z in A ]

def rand_a_matrix():
    #inv_sqrt_2 = 1.0 / math.sqrt(2.0)
    #return np.random.normal(loc=0.0, scale=inv_sqrt_2, size=(2, 3))

    return np.array([
            [ 0.06159399,  0.42724387,  0.53944334 ],
            [ 0.55385823, -0.01482455, -0.49901313 ]
        ])

if __name__ == "__main__":
    base = rand_ortogonal_base()
    plane = Plane.from_vectors([0, 0, 0], base[0], base[1])
    _, ax = plt.subplots()
    L = l_points()
    for point in L:
        point_proj = plane.project_point(point)
        point_proj.plot_2d(ax)
    plt.savefig("z49_plane.png", dpi=300)
    plt.close()

    A = rand_a_matrix()
    L_proj = []
    _, ax = plt.subplots()
    for point in L:
        point_proj = Point(A.dot(point))
        point_proj.plot_2d(ax)
    plt.savefig("z49_a_matrix.png", dpi=300)
    plt.close()