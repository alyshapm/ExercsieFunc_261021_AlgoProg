def convertToDays(): # (1) user inputs the hours, minutes, and seconds
    h = float(input("Enter no. of hours: "))
    m = float(input("Enter no. of minutes: "))
    s = float(input("Enter no. of seconds: "))
    print("The number of days is", getDays(h,m,s))# (3) returned value from getDays function is printed

def getDays(h, m, s): # (2) the data inputted will then be calculated in this function
    d = (h/24) + (m/1440) + (s/86400) # formula to convert to days
    return round(d, 4) # the new value will be rounded and returned

convertToDays()