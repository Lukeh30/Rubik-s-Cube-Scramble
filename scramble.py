import random
def scrambleCube(moves):
    faces = ["R", "L", "U", "D", "F", "B"]
    modifiers = ["", "'", "2"]
    scramble = []
    for i in range(moves):
        face = random.choice(faces)
        modifier = random.choice(modifiers)
        move = face + modifier
        scramble.append(move)
    return scramble
