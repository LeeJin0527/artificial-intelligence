# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:04:31 2021

@author: ijin
"""

class State:
    def __init__(self, board, goal, moves =0):
        self.board = board 
        self. goal = goal
        self.moves = moves
        
    def get_new_board(self, i1, i2, moves):
        new_board = self.board[ : ]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, moves)
    
    def expand(self, moves):
        result = []
        i = self.board.index(0)
        if not i in [0, 1, 2]:
            result.append(self.get_new_board(i, i-3, moves))
        if not i in [0, 3, 6]:
            result.append(self.get_new_board(i, i -1, moves))
        if not i in [2, 5, 8]:
            result.append(self.get_new_board(i, i+1, moves))
        if not i in [6, 7, 8]:
            result.append(self.get_new_board(i, i+3, moves))
        return result
    
    def __str__(self):
        return str(self.board[:3]) +"\n"+\
            str(self.board[3:6]) +"\n" +\
            str(self.board[6:]) +"\n" +\
            "======================"
            
    def __eq__(self , other):
        return self.board == other.board
    
puzzle = [1, 2, 3, 
          4, 5, 6, 
          0, 7, 8]
goal = [1, 2, 3, 
        4, 5, 6,
        7, 8, 0]

open_stack =[]
open_stack.append(State(puzzle, goal))

closed_stack =[]
moves = 0

while len(open_stack) != 0 :
    current = open_stack.pop(0)
    print(current)
    if current.board ==goal:
        print("탐색성공")
        break
    moves = current.moves +1
    closed_stack.append(current)
    current.expand(moves).reverse()
    for state in current.expand(moves):
        if (state in closed_stack) or (state in open_stack):
            continue
        else:
            open_stack.insert(0, state)
    

    
    
                
    

