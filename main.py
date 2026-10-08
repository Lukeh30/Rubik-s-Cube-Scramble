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

