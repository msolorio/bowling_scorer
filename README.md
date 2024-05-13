# Running the App
See Makefile for running and testing app from Docker.

# Debugger
To get debugger to work and run tests locally, outside of Docker
- create `.venv` - `$ python -m venv .venv`
- start venv - `$ source .venv/bin/activate`
- install packages - `$ pip install -r requirements.txt`
- install setup packages (installs `app` as a package accessible from `tests`) - `$ pip install -e src`
