"""Includes functions from exercise-4 part 1 and 2
Includes 2 functions
1.Converts Fahrenheit to Celsius
2. Reclassifies temperatures in Celsius to integer classes 0-3"""

#1. Defining a function that converts Fahrenheit to Celsius.

def fahr_to_celsius(temp_fahrenheit):
    """converts Fahrenheit to Celsius"""
    
    #Converts with the provided formula
    converted_temp = (temp_fahrenheit - 32) / 1.8
    
    #Returns the variable converted_temp in Celsius
    return converted_temp




"""2. Function that reclassifies temperatures to integer classes 0-3"""

#Function that takes in temperatures in Celsius and reclassifies them
def temp_classifier(temp_celsius):
    """The reclassification for temp_celsius goes as follows:
    Temperatures below -2 degrees Celsius == 0
    Temperatures equal or warmer than -2, but less than +2 degrees Celsius == 1
    Temperatures equal or warmer than +2, but less than +15 degrees Celsius == 2
    Temperatures equal or warmer than +15 degrees Celsius == 3
    
    Parameters:
    temp_celsius only accepts temperatures in Celsius
    
    Return value:
    A reclassified integer value 0-3 depending from the temperature"""
    
    if temp_celsius < -2:
        temp_celsius = 0
    elif (temp_celsius >= -2) and (temp_celsius < 2):
        temp_celsius = 1
    elif (temp_celsius >= 2) and (temp_celsius < 15):
        temp_celsius = 2
    elif temp_celsius >= 15:
        temp_celsius = 3
    return temp_celsius