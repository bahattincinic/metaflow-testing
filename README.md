# Metaflow Testing

This repository explains how to add unit test for MetaFlow flows.

MetaFlow doesn't support running outside of its own file.
That's why we can only test it with `subprocess`

Gitter thread is below;

https://gitter.im/metaflow_org/community?at=5f4e3aeadfaaed4ef5239f51

## Helpful Links to understand how MetaFlow core tests work.

- https://gitter.im/metaflow_org/community?at=5e5e87fcca2f5a558d62ad96
- https://docs.metaflow.org/internals-of-metaflow/testing-philosophy

# Installation

Clone project and install dependencies:

```bash
$ git clone git@github.com:bahattincinic/metaflow-testing.git
$ cd metaflow-testing
$ virtualenv env --python=/usr/bin/python3
$ pip install -r requirements.txt
```

Run flow:

```bash
$ python flow.py run
```

Run Tests:

```bash
$ python tests/run_tests.py

Metaflow 2.2.3 executing ExampleFlow for user:bahattincinic
Validating your flow...
    The graph looks good!
Running pylint...
    Pylint is happy!
2020-09-10 11:21:24.846 Workflow starting (run-id 1599726084839448):
2020-09-10 11:21:24.852 [1599726084839448/start/1 (pid 2524)] Task is starting.
2020-09-10 11:21:25.638 [1599726084839448/start/1 (pid 2524)] Task finished successfully.
2020-09-10 11:21:25.644 [1599726084839448/load_cars/2 (pid 2529)] Task is starting.
2020-09-10 11:21:26.253 [1599726084839448/load_cars/2 (pid 2529)] Foreach yields 2 child steps.
2020-09-10 11:21:26.254 [1599726084839448/load_cars/2 (pid 2529)] Task finished successfully.
2020-09-10 11:21:26.260 [1599726084839448/calculate_car/3 (pid 2534)] Task is starting.
2020-09-10 11:21:26.265 [1599726084839448/calculate_car/4 (pid 2535)] Task is starting.
2020-09-10 11:21:27.097 [1599726084839448/calculate_car/3 (pid 2534)] Task finished successfully.
2020-09-10 11:21:27.102 [1599726084839448/calculate_car/4 (pid 2535)] Task finished successfully.
2020-09-10 11:21:27.107 [1599726084839448/merge_car_data/5 (pid 2544)] Task is starting.
2020-09-10 11:21:27.711 [1599726084839448/merge_car_data/5 (pid 2544)] Task finished successfully.
2020-09-10 11:21:27.717 [1599726084839448/end/6 (pid 2549)] Task is starting.
2020-09-10 11:21:28.467 [1599726084839448/end/6 (pid 2549)] Task finished successfully.
2020-09-10 11:21:28.468 Done!
....
----------------------------------------------------------------------
Ran 4 tests in 9.087s

OK
```