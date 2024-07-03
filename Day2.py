# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 16:03:52 2024

@author: Ahmed Alshamli

Givin nxn 2d matrix representing an image, rotate image by 90 degrees (clockwise)
"""
def printm(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j],end=" ")
        print()

def rotate(matrix):
    rotated_matrix = [i[:] for i in matrix]
    printm(rotated_matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            rotated_matrix[j][-(i+1)] = matrix[i][j]
    
    
    return rotated_matrix

 
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

printm(rotate(matrix))

