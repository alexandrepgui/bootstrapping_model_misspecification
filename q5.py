import math
import numpy as np


def generate_sample(n=100, alpha=1.1, beta=.5):
    # Changing parametrization
    k = alpha
    theta = 1 / beta
    # Generating n-sized sample
    sample = np.random.gamma(shape=k, scale=theta, size=n)
    return sample


def generate_bootstrap_samples(sample, B=5000):
    # Generates B bootstrap samples
    n = sample.size
    # Maximum likelihood estimator for beta parameter of the exponential distribution is the sample mean
    beta = sample.mean()
    for _ in range(B):
        try:
            boot = np.concatenate((boot, np.random.exponential(scale=beta, size=n).reshape(1, -1)), axis=0)
        except NameError:
            boot = np.random.exponential(scale=beta, size=n).reshape(1, -1)
    return boot


def estimate_from_sample(sample):
    # Estimates s from the original sample
    n = sample.size
    A = sample.mean() ** 2
    B = sample.var(ddof=0)
    return A - B


def estimates_from_bootstrap(boot):
    # Estimates s for each bootsrap sample
    A = np.square(boot.mean(axis=1))
    B = boot.var(axis=1, ddof=0)
    return np.abs(A - B)


def estimate_quantile(sample, s_boot, s_sample, alpha=.05):
    # estimating std from original sample
    std_estimate = sample.mean()
    # obtaining the quantile estimator q numerically
    error = np.abs(s_boot - s_sample) / std_estimate
    error_range = np.linspace(error.min(), error.max(), num=10000)
    for q in error_range:
        if (error - q*std_estimate < 0).mean() >= 1 - alpha:
            return q


def bootstrap_interval(s_sample, q):
    return (s_sample - q, s_sample + q)


def wrapper():
    np.random.seed(10)
    sample = generate_sample()
    boot = generate_bootstrap_samples(sample)

    s_sample = estimate_from_sample(sample)
    s_boot = estimates_from_bootstrap(boot)
    q = estimate_quantile(sample, s_boot, s_sample)
    interval = bootstrap_interval(s_sample, q)
    print('bootstrap interval: ', interval)
    if interval[0] > 0 or interval[1] < 0:
        print('0 not in interval. Null hypothesis rejected: specified model is incorrect.')
    else:
        print('0 in interval. Null hypothesis accepted: specified model is correct.')


if __name__ == '__main__':
    wrapper()