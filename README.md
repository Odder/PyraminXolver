# PyraminXolver
A pyraminx solver!

## Installation
Download using pip
```commandline
pip  install pyraminxolver
```

Setup the pyraminx graph (this should take around 5-30 seconds). You only need to run this once.
```commandline
pyraminxolver-setup
```

## Usage
### Command-line interface
You can either supply a scramble like this:
```commandline
pyraminxolver --scramble="R U R' L' U R"
```

or in input file with scrambles
```commandline
pyraminxolver --input-file=scrambles.txt
```

where the content of scrambles.txt looks like this
```text
L U R L U' B' R
L R U R L R U R
```

If you also want it to find suboptimal solutions you can use the `slack` to indicate how many moves from optimal you will allow the solutions to be.
```commandline
pyraminxolver --scramble="R U R' L' U R" --slack=2
```

### Programmatical interface
```python
from pyraminxolver import PyraminXolver

px = PyraminXolver()
solutions = px.search_scramble("R U L R U L B' R' U")
for solution, move_count, time_ns, _ in solutions:
    print(f'{solution} ({move_count} moves found in {time_ns // 1000000}ms)')
```

Generating algs for L4E with 2 moves slack for each case and dumping them into a file.
```python
from pyraminxolver import PyraminXolver, Pyraminx

slack = 2
file_name = 'l4e-solutions.txt'
pyra = PyraminXolver()
cases = Pyraminx.set([
    [-1, -1, -1, 0, -1, 0],
    [0, 0, 0, 0],
    [-1, -1, -1, 3, -1, 5],
])

for case in cases:
    solutions = pyra.search(case, slack)
    with open(file_name, 'a') as f:
        f.write(f'\nSolving a new L4E case\n')
        for solution, length, timing, _ in solutions:
            f.write(f'{solution} ({length})\n')
```

### State explanation:
When generating a set we need to describe the properties of the pyraminx. We describe a fixed position, with some "wildcards" and then all valid cases will be based off that.
The first array descibes EO, then CO and lastly EP.

```python
[
    [UB, UR, UL, BR, RL, BL], # EO
    [U, R, L, B], # CO
    [UB, UR, UL, BR, RL, BL] # EP
]
```