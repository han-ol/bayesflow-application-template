{% if cookiecutter.model_comparison == "yes" -%}
from bayesflow.simulators import ModelComparisonSimulator

from .model_1 import simulator as simulator_1
from .model_2 import simulator as simulator_2

simulator = ModelComparisonSimulator(simulators=[simulator_1, simulator_2])

from .adapter import adapter
from .adapter_comparison import adapter_comparison
{% else -%}
from .model_1 import simulator
from .adapter import adapter
{% endif %}
