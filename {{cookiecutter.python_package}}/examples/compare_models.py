import keras
import bayesflow as bf
from bayesflow.approximators import ModelComparisonApproximator

from {{cookiecutter.python_package}} import simulator, adapter_comparison

NUM_MODELS = 2

approximator = ModelComparisonApproximator(
    num_models=NUM_MODELS,
    classifier_network=keras.Sequential(
        [
            keras.layers.Dense(128, activation="relu"),
            keras.layers.Dense(128, activation="relu"),
        ]
    ),
    summary_network=bf.networks.DeepSet(),
)

train_data = simulator.sample(10000)
test_data = simulator.sample(500)

history = approximator.fit(
    adapter=adapter_comparison,
    dataset=bf.datasets.OfflineDataset(train_data, adapter=adapter_comparison),
    epochs=30,
)

probs = approximator.predict(conditions=test_data)
print("Posterior model probabilities shape:", probs.shape)

true_model = test_data["model_indices"].argmax(axis=-1)
predicted_model = probs.argmax(axis=-1)
accuracy = (true_model == predicted_model).mean()
print(f"Classification accuracy: {accuracy:.3f}")
