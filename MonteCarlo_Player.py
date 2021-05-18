import numpy as np
import random

class Player():
    def __init__(self, id, ite=10000):
        self.id = id
        self.pieces = ['X','O']
        self.ite = ite

    def ite_simulate(self,board):
        i = 0
        flag = True
        score = 0
        if len(self.get_valid_pos(board))>0:
            step = self.get_valid_pos(board)[0]
        else: step = [-1,-1]
        while(len(self.get_valid_pos(board))>0):
            s, board = self.simulate(board)
            if flag:
                step = s
                flag = False
            if self.verify_won(board):
                score = 100 - i*10
                return [tuple(step), score]
            if len(self.get_valid_pos(board))>0:
                _, board = self.simulate(board, o = 1)
                if self.verify_lose(board):
                    score = -(100 - i*10)
                    return [tuple(step), score]
            i += 1
        return [tuple(step), score]

    def simulate(self, board, o = 0):
        valid_pos = self.get_valid_pos(board)
        choice = random.choice(valid_pos)
        board[tuple(choice)] = self.pieces[self.id-o]
        return choice, board
    
    def get_valid_pos(self, board):
        valid_pos = []
        for l in range(3):
            for r in range(3):
                if board[l,r] == ' ': valid_pos.append([l,r])
        return valid_pos

    def verify_won(self, board):
        math_board = self.get_math_board(board)
        if (math_board[0,0] + math_board[1,1] + math_board[2,2] == 3 or
            math_board[2,0] + math_board[1,1] + math_board[0,2] == 3 or
            sum(math_board[:,0]) == 3 or
            sum(math_board[:,1]) == 3 or
            sum(math_board[:,2]) == 3 or
            sum(math_board[0,:]) == 3 or
            sum(math_board[1,:]) == 3 or
            sum(math_board[2,:]) == 3): 
            return True
        else: return False
    
    def verify_lose(self, board):
        math_board = self.get_math_board(board)
        if (math_board[0,0] + math_board[1,1] + math_board[2,2] == -3 or
            math_board[2,0] + math_board[1,1] + math_board[0,2] == -3 or
            sum(math_board[:,0]) == -3 or
            sum(math_board[:,1]) == -3 or
            sum(math_board[:,2]) == -3 or
            sum(math_board[0,:]) == -3 or
            sum(math_board[1,:]) == -3 or
            sum(math_board[2,:]) == -3): 
            return True
        else: return False

    def get_math_board(self, board):
        math_board = np.array([[0,0,0]]*3)
        for l in range(3):
            for r in range(3):
                if board[l,r] == self.pieces[self.id]: math_board[l,r] = 1
                elif board[l,r] == self.pieces[self.id - 1]: math_board[l,r] = -1
        return math_board
    
    def play(self, i_board):
        random_steps = []
        for _ in range(self.ite):
            board = np.array(i_board)
            random_steps.append(self.ite_simulate(board))
        random_steps = np.array(random_steps, dtype=object)
        scores = random_steps[:,1]
        steps = random_steps[:,0]
        return steps[np.argmax(scores, axis=0)]
        

if __name__ == '__main__':
    p = Player(0)
    b = np.array([[' ',' ',' ']]*3)
    p.play(b)