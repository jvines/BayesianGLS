import numpy as np
from numba import jit


def bayesian_generalized_lomb_scargle(data, times, uncerts, freqs):
    """Compute the BGLS.

    Parameters
    ----------
    data : array_like
        Data observations.

    times : array_like
        Data observation times.

    uncerts : array_like
        An array with the data uncertainties.

    freqs : array_like
        The target frequencies

    """
    return bgls(data, times, uncerts, freqs)


@jit(nopython=True)
def bgls(data, times, uncerts, freqs):
    """Compute the BGLS.

    Parameters
    ----------
    data : array_like
        Data observations.

    times : array_like
        Data observation times.

    uncerts : array_like
        An array with the data uncertainties.

    freqs : array_like
        The target frequencies

    """
    lnp = np.zeros(freqs.shape[0])
    for i, f in enumerate(freqs):
        lnp[i] = model(data, times, uncerts, f)
    return lnp


@jit(nopython=True)
def model(d, t, sig, f):
    """Compute the BGLS model.

    Parameters
    ----------
    d : array_like
        Data observations.

    t : array_like
        Data observation times.

    sig : array_like
        An array with the data uncertainties.

    f : float
        The target frequency

    """
    # Angular argument -> goes inside sines and cosines
    ang_arg = 2 * np.pi * f * t
    # Calculate weights
    w = 1 / sig**2
    # Calculate phase offset
    theta_up = (w * np.sin(2 * ang_arg)).sum()
    theta_down = (w * np.cos(2 * ang_arg)).sum()
    theta = .5 * np.arctan2(theta_up, theta_down)
    # Some definitions
    W = w.sum()
    Y = (w * d).sum()
    YY = (w * d**2).sum()
    YC = (w * d * np.cos(ang_arg - theta)).sum()
    YS = (w * d * np.sin(ang_arg - theta)).sum()
    C = (w * np.cos(ang_arg - theta)).sum()
    S = (w * np.sin(ang_arg - theta)).sum()
    CC = (w * np.cos(ang_arg - theta)**2).sum()
    SS = (w * np.sin(ang_arg - theta)**2).sum()
    # Functions of frequency
    K = (C**2 * SS + S**2 * CC - W * CC * SS) / (2 * CC * SS)
    L = (Y * CC * SS - C * YC * SS - S * YS * CC) / (CC * SS)
    M = (YC**2 * SS + YS**2 * CC) / (2 * CC * SS)
    # Final model
    mod = (M - L**2 / (4 * K)) - np.log(np.sqrt(abs(K) * CC * SS))
    return mod
