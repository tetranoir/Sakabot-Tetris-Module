class Player(object):
    def __init__(self):
        self.timebank = 0
        self.time_per_move = 500

class Board(object):
    def __init__(self, w, h):
        self.width = w
        self.height = h

class State(object):
    def __init__(self):
        self.round = 0
        self.combo = 0
        self.points = 0

        self.piece = None
        self.piecePosiiton = None
        self.next_piece = None

