class Player():
    def __init__(self, id):
        self.id = id
        self.piece = ['X','O']
        print('Você é o {}'.format(self.piece[self.id]))
        print('No seu turno digite a linha e a coluna nessa ordem e com um espaço entre eles. Assim:')
        print('0 0')

    def play(self, board):
        return tuple(int(i) for i in input('Digite coordenada. . .\n').split(' '))