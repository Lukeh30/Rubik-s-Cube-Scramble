import numpy as np
faces = ["R", "L", "U", "D", "F", "B"]
colors = ["r", "o", "w", "y", "g", "b",]
rot = {"R": ("FUBD", "rrlr"), "L": ("FDBU", "llrl"), "U": ("RFLB", "tttt"), "D": ("RBLF", "bbbb"), "F": ("URDL", "bltr"), "B": ("ULDR", "tlbr")}
slices = {"t": np.s_[0,:], "b": np.s_[2,::-1], "r": np.s_[:,2], "l": np.s_[::-1,0]}
cube = dict()
for i in range(6):
    cube[faces[i]] = np.full((3, 3), colors[i])

def rotate(input):
    axis = input[:1]
    modifier = {"": 1, "'": 3, "2": 2}[input[1:]]
    cube[axis] = np.rot90(cube[axis], -modifier)
    for _ in range(modifier):
        slicesRef = [cube[rot[axis][0][i]][slices[rot[axis][1][i]]] for i in range(4)]
        saved = [s.copy() for s in slicesRef]
        for i in range(4):
            slicesRef[(i+1)%4][:] = saved[i]

def printCube():
    for i in range(3):
        print((" " * 3 ) + "".join(cube["U"][i,:].astype(str)))
    for i in range(3):
        print("".join(cube["L"][i,:].astype(str)) + "".join(cube["F"][i,:].astype(str)) + "".join(cube["R"][i,:].astype(str)) + "".join(cube["B"][i,:].astype(str)))
    for i in range(3):
        print((" " * 3 ) + "".join(cube["D"][i,:].astype(str)))
