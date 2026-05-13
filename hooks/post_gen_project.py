import os
import shutil

if "{{ cookiecutter.model_comparison }}" == "no":
    project_root = os.getcwd()
    pkg_dir = os.path.join(project_root, "src", "{{ cookiecutter.python_package }}")
    shutil.rmtree(os.path.join(pkg_dir, "model_2"))
    os.remove(os.path.join(project_root, "examples", "compare_models.py"))
    os.remove(os.path.join(pkg_dir, "adapter_comparison.py"))
