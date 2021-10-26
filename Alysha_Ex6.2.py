# non-interactive
def calcWeightOnPlanet(weight, surfaceGravity=23.1): # the function takes two arguments, where surfaceGravity is optional and is assigned with default value of 23.1
    return (weight / 9.8) * surfaceGravity # formula of the new weight

newWeight = calcWeightOnPlanet(120, 23.1) #120 is the weight on earth and 23.1 is the surface gravity of the planet
print(newWeight) #the result should yield 282.85714285714283, same if the value of 23.1 is opted out
#%%
# interactive
def calcWeightOnPlanet(weight, surfaceGravity): # here, I did not assign a default value because I'm not sure how to do it, so I substituted with an if else statement
    mass = weight/9.8 
    if surfaceGravity == 0: # when the user inputs 0, the formula will us 23.1 as surfaceGravity
        weight2 = mass * 23.1
    else:
        weight2 = mass * surfaceGravity # otherwise, the formula will use the value of surfaceGravity inputted
    return weight2


weight = eval(input("Enter your weight, in kg: ")) # promts user to input the weight
surfaceGravity = eval(input("Enter the surface gravity of the planet, in m/s2 (optional; enter 0 to use default value): ")) # promts user to input the surface gravity, with the optional choice
print(f"Your weight will be {calcWeightOnPlanet(weight, surfaceGravity)}.") # prints return value from the calcWeightOnPlanet function
#%%