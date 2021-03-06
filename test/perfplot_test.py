import numpy
import perfplot


def test():
    kernels = [lambda a: numpy.c_[a, a]]
    r = [2**k for k in range(4)]
    perfplot.show(
            setup=numpy.random.rand,
            kernels=kernels, labels=['c_'], n_range=r, xlabel='len(a)'
            )
    perfplot.show(
            setup=numpy.random.rand,
            kernels=kernels, labels=['c_'], n_range=r, xlabel='len(a)',
            logx=True, logy=False
            )
    perfplot.show(
            setup=numpy.random.rand,
            kernels=kernels, labels=['c_'], n_range=r, xlabel='len(a)',
            logx=False, logy=True
            )
    perfplot.show(
            setup=numpy.random.rand,
            kernels=kernels, labels=['c_'], n_range=r, xlabel='len(a)',
            logx=True, logy=True
            )
    return


def test_no_labels():
    def mytest(a):
        return numpy.c_[a, a]
    kernels = [mytest]
    r = [2**k for k in range(4)]
    perfplot.show(
            setup=numpy.random.rand,
            kernels=kernels, n_range=r, xlabel='len(a)'
            )
    return
