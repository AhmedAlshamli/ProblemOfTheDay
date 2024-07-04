# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 22:04:50 2024

@author: Ahmed Alshamli

Given a list with the hights of values in a histogram. calculate the area of the largest rectangle in the 
    histogram
"""

def calculate(hights):
    maxArea = 0;
    for i in range(len(hights)):
        for j in range(1,hights[i]+1):
            cols = 1
            for k in range(i+1,len(hights)):
                if hights[k] < j:
                    break
                cols += 1
            
            area = j*cols

            maxArea = max(maxArea, area)
            
    return maxArea


t1 = [2,1,5,6,2,3]
t2 = [8,5,2,6,4,1]


#print(calculate(t1))
print(calculate(t2))

