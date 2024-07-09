# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 09:28:01 2024

@author: Ahmed Alshamli

Given an array of integers (distance) and start point (0,0) and the moves are in this order:
    [North , West , South , East] , print true if the path crosses itself or false if it does not.

"""

def solve(lst):
    visited = []
    directions = {1:(0,1), 2:(-1,0), 3:(0,-1), 0:(1,0)}
    point = (0,0)
    direction = 1 # [North , West , South , East]
    
    for i in lst:
        for j in range(i):
            visited.append(point)
            point = (point[0]+directions[direction][0],point[1]+directions[direction][1])
            if point in visited:
                return True
        direction = (direction+1)%4
        
    return False
        
        

test1 = [2,1,1,2]
print(solve(test1))

test2 = [1,2,3,4]
print(solve(test2))

test3 = [1,1,1,2,1]
print(solve(test3))

test4 = [10,5,6,9,8,6]
print(solve(test4))

test5 = [1,2,3,4,2,8,10]
print(solve(test5))

test6 = [1,1,4,5,2,1]
print(solve(test6))
