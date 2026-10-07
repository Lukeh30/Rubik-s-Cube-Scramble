import scramble as Sc
import cube as cube
def toString(array):
    finalStr = ""
    for i in array:
        finalStr = finalStr + i + " "
    return finalStr
def block(color, length):
    print(f"\033[{color}m{' ' * length}\033[0m")
print("Have green as front face and white as top face.")
scram = Sc.scrambleCube(20)
#print(scram)
print(toString(scram))
cube.rotate("R")
cube.printCube()
"""
for i in range(3):   
    print(f"\033[48;5;0m{' ' * 3}\033[0m\033[48;5;15m{" " * 3}\033[0m\033[48;5;0m{" " * 3}\033[0m\033[48;5;0m{" " * 3}\033[0m")
for i in range(3):   
    print(f"\033[48;5;208m{' ' * 3}\033[0m\033[48;5;46m{" " * 3}\033[0m\033[48;5;196m{" " * 3}\033[0m\033[48;5;21m{" " * 3}\033[0m")
for i in range(3):   
    print(f"\033[48;5;0m{' ' * 3}\033[0m\033[48;5;226m{" " * 3}\033[0m\033[48;5;0m{" " * 3}\033[0m\033[48;5;0m{" " * 3}\033[0m")
"""
