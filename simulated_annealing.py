from hill_climbing import * 
import random
import math

TIPOS = [ (1,3), (4,6), (5,7) ]


def probability(state, neighbor, types, t):
    exponent = (-(stateValue(state, types) - stateValue(neighbor, types))) / t
    #print(exponent)
    probability = math.exp(exponent)
    return probability

def simulated_annealing(types, maxsize, numiter, t):
    trivial = hillClimb(TIPOS, 19)
    alpha = random.random()
    state = [0 for i in types]
    for i in range(0, numiter):
        neighbor = getNeighbor(state, types, maxsize)
        if stateValue(neighbor, types) > stateValue(state, types):
            state = neighbor
            if stateValue(state, types) > stateValue(trivial, types):
                trivial = state
        else:
            prob = probability(state, neighbor, types, t)
            aux = prob*100
            if random.randint(0,100) < aux:
                state = neighbor
        t = alpha*t
    return state

if __name__ == "__main__":
    result = simulated_annealing(TIPOS, 19, 100, 100)
    print(stateSize(result, TIPOS))
    print(result)
