import copy

class Computer():
    def __init__(self, player=None):
        if player == 'O':
            self.ai = -1
        else:
            self.ai = 1
    
    def _actions(self, state, player):
        coords = []
        for x, row in enumerate(state):
            for y, cell in enumerate(row):
                if not cell:
                    coords.append((x, y, player))
        return coords
    
    def _result(self, state, action):
        x, y, player = action
        state[x][y] = player
        return state
    
    def _player(self, state):
        count = 0
        for row in state:
            for cell in row:
                if cell:
                    count += 1
        return -1 if count % 2 == 0 else 1
    
    def _value(self, state): 
        winner = None

        for row in state:
        #row check
            if sum(row) == 3:
                winner = 1
                break
            elif sum(row) == -3:
                winner = -1
                break
        
        for col in range(3):
        #col check
            if state[0][col] + state[1][col] + state[2][col] == 3:
                winner = 1
                break
            elif state[0][col] + state[1][col] + state[2][col] == -3:
                winner = -1
                break

        if state[0][0] == state[1][1] == state[2][2] and state[0][0] != 0:
            winner = state[0][0]
        elif state[0][2] == state[1][1] == state[2][0] and state[0][2] != 0:
            winner = state[0][2]
            
        #draw check
        if winner is None:
            count = 0
            for row in state:
                for cell in row:
                    if cell:
                        count += 1
                if count == 9:
                    winner = 0
            
        return winner
    
    def _playing(self, state):        
        for row in state:
            for cell in row:
                if not cell:
                    return True
        return False        
    
    def _minimax(self, state, player):
        winner = self._value(state)
        
        if winner is not None:
            return winner
        
        if player == -1:
            value = +999
            for action in self._actions(state, player):
                next_state = self._result(copy.deepcopy(state), action)
                value = min(value, self._minimax(next_state, +1))
            return value
        
        if player == +1:
            value = -999
            for action in self._actions(state, player):
                next_state = self._result(copy.deepcopy(state), action)
                value = max(value, self._minimax(next_state, -1))
            return value
        
    def choice(self, state):
        best_move = None
        best_value = -999 if self.ai == 1 else 999
        for x, row in enumerate(state):
            for y, cell in enumerate(row):
                if not cell:
                    state[x][y] = self.ai
                    value = self._minimax(state, self.ai * -1)
                    state[x][y] = 0
                    
                    if self.ai == 1 and best_value < value:
                        best_value = value
                        best_move = (x, y)
                    elif self.ai == -1 and best_value > value:
                        best_value = value
                        best_move = (x, y)
        if best_move is not None:
            x, y = best_move
            state[x][y] = self.ai
        return state


