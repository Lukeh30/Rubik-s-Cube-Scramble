import numpy as np
faces = ["R", "L", "U", "D", "F", "B"]
colors = [f"\033[30;48;5;196mr\033[0m",
          f"\033[30;48;5;208mo\033[0m",
          f"\033[30;48;5;231mw\033[0m",
          f"\033[30;48;5;226my\033[0m",
          f"\033[30;48;5;46mg\033[0m",
          f"\033[30;48;5;33mb\033[0m",]
rot = {"R": ("FUBD", "rrlr"), "L": ("FDBU", "llrl"), "U": ("RFLB", "tttt"), "D": ("RBLF", "bbbb"), "F": ("URDL", "bltr"), "B": ("ULDR", "tlbr")}
slices = {"t": np.s_[0,:], "b": np.s_[2,::-1], "r": np.s_[:,2], "l": np.s_[::-1,0]}
cube = dict()
for i in range(6):
    cube[faces[i]] = np.full((3, 3), colors[i], dtype=object)

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
        print((" " * 4 ) + "".join(cube["U"][i,:].astype(str)) + "\033[0m")
    print()
    for i in range(3):
        print("".join(cube["L"][i,:].astype(str)) + " " + "".join(cube["F"][i,:].astype(str)) +  " " + "".join(cube["R"][i,:].astype(str)) +  " " + "".join(cube["B"][i,:].astype(str)) + "\033[0m")
    print()
    for i in range(3):
        print((" " * 4 ) + "".join(cube["D"][i,:].astype(str)) + "\033[0m")
