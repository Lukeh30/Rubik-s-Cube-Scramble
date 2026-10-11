import scramble as Sc
import cube as cube

def toString(array):
    finalStr = ""
    for i in array:
        finalStr = finalStr + i + " "
    return finalStr

scram = Sc.scrambleCube(20)
print("Have green as front face and white as top face.")
print(toString(scram))
for i in range(len(scram)):
    cube.rotate(scram[i])
cube.printCube()

