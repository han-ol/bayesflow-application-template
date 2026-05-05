import bayesflow as bf

from {{cookiecutter.package_name}} import adapter, simulator

workflow = bf.BasicWorkflow(
    simulator=simulator,
    adapter=adapter,
    summary_network=bf.networks.DeepSet(),
)

train_data = simulator.sample(10000)
test_data = simulator.sample(100)

history = workflow.fit_offline(train_data, epochs=30)

figs = workflow.plot_default_diagnostics(test_data, num_samples=300)

for fig_name, fig in figs.items():
    fname = f"diagnostic_{fig_name}.png"
    fig.savefig(fname, dpi=150, bbox_inches="tight")
    print(f"Saved {fname}")
