import Game
import Human_Player
import MonteCarlo_Player

if __name__ == '__main__':
    p1 = MonteCarlo_Player.Player(0,10)
    p2 = MonteCarlo_Player.Player(1,10000)
    game = Game.Game(p1,p2)

    while(game.gaming):
        game.show_table()
        game.turn()
    game.show_end()
