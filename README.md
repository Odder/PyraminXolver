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

pyra = PyraminXolver()
solutions = pyra.search_scramble("R U L R U L B' R' U")
for solution, move_count, time_ns, _ in solutions:
    print(f'{solution} ({move_count} moves found in {time_ns // 1000000}ms)')
```