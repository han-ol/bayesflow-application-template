import bayesflow as bf

adapter_comparison = (
    bf.Adapter()
    .convert_dtype("float64", "float32")
    .concatenate(["model_indices"], into="inference_variables")
    .expand_dims("y", axis=-1)
    .concatenate(["y"], into="summary_variables")
)
