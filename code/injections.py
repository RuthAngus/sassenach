# inject 1000 light curves into a quiet star.
# see how many you can recover using the ACF method over a grid of heuristics.
import numpy as np
import matplotlib.pyplot as plt
import mklc
import pyfits
import fitsio

def inject(pmin, pmax, amin, amax, EPIC):
    """
    pmin and pmax in days, amin and amax in ppm
    """

    periods = np.exp(np.random.uniform(np.log(pmin), np.log(pmax)))
    amps = np.exp(np.random.uniform(np.log(amin), np.log(amax)))

    # load test star data
    fname = "hlsp_k2sff_k2_lightcurve_%s-c01_kepler_v1_llc.fits" % EPIC
    dname = "/export/bbq1/angusr/data/vanderburgC1/%s" % fname
#     hdulist = pyfits.open(dname)

    data = fitsio.read(dname)
    aps = fitsio.read(dname, 2)
    y = data["flux"][:, np.argmin(aps["cdpp6"])]
    x = data["time"]
    q = data["quality"]
    l = np.isfinite(y) * np.isfinite(x) * (q==0)
    y, x = y[l], x[l]
    print y, x

# #     print hdulist
#     print np.shape(hdulist)
#     tbdata = hdulist[0]
#     print tbdata
    assert 0
#     x, y, _ = np.genfromtxt("/export/bbq1/angusr/data/vanderburgc0/%s" % EPIC)

    # generate simulated lc

    # add real data and simulated data

    # save the light curve

if __name__ == "__main__":
    inject(.5, 30., 10., 10000., "201121245")
