def numAtoms(sampleWeight, atomicWeight=196.67): # optional argument assigned with default value of 196.67
    mole = sampleWeight / atomicWeight # formula for mole, or the amount of substance
    avogrado = 6.022 * pow(10, 23) # Avogrado's constant
    totalAtoms = mole * avogrado # forumla to find total number of atom in the sample using mole and avogrado
    return totalAtoms

newWeight = numAtoms(10, 12.001) # weight of sample is 10, and the atomic weight of carbon is 12.001
print(newWeight) 