# this code took me about 3 hours and 5 breakdowns to make, some parts still doesn't make sense to me but it works overall. 

def covertToCelsius(fahrenheit): # function to covert fahrenheit to celsius
    celcius = (fahrenheit - 32) * (5/9)
    return celcius

def convertToKelvin(fahrenheit): # function to convert celsius to kelvin
    kelvin = covertToCelsius(fahrenheit) + 273.15 # here i used the convertToCelsius function that returns celsius
    return kelvin

def convertTemp(): # the function that displays the converted temperatures 
    fahrenheit = eval(input("Enter a temperature in fahrenheit: ")) 
    print("The temperature in Fahrenheit is:", fahrenheit)
    print("The temperature in Celsius is:", covertToCelsius(fahrenheit))
    print("The temperature in Kelvin is:", convertToKelvin(fahrenheit))

convertTemp()