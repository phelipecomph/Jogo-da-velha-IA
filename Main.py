import Game
import Human_Player
import MonteCarlo_Player
import Q_Player

if __name__ == '__main__':
    p1 = MonteCarlo_Player.Player(0,10)
    p2 = Q_Player.Player(1)
    p2.learn(n=5000)
    

    for _ in range(10):
        game = Game.Game(p2,p1)
        while(game.gaming):
            game.show_table()
            game.turn()
        game.show_end()
