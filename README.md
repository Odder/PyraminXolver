# PyraminXolver
A pyraminx solver!

## Installation
Download using pip
```commandline
pip  install pyraminxolver
```

Setup the pyraminx graph (this may take around 5-10 minutes)
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

If you also want it to find suboptimal solutions you can use the `max-slack` to indicate how many moves from optimal you would allow it to be.
```commandline
pyraminxolver --scramble="R U R' L' U R" --max-slack=2
```

### Programmatical interface
```python
from pyraminxolver import PyraminXolver

pyra = PyraminXolver()
solutions = pyra.search_scramble("R U L R U L B' R' U")
```