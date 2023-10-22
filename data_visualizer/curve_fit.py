# ECOR 1042 Lab 6 - Individual submission for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "George Resendes-Awada"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101277596"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-037"

#==========================================#
# Place your curve_fit function after this line

import matplotlib as plt

import numpy as np 

from scipy.optimize import curve_fit



def curve_fit(data:list, attr:str, degree:int)->list:
    """
    Returns the equation of the best fit as a list of coefficients.
    Takes three arguments, data given as a dictionary, attribute given as a
    string and degree given as a integer.
    
    Precondition: attribute must have a numeric value therefore "School" is 
    not valid, dictionary inputs are; school, health, age, failures.
    
    >>>curve_fit([{'Age' : 19, 'G_Avg' : 6},{'Age' : 20, 'G_Avg' : 4}, {'Age' : 20, 'G_Avg' : 7}], 'Age', 1)
    'y=-0.4999999999999912x + 15.499999999999817'
    
    >>>curve_fit([{'Health' : 3, 'G_Avg' : 7},{'Health' : 4, 'G_Avg' : 2}, {'Health' : 2, 'G_Avg' : 8}], 'Health', 2)
    'y=-1.9999999999999996x^2 + 9.000000000000037x + -2.0000000000001186'
    """

    avg_attr = {}
    for value in range(len(data)):
        if data[value][attr] not in avg_attr:
            avg_attr[data[value][attr]] = [data[value]['G_Avg']]
        else:
            avg_attr[data[value][attr]] += [data[value]['G_Avg']]
            
    x = []
    y = []
    
    for item in avg_attr:
        x +=[item]
        mean = sum(avg_attr[item])
        n = len(avg_attr[item])
        y += [mean/n]
    
    coefficient = []
    eqp1 = 'y='
    if len(x) > degree:
        coefficient += [np.polyfit(x,y,degree)]
        degree = degree
        i = 0
    
        while degree >= 0:
            old_coef = coefficient[0][i]
            i+=1
            if degree > 1:
                eqp1 += f'{old_coef}x^{degree} + '
            elif degree == 1:
                eqp1 += f'{old_coef}x + '
            else:
                eqp1 += f'{old_coef}'
            degree -= 1
    elif len(x) <= degree:
       
        coefficient += [np.polyfit(x,y, (len(x)-1))]
        
        deg = (len(x)-1)
        i = 0
        
        while deg >= 0:
            old_coef = coefficient[0][i]
            i += 1
            if deg > 1:
                eqp1 += f'{old_coef}x^{deg} + '
            elif deg == 1:
                eqp1 += f'{old_coef}x + '
            else:
                eqp1 += f'{old_coef}'
            deg -= 1
    return eqp1

# Do NOT include a main script in your submission

