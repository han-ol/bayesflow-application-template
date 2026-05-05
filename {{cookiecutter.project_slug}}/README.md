# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Install & run

We use `uv` to manage a reproducible python environment. See the documentation of [uv projects](https://docs.astral.sh/uv/guides/projects/).

```bash
uv sync                                  # create .venv and install deps
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
src/{{cookiecutter.package_name}}/
├── simulator.py   # prior() + observation_model() -> bf.make_simulator(...)
├── adapter.py     # bf.Adapter wiring simulator outputs to BayesFlow roles
└── __init__.py    # re-exports simulator, adapter
```

```python
from {{cookiecutter.package_name}} import simulator, adapter
```
