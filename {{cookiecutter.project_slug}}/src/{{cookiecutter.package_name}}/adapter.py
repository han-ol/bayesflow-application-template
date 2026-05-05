import bayesflow as bf

from .simulator import PARAM_NAMES


adapter = (
    bf.Adapter()
    .convert_dtype("float64", "float32")
    .concatenate(PARAM_NAMES, into="inference_variables")
    .expand_dims("y", axis=-1)
    .concatenate(["y"], into="summary_variables")
)
