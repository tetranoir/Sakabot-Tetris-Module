from sys import stdin, stdout


class Sakabot(object):
    def __init__(self):
        self.board = 

    def settings(self):
        return

    def update(self):
        return

    def action(self):
        return

    def read_input(self):
        try:
            cmd, args = stdin.readline().strip().split(' ', 1)
        except EOFError:
            return '', ''
        return cmd, args

    def run(self):
        while not stdin.closed:
            cmd, args = read_input()
            if cmd == 'settings': 
                settings(args)
            elif cmd == 'update': 
                update(args)
            elif cmd == 'action': 
                move = action(args)
                stdout.write(','.join(moves) + '\n')
                stdout.flush()
            else: continue

if __name__ == "__main__":
    Sakabot.run()