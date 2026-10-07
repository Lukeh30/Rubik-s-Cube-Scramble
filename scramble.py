import random
def scrambleCube(moves):
    faces = ["R", "L", "U", "D", "F", "B"]
    modifiers = ["", "'", "2"]
    finalScramble = []
    while len(finalScramble) < 20:
        face = random.choice(faces)
        if len(finalScramble) == 0:    
            modifier = random.choice(modifiers)
            move = face + modifier
            finalScramble.append(move)
        elif len(finalScramble) == 1:
            if face != finalScramble[len(finalScramble)-1][0:1]:
                modifier = random.choice(modifiers)
                move = face + modifier
                finalScramble.append(move)
        elif len(finalScramble) > 1:
            if face == finalScramble[len(finalScramble)-2][0:1]: 
                if finalScramble[len(finalScramble)-1][0:1] != faces[(-2 * (faces.index(face)%2)) + 1 + faces.index(face)]:
                    if face != finalScramble[len(finalScramble)-1][0:1]:
                        modifier = random.choice(modifiers)
                        move = face + modifier
                        finalScramble.append(move)
            elif face != finalScramble[len(finalScramble)-1][0:1]:
                modifier = random.choice(modifiers)
                move = face + modifier
                finalScramble.append(move)
    return finalScramble
