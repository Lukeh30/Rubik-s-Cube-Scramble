import scramble as Sc
def toString(array):
    finalStr = ""
    for i in array:
        finalStr = finalStr + i + " "
    return finalStr
print(toString(Sc.scrambleCube(20)))
