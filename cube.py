import numpy as np
faces = ["R", "L", "U", "D", "F", "B"]
colors = ["r", "o", "w", "y", "g", "b",]
cube = dict()
rot = {"R": "FUBD", "L": "FDBU", "U": "RFLB", "D": "RBLF", "F": "URDL", "B": "ULDR"}
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
    temp = rot[axis][0:1]
    print(temp)

def printCube():
    for i in range(3):
        print((" " * 3 ) + "".join(cube["U"][i,:].astype(str)))
    for i in range(3):
        print("".join(cube["L"][i,:].astype(str)) + "".join(cube["F"][i,:].astype(str)) + "".join(cube["R"][i,:].astype(str)) + "".join(cube["B"][i,:].astype(str)))
    for i in range(3):
        print((" " * 3 ) + "".join(cube["D"][i,:].astype(str)))
