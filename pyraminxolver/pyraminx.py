import itertools


def is_even_permutation(permutation):
    swaps = 0
    p = list(permutation)

    for i in range(6):
        if p[i] != i:
            for j in range(i, 6):
                if p[j] == i:
                    p[i], p[j] = p[j], p[i]
                    swaps += 1
                    break

    return swaps % 2 == 0


class Pyraminx:
    ep = [[y for y in x] for x in itertools.permutations(range(6)) if is_even_permutation(x)]
    eo = [[y for y in x] for x in itertools.product(range(2), repeat=6) if sum(list(x)) % 2 == 0]
    co = [[y for y in x] for x in itertools.product(range(3), repeat=4)]
    move_transformations = [
        [  # U
            [0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0],
            [2, 0, 1, 3, 4, 5]
        ],
        [  # U'
            [0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0],
            [1, 2, 0, 3, 4, 5]
        ],
        [  # R
            [0, 0, 0, 1, 1, 0],
            [0, 1, 0, 0],
            [0, 4, 2, 1, 3, 5]
        ],
        [  # R'
            [0, 1, 0, 1, 0, 0],
            [0, 2, 0, 0],
            [0, 3, 2, 4, 1, 5]
        ],
        [  # L
            [0, 0, 0, 0, 1, 1],
            [0, 0, 1, 0],
            [0, 1, 5, 3, 2, 4]
        ],
        [  # L'
            [0, 0, 1, 0, 1, 0],
            [0, 0, 2, 0],
            [0, 1, 4, 3, 5, 2]
        ],
        [  # B
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1],
            [3, 1, 2, 5, 4, 0]
        ],
        [  # B'
            [1, 0, 0, 0, 0, 1],
            [0, 0, 0, 2],
            [5, 1, 2, 0, 4, 3]
        ],
    ]

    def __init__(self):
        pass

    @staticmethod
    def apply_move(state, move):
        eo, co, ep = state
        transform_eo, transform_co, transform_ep = move
        permuted_eo = [eo[x] for x in transform_ep]

        return (
            [(a + b) % 2 for a, b in zip(permuted_eo, transform_eo)],
            [(a + b) % 3 for a, b in zip(co, transform_co)],
            [ep[x] for x in transform_ep],
        )

    @staticmethod
    def id_to_state(idx):
        ep = Pyraminx.ep[idx % 360]
        co = Pyraminx.co[idx // 360 % 81]
        eo = Pyraminx.eo[idx // 29160 % 32]

        return eo, co, ep

    @staticmethod
    def state_to_id(state):
        eo, co, ep = state
        idx = 0
        if (ep not in Pyraminx.ep) or (co not in Pyraminx.co) or (eo not in Pyraminx.eo):
            return -1

        idx += Pyraminx.ep.index(ep)
        idx += Pyraminx.co.index(co) * 360
        idx += Pyraminx.eo.index(eo) * 29160

        return int(idx)


if __name__ == '__main__':
    pass
