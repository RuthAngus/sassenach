# inject 1000 light curves into a quiet star.
# see how many you can recover using the ACF method over a grid of heuristics.
import numpy as np
import matplotlib.pyplot as plt
import mklc

def inject(pmin, pmin, amin, amax, EPIC):
    """
    pmin and pmax in days, amin and amax in ppm
    """

    periods = np.exp(np.random.uniform(np.log(pmin), np.log(pmax)))
    amps = np.exp(np.random.uniform(np.log(amin), np.log(amax)))

    # load test star data

    # generate simulated lc

    # add real data and simulated data

    # save the light curve

if __name__ == "__main__":
    inject(.5, 30., 10., 10000., "201121245")
