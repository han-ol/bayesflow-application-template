# {{cookiecutter.project_name}}

{{cookiecutter.description}}

---

## Getting started

*Generated with [bayesflow-application-template](https://github.com/han-ol/bayesflow-application-template). Rewrite anything below once you've filled in the models.*

```bash
uv sync                                        # set up .venv and install this package in editable mode
uv sync --extra dev                            # also install dev tools (ruff, pytest, ...)
uv run pre-commit install                      # set up git hooks
uv run python examples/calibrate.py            # run inside the environment
{% if cookiecutter.model_comparison == "yes" -%}
uv run python examples/compare_models.py       # run direct model comparison
{% endif %}```

`uv run` uses the project's `.venv` automatically. Activate manually with `source .venv/bin/activate` (Linux/macOS) or `.venv\Scripts\activate` (Windows). Add packages with `uv add <package>`.

Fill in your priors and likelihoods in `model_*/simulator.py`. Adjust the adapters if your observation key differs from `y`.

### Structure

{% if cookiecutter.model_comparison == "yes" -%}
```
src/{{cookiecutter.python_package}}/
├── model_1/
│   ├── simulator.py   # prior() + observation_model() -> bf.make_simulator(...)
│   └── __init__.py
├── model_2/
│   ├── simulator.py
│   └── __init__.py
├── adapter_inference.py   # bf.Adapter for per-model posterior inference
├── adapter_comparison.py  # bf.Adapter for ModelComparisonApproximator
└── __init__.py
```
{% else -%}
```
src/{{cookiecutter.python_package}}/
├── model_1/
│   ├── simulator.py   # prior() + observation_model() -> bf.make_simulator(...)
│   └── __init__.py
├── adapter_inference.py   # bf.Adapter for per-model posterior inference
└── __init__.py
```
{% endif %}

---

## Usage

<!-- Replace this section with documentation for users of your package. -->

```python
{% if cookiecutter.model_comparison == "yes" -%}
from {{cookiecutter.python_package}} import simulator, adapter_inference, adapter_comparison
{% else -%}
from {{cookiecutter.python_package}} import simulator, adapter_inference
{% endif %}```
