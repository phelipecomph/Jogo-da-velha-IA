import numpy as np

class Game():
    def __init__(self, player_one, player_two):
        self.board = np.array([[' ',' ',' ']]*3)
        self.player_turn = 0
        self.player_piece = ['X','O']
        self.player = [player_one, player_two]
        self.gaming = True
        self.winner = -1 # -1: Em jogo; 0: X; 1: O; 2: Empate
    
    def turn(self):
        pos = self.player[self.player_turn].play() # A funcao Play precisa retornar uma tupla (row, col)
        if pos[0] > 2 or pos[1] > 2 or pos[0] < 0 or pos[1] < 0: 
            print('O jogador {} tentou jogar em um espaço que não existe'.format(self.player_piece[self.player_turn]))
        elif self.board[pos] == ' ': 
            self.board[pos] = self.player_piece[self.player_turn]
            self.verify_end()
            self.player_turn = abs(self.player_turn - 1)
        else: 
            print('O jogador {} tentou jogar em um espaço já ocupado'.format(self.player_piece[self.player_turn]))
        
    
    def verify_end(self):
        math_board = self.math_board()
        if (abs(math_board[0,0] + math_board[1,1] + math_board[2,2]) == 3 or
            abs(math_board[2,0] + math_board[1,1] + math_board[0,2]) == 3 or
            abs(sum(math_board[:,0])) == 3 or
            abs(sum(math_board[:,1])) == 3 or
            abs(sum(math_board[:,2])) == 3 or
            abs(sum(math_board[0,:])) == 3 or
            abs(sum(math_board[1,:])) == 3 or
            abs(sum(math_board[2,:])) == 3): 
            self.winner = self.player_turn
            self.gaming = False
        elif 0 not in math_board[:,:]:
            self.winner = 2
            self.gaming = False

    def math_board(self):
        board = np.array([[0,0,0]]*3)
        for l in range(3):
            for r in range(3):
                if self.board[l,r] == 'X': board[l,r] = 1
                elif self.board[l,r] == 'O': board[l,r] = -1
        return board

    def show_table(self):
        for row in self.board: print(row)
        print()
    
    def show_end(self):
        self.show_table()
        if self.winner == -1: print('O Jogo não foi finalizado')
        elif self.winner == 0: print('X é o vencedor')
        elif self.winner == 1: print('O é o vencedor')
        elif self.winner == 2: print('O Jogo empatou')