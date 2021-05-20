from collections import defaultdict
from Game import Game
from MonteCarlo_Player import Player as M_Player
import random
import pickle


class Player:
    def __init__(self,id = 0):
        self.id = id
        self.pieces = ['X','O']
        self.eps = 1.0
        self.qlearner = Q()

    def play(self, state):
        self.last_action = self._get_action(state, self.get_valid_pos(state))
        return tuple(self.last_action)

    def _get_action(self, state, valid_actions):
        if random.random() < self.eps:
            return random.choice(valid_actions)
        best = self.qlearner.get_best_action(self.get_math_board(state))
        if best is None:
            return random.choice(valid_actions)
        return best

    def _learn_one_game(self,p2):
        game = Game(self,p2)
        while True:
            state = game.board
            game.turn()
            action = self.last_action
            winner = game.winner

            if winner == self.id and not game.gaming:
                self.qlearner.update(self.get_math_board(state), action, self.get_math_board(game.board), 100)
                break

            if winner != self.id and not game.gaming:
                self.qlearner.update(self.get_math_board(state), action, self.get_math_board(game.board), -100)
                break
            self.qlearner.update(self.get_math_board(state), action, self.get_math_board(game.board), 0)
    
    def get_valid_pos(self, board):
        valid_pos = []
        for l in range(3):
            for r in range(3):
                if board[l,r] == ' ': valid_pos.append([l,r])
        return valid_pos
    
    def get_math_board(self, board):
        math_board = [[0, 0, 0] for _ in range(3)]
        for l in range(3):
            for r in range(3):
                if board[l,r] == self.pieces[self.id]: math_board[l][r] = 1
                elif board[l,r] == self.pieces[self.id - 1]: math_board[l][r] = -1
        return math_board

    def learn(self, n=20000):
        player_2 = M_Player(1,1)
        for i in range(n):
            self._learn_one_game(player_2)
            self.eps -= 0.0001
            print('{0}/{1}'.format(i,n))

class Q:
    def __init__(self, alpha=0.5, discount=0.5):
        self.alpha = alpha
        self.discount = discount
        self.values = defaultdict(lambda: defaultdict(lambda: 0.0))
        self.values_to_save = {}

    def update(self, state, action, next_state, reward):
        value = self.values[str(state)][str(action)]
        v = list(self.values[str(next_state)].values())
        next_q = max(v) if v else 0
        value = value + self.alpha * (reward + self.discount * next_q - value)
        self.values[str(state)][str(action)] = value
    
    def get_best_action(self, state):
        keys = self.values[str(state)].keys()
        if not keys:
            return None
        return int(max(keys, key=lambda x: self.values[str(state)][x])[1]), int(max(keys, key=lambda x: self.values[str(state)][x])[4])

if __name__ == '__main__':
    q_player = Agent()
    q_player.learn(n=5000)