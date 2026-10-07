import numpy as np
cube = dict()
cube["R"] = np.full((3, 3), 'r')
cube["L"] = np.full((3, 3), 'o')
cube["U"] = np.full((3, 3), 'w')
cube["D"] = np.full((3, 3), 'y')
cube["F"] = np.full((3, 3), 'g')
cube["B"] = np.full((3, 3), 'b')
def rotate(self, input):
    axis = input[0:1]
    modifier = ""
    if len(input) > 1:
        modifier = input[1:2]


