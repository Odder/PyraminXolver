from collections import deque
import pickle
from . import Pyraminx, PYRAMINX_CASE_PATH


def setup():
    graph = create_move_table()

    with open(PYRAMINX_CASE_PATH, 'wb') as f:
        pickle.dump(graph, f, pickle.HIGHEST_PROTOCOL)


def create_move_table():
    move_table = [[-1, -1, -1, -1, -1, -1, -1, -1, -1] for _ in range(933120)]
    queue = deque()
    queue.append(0)
    move_table[0][0] = 0

    while queue:
        node = queue.popleft()
        state = Pyraminx.id_to_state(node)
        for i in range(1, 9):
            transformation = Pyraminx.move_transformations[i-1]
            new_state = Pyraminx.apply_move(state, transformation)
            new_id = Pyraminx.state_to_id(new_state)
            if move_table[new_id][0] == -1:
                move_table[new_id][0] = move_table[node][0] + 1
                queue.append(new_id)
            move_table[node][i] = new_id

    return move_table


if __name__ == '__main__':
    setup()
