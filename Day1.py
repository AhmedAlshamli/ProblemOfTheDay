# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1  2024

@author: Ahmed Alshamli


Given 2 integers black and white representing the count of colored
    balls used to preform a triangle. Return the maximum hight of the
    triangle if adjacent rows can not have the same color and 
    each row contains balls of the same color.
"""

w = 34
b = 49

def solve(x,y):
    counter = 0
    while True:
        if x < counter+1:
            break
        x -= counter+1
        counter += 1
        if y < counter+1:
            break
        y -= counter+1
        counter += 1
    return counter
        

print(max(solve(b,w),solve(w,b)))
