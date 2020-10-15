import random

class MyPlayer:
    '''Hrac hraje na zaklade nahodneho vyberu'''
    def __init__(self, payoff_matrix, number_of_iterations=100):
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations=number_of_iterations
        self.history = [None]*self.number_of_iterations

    def move(self):
        return True


    def record_last_moves(self, my_last_move, opponent_last_move):
        # INPUTS: my_last_move, opponent_last_move
                    # respective last moves of both players
        # OUTPUTS: none
        # notes down players' moves in pairs in a list
        del self.history[-1]
        self.history.insert(0, (my_last_move, opponent_last_move))


