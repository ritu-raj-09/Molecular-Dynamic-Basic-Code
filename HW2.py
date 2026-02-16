#1. Assume 121 atoms are laid out 11 by 11 evenly in a 2-D grid (see below for an example). The closest distance between adjacent atoms is 1, thus the box length is 10. Write a python program to compute all the pairwise distances and the average.




import numpy as np
import matplotlib.pyplot as plt
atoms_n=int(input("Enter the Gird Size if its 11X11 enter 11: "))
points = []
for i in range(atoms_n):        # x
    for j in range(atoms_n):    # y
        points.append((i, j))

distances = []
for a in range(len(points)):
    for b in range(a+1, len(points)):  
        dx = points[a][0] - points[b][0]
        dy = points[a][1] - points[b][1]
        d = ((dx*dx + dy*dy))**0.5
        distances.append(d)

print(distances)

print("Number of pairwise distances:", len(distances))
print("Average distance:", np.mean(distances))

# JUST FOR FUN
points=np.array(points)
plt.figure(figsize=(6,6))
plt.scatter(points[:,0], points[:,1], color='red')
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
