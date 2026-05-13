# bayesflow-application-template

A cookiecutter template for amortized Bayesian inference using BayesFlow.

    cookiecutter gh:han-ol/bayesflow-application-template

If you don't have cookiecutter: `uv tool install cookiecutter` ([get uv](https://docs.astral.sh/uv/getting-started/installation/)) or `pipx install cookiecutter`.

It will ask questions like this:

    [1/3] project_name (My BayesFlow Application): Gaussian Mixture
    [2/3] python_package (gaussian_mixture): 
    [3/3] model_comparison (no): yes

Set `model_comparison` to `yes` to scaffold two competing models and a `ModelComparisonApproximator` workflow alongside the standard inference setup.

Then:

    cd gaussian_mixture
    uv sync
    uv run python examples/calibrate.py

Fill in your priors and likelihoods in `model_*/simulator.py`.
