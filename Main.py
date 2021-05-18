import Game
import Human_Player

if __name__ == '__main__':
    p1 = Human_Player.Player(0)
    p2 = Human_Player.Player(1)
    game = Game.Game(p1,p2)

    while(game.gaming):
        game.show_table()
        game.turn()
    game.show_end()
