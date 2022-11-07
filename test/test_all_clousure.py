import random
from time import sleep


def simulateUp(current, boardSize):
    result = simulate(current.copy(), 0, boardSize, 1, boardSize, boardSize, 1)
    return result


def simulateDown(current, boardSize):
    result = simulate(current.copy(), boardSize * (boardSize - 1), boardSize ** 2, 1, -1 * boardSize, boardSize, -1)
    return result


def simulateLeft(current, boardSize):
    result = simulate(current.copy(), 0, boardSize * (boardSize - 1) + 1, boardSize, 1, boardSize, 1)
    return result


def simulateRight(current, boardSize):
    result = simulate(current.copy(), boardSize - 1, boardSize ** 2, boardSize, -1, boardSize, -1)
    return result


def simulate(current_entry, initial, end, increment, shift, boardSize, direction):
    current = current_entry.copy()
    availableCells = []
    totalMerged = 0

    for o in range(0, 3):
        for i in range(initial, end, increment):
            for j in range(i + shift, (i + shift * (boardSize - 1)) + direction, shift):
                tmp = j
                summed = False

                for n in range(j - shift, i - direction, -1 * shift):
                    if o % 2 == 0:
                        if current[n] == 0 and current[tmp] != 0:
                            current[n] = current[tmp]
                            current[tmp] = 0

                        tmp = n

                    else:
                        if current[j - shift] == current[j] and not summed:
                            current[j - shift] *= 2
                            totalMerged += current[j - shift]
                            current[j] = 0
                            summed = True

    if not isEquals(current, current_entry):
        for i in range(0, len(current)):
            if current[i] == 0:
                availableCells.append(i)
        if len(availableCells):
            current[random.choice(availableCells)] = random.choice([2, 2, 2, 4])  # AdversarialMove(2: 75%; 4: 25%)

    retorno = [current.copy(), totalMerged]
    return retorno


def isEquals(current1, current2):
    if len(current1) != len(current2):
        return False

    for i in range(0, len(current1)):
        if current1[i] != current2[i]:
            return False

    return True


def hasPossibleMoves(current, boardSize):
    movesSimulated = [simulateUp(current, boardSize)[0], simulateLeft(current, boardSize)[0],
                      simulateDown(current, boardSize)[0], simulateRight(current, boardSize)[0]]

    for i in range(0, len(movesSimulated)):
        for j in range(0, len(movesSimulated[i])):
            if (movesSimulated[i])[j] != current[j]:
                return True

    return False


def firstStep(step, current, boardSize, depth):
    steps = ["UP", "DOWN", "LEFT", "RIGHT"]
    result = []
    merged = 0
    currentSimulated = current.copy()
    stepSimulated = step

    for o in range(0, depth):
        if stepSimulated == "UP":
            result = simulateUp(current, boardSize)

        elif stepSimulated == "DOWN":
            result = simulateDown(current, boardSize)

        elif stepSimulated == "LEFT":
            result = simulateLeft(current, boardSize)

        elif stepSimulated == "RIGHT":
            result = simulateRight(current, boardSize)

        if (o == 0 and isEquals(current, result[0])) or not hasPossibleMoves(current, boardSize):
            return -8000

        currentSimulated = result[0]
        merged += result[1]

        stepSimulated = random.choice(steps)

    return merged


def resultSteps(current, depth, width, boardSize):
    resultUp = 0
    resultDown = 0
    resultLeft = 0
    resultRight = 0

    for o in range(0, width):
        resultUp += firstStep("UP", current, boardSize, depth)
        resultDown += firstStep("DOWN", current, boardSize, depth)
        resultLeft += firstStep("LEFT", current, boardSize, depth)
        resultRight += firstStep("RIGHT", current, boardSize, depth)

    return [resultUp, resultDown, resultLeft, resultRight]


def move(direction, current, boardSize):
    if direction == 1:
        current = simulateUp(current, boardSize)

    elif direction == 2:
        current = simulateDown(current, boardSize)

    elif direction == 3:
        current = simulateLeft(current, boardSize)

    elif direction == 4:
        current = simulateRight(current, boardSize)

    return current[0]


def play(current, depth, width, boardSize):
    values = resultSteps(current, depth, width, boardSize)
    maxi = max(values)

    current = move(values.index(maxi) + 1, current, boardSize)
    print(current)
    print(values)

    if sum(values) != -3200000:
        play(current, depth, width, boardSize)

    else:
        print("Endgame...")


if __name__ == "__main__":
    play([0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0], 4, 100, 4)
