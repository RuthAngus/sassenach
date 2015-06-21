import numpy as np
import matplotlib.pyplot as plt
from K2_ACF import corr_run

def test_ACF():

    max_factors = np.linspace(2., 1., 10)
    min_phs = np.linspace(.1, .5, 10)
    min_lphs = np.linspace(.1, .5, 10)

    IDs, true_ps, true_as = np.genfromtxt("true_periods.txt").T

    p_recovered = np.zeros(1000)
    p_recovered_err = np.zeros(1000)
    yes, no = [], []
    for i, mf in enumerate(max_factors):
        for j, true_p in enumerate(true_ps):
            x, y = genfromtxt("simulations/%s.txt" % j)
            p_recovered[j], p_recovered_err[j] = \
                    corr_run(x, y, np.ones_like(y)*1.-5)
            if true_p[j] < p_recovered[j] + p_recovered_err[j] or \
                    p_recovered[j] - p_recovered_err[j] < true_p[j]:
                yes.append(true_p[j])
            else: no.append(true_p[j])
        print "max_factor = ", mf, "nsuccess = ", len(yes), "nfail = ", len(no)

if __name__ == "__main__":
    test_ACF()
