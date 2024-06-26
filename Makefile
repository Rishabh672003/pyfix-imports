project = pyfix_imports
mode = Debug

all: install

install:
	pdm install

build:
	pdm build

run:
	python -m $(project) /home/rishabh/projects/PYTHON-ML/numpy/test.py
