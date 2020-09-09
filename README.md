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