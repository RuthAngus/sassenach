# inject 1000 light curves into a quiet star.
# see how many you can recover using the ACF method over a grid of heuristics.
import numpy as np
import matplotlib.pyplot as plt
import mklc
import pyfits
import fitsio
import scipy.interpolate as spi

def simulate(EPIC, c=1, pmin=.5, pmax=100., amin=1e-3, amax=1e-1,
             nsim=1000, usereal=False):
    """
    pmin and pmax in days, amin and amax in ppm.
    """
    periods = np.exp(np.random.uniform(np.log(pmin), np.log(pmax), nsim))
    amps = np.exp(np.random.uniform(np.log(amin), np.log(amax), nsim))
    np.savetxt("true_periods.txt", np.transpose((np.arange(1000), periods,
               amps)))

    # load test star data
    fname = "hlsp_k2sff_k2_lightcurve_%s-c0%s_kepler_v1_llc.fits" % (EPIC, c)
    dname = "/export/bbq1/angusr/data/vanderburgC%s/%s" % (c, fname)
    data = fitsio.read(dname)
    time, raw, flux = [np.zeros(len(data)) for i in range(3)]
    for i in range(len(data)):
        time[i] = data[i][0]
        raw[i] = data[i][1]
        flux[i] = data[i][2] - 1

    if usereal:
        # fit and remove straight line
        AT = np.vstack((time, np.ones_like(time)))
        ATA = np.dot(AT, AT.T)
        m, c = np.dot(np.linalg.inv(ATA), np.dot(AT, flux))
        flux -= (m*time+c)

    std = np.std(flux)
    flux = np.zeros_like(time) + np.random.randn(len(time))*std

    for i, p in enumerate(periods):
        print i, "of ", len(periods), "\n"
        print "amps = ", amps[i]
        res0, res1 = mklc.mklc(time, p=p)
        nspot, ff, amp_err = res0
        time, area_tot, dF_tot, dF_tot0 = res1
        simflux = dF_tot0 / np.median(dF_tot0) - 1

        np.savetxt("simulations/%s.txt" % i, np.transpose((time, simflux)))

        plt.clf()
        plt.plot(time, simflux*amps[i]+flux, "k.")
        plt.savefig("simulations/%s" % i)
        plt.title("p = %s, a = %s" % (p, amps[i]))

if __name__ == "__main__":
    simulate("201121245", pmin=.5, pmax=100., nsim=1000)
