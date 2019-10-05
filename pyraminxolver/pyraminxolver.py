from collections import deque
import pickle
import time
from . import Pyraminx, PYRAMINX_CASE_PATH


class PyraminXolver():
    def __init__(self):
        with open(PYRAMINX_CASE_PATH, 'rb') as f:
            self.graph = pickle.load(f)
        self.moves = ["U", "U'", "R", "R'", "L", "L'", "B", "B'"]
        Pyraminx()
        pass

    def search(self, state, max_slack=0):
        start_time = time.time_ns()
        solutions = []
        k = 0
        queue = deque()
        queue.append((state, [], [state], 0))

        while queue:
            state, moves, path, slack = queue.popleft()
            depth = self.graph[state][0]
            k += 1
            if self.graph[state][0] > 0:
                for i in range(1, 9):
                    if len(moves) > 0 and (i-1) // 2 == (moves[-1]-1) // 2:
                        continue
                    new_state = self.graph[state][i]
                    new_slack = slack + self.graph[new_state][0] - depth + 1
                    if new_slack <= max_slack:
                        queue.append((new_state, moves + [i], path + [new_state], new_slack))
            else:
                solutions.append((self.parse(moves), len(moves), time.time_ns()-start_time, path))
        return solutions

    def parse(self, moves):
        return ' '.join([self.moves[x - 1] for x in moves])

    def scramble_to_state(self, algorithm):
        moves = algorithm.split(' ')
        state = 0
        for move in moves:
            move_idx = self.moves.index(move) + 1
            state = self.graph[state][move_idx]

        return state

    def search_scramble(self, algorithm, max_slack=0):
        state = self.scramble_to_state(algorithm)
        return self.search(state, max_slack=max_slack)
