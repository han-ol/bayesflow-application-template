import os
import shutil

MODEL_COMPARISON = "{{ cookiecutter.model_comparison }}"
NUM_MODELS = {{ cookiecutter.num_models }} if MODEL_COMPARISON == "yes" else 1
PACKAGE_NAME = "{{ cookiecutter.python_package }}"

project_root = os.getcwd()
pkg_dir = os.path.join(project_root, "src", PACKAGE_NAME)
template_dir = os.path.join(pkg_dir, "_model_template")

# Copy model template into model_1/, model_2/, ..., model_N/
for i in range(1, NUM_MODELS + 1):
    shutil.copytree(template_dir, os.path.join(pkg_dir, f"model_{i}"))

shutil.rmtree(template_dir)

# Remove model-comparison-only files when not needed
if MODEL_COMPARISON == "no":
    os.remove(os.path.join(project_root, "examples", "compare_models.py"))
    os.remove(os.path.join(pkg_dir, "adapter_comparison.py"))

# Write __init__.py with the right imports
lines = []

if MODEL_COMPARISON == "yes":
    lines += ["from bayesflow.simulators import ModelComparisonSimulator", ""]
    for i in range(1, NUM_MODELS + 1):
        lines.append(f"from .model_{i} import simulator as simulator_{i}")
    sim_list = ", ".join(f"simulator_{i}" for i in range(1, NUM_MODELS + 1))
    lines += ["", f"simulator = ModelComparisonSimulator(simulators=[{sim_list}])", ""]
    lines += [
        "from .adapter_inference import adapter_inference",
        "from .adapter_comparison import adapter_comparison",
    ]
else:
    lines += [
        "from .model_1 import simulator",
        "from .adapter_inference import adapter_inference",
    ]

with open(os.path.join(pkg_dir, "__init__.py"), "w") as f:
    f.write("\n".join(lines) + "\n")
