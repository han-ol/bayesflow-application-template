# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Install & run

We use `uv` to manage a reproducible python environment. See the documentation of [uv projects](https://docs.astral.sh/uv/guides/projects/).

```bash
uv sync                                  # create .venv, install deps, and install this package in editable mode
uv run python examples/calibrate.py      # run inside the environment
```

> `uv run` uses the project's `.venv` automatically.
> To activate manually instead: `source .venv/bin/activate` (Linux/macOS) or `.venv\Scripts\activate` (Windows).

## Add dependencies

```bash
uv add pandas                            # will add pandas to pyproject.toml and uv.lock
```

## Structure

```
src/{{cookiecutter.python_package}}/
├── model_1/
│   ├── simulator.py   # prior() + observation_model() -> bf.make_simulator(...)
│   └── __init__.py
├── adapter_inference.py   # bf.Adapter for per-model posterior inference
└── __init__.py
```

```python
from {{cookiecutter.python_package}} import simulator, adapter_inference
```
