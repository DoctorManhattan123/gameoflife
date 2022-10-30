# Game of life

This is the game of life.

[Game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

## Requirements

* Python >= 3.10.6
* Pip >= 21.3.1

## Setup

We use a [virtual environment](https://docs.python.org/3/tutorial/venv.html).

```sh
# bash
source ./venv/bin/activate
# fish 
source ./venv/bin/activate.fish
# csh
source ./venv/bin/activate.csh
```

All the next commands imply that you are inside the virtual environment.
You can see this, because in your command line there will be written `(venv)` 
at the left of command.

## Install all dependencies

```shell
python3 -m pip install -r requirements.txt
```

## Run

```sh
python3 main.py
```

## Contribute

### Add dependency

```shell
python -m pip install <pkg>
```
