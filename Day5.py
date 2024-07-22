# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 16:13:42 2024

@author: Ahmed Alshamli

given a list of buildings each has [left,right,hight]
print out the points where the hight changes in the line.
"""

def solve(buildings):
    points = []
    
    end = buildings[-1][-2]
    xline = [0]*(end+1)
    for building in buildings:
        left = building[0]
        right = building[1]
        hight = building[2]
        xline[left:right] = [max(xline[i],hight) for i in range(left,right)]
        
    prev = 0
    for i in range(end+1):
        if prev != xline[i]:
            points.append([i,xline[i]])
            prev = xline[i]
            
    return points
    
test = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
test2 = [[0,2,3],[2,5,3]]
print("test 1",solve(test))
print("test 2",solve(test2))