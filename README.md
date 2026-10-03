# openshell-lab

A disposable lab repository for OpenShell agent evaluations. It holds a small
Python project so an agent has something real to clone, install, and test.

`release_notes` parses release lines such as `1.4.0 2026-03-14`, finds the
latest stable version, and measures the days between releases.

## Run the tests

```shell
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pytest
```

Branches named `work/...` are left behind by evaluation runs as evidence.
