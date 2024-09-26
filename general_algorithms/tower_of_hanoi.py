def towersOfHanoi(n, firstRod, secondRod, thirdRod):
    if n == 0:
        return
    towersOfHanoi(n - 1, firstRod, thirdRod, secondRod)
    print("disk ", n," moved from ", firstRod, " to ", secondRod)
    towersOfHanoi(n - 1, thirdRod, secondRod, firstRod)