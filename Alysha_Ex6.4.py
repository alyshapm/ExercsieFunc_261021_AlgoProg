def calcNewHeight():
    currentWidth = eval(input("Enter the current width of the image: ")) # input prompt
    currentHeight = eval(input("Enter the current height of the image: "))
    newWidth = eval(input("Enter desired width: "))
    newHeight = newWidth * currentHeight / currentWidth # formula to find the new height, by using the concept of proportions/ratio (cross-multiplication) and / is used to give a float value
    return newHeight 

print(f"The corresponding height is {calcNewHeight()}.")