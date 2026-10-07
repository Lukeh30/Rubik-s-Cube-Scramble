import numpy as np
faces = {"R", "L", "U", "D", "F", "B",}
colors = {"r", "o", "w", "y", "g", "b",}
cube = dict()
for i in range(6):
    cube[faces[i]] = np.full((3, 3), colors[i])

def rotate(input):
    axis = input[0:1]
    modifier = -1
    if len(input) > 1:
        if input[1:2] == "'":
            modifier = 1
        elif input[1:2] == "2":
            modifier = -2
    np.rot90(cube[axis], k=modifier)


