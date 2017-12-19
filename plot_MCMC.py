''' 
Example script to plot the 2D contours of a MCMC chain using 
the getdist python package
'''
from getdist import plots, MCSamples
import numpy as np

def get_constraints(samples):
    for i, mean in enumerate(samples.getMeans()):
        upper = samples.confidence(i, upper=True, limfrac=0.05)
        print("\nupper limit 95 C.L. = %f" % upper)
        lower = samples.confidence(i, upper=False, limfrac=0.05)
        print("lower limit 95 C.L. = %f" % lower)
        print("%s = %f +/- %f +/- %f" % (samples.parLabel(i), mean, mean - samples.confidence(i, limfrac=0.16),\
        mean - samples.confidence(i, limfrac=0.025)) )
    return 

def main():
    mean = [0, 0, 0]
    cov = [[1, 0, 0], [0, 100, 0], [0, 0, 8]]
    x1, x2, x3 = np.random.multivariate_normal(mean, cov, 50000).T
    s1 = np.c_[x1, x2, x3]

    mean = [0.2, 0.5, 6.]
    cov = [[0.7, 0.3, 0.1], [0.3, 10, 0.25], [0.1, 0.25, 7]]
    x1, x2, x3 = np.random.multivariate_normal(mean, cov, 50000).T
    s2 = np.c_[x1, x2, x3]

    names = ['x_1', 'x_2', 'x_3']
    samples1 = MCSamples(samples=s1, labels=names, label='sample1')
    samples2 = MCSamples(samples=s2, labels=names, label='sample2')

    get_constraints(samples1)
    get_constraints(samples2)

    g = plots.getSubplotPlotter()
    g.triangle_plot([samples1, samples2], filled=True)
    g.export('triangle_plot.png')
    g.export('triangle_plot.pdf')
    return 


if __name__ == "__main__":
    main()
