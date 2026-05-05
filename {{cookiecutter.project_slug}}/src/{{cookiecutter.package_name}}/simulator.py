import numpy as np
import bayesflow as bf


N_OBS = 32

PARAM_NAMES = ["mu", "sigma"]


def prior():
    mu = np.random.normal(0.0, 5.0)
    sigma = np.random.lognormal(0.0, 0.5)
    return dict(mu=mu, sigma=sigma)


def observation_model(mu, sigma):
    y = np.random.normal(mu, sigma, size=N_OBS)
    return dict(y=y.astype(np.float32))


simulator = bf.make_simulator([prior, observation_model])
